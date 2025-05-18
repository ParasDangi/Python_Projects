import sqlite3
from docx import Document
from tkinter import *
from tkinter import messagebox
import os
import subprocess
import threading

# --- Fill Word Template ---
def fill_word_template(data, template_path='template.docx', output_path='filled.docx'):
    doc = Document(template_path)
    for paragraph in doc.paragraphs:
        paragraph.text = paragraph.text.replace('{name}', data[0])
        paragraph.text = paragraph.text.replace('{email}', data[1])
        paragraph.text = paragraph.text.replace('{score}', str(data[2]))
        paragraph.text = paragraph.text.replace('{DOB}', str(data[3]))
    doc.save(output_path)

# --- Convert Multiple DOCX to PDF ---
def convert_multiple_docx_to_pdf(docx_pdf_pairs):
    import win32com.client
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False
    for docx_path, pdf_path in docx_pdf_pairs:
        doc = word.Documents.Open(os.path.abspath(docx_path))
        doc.SaveAs(os.path.abspath(pdf_path), FileFormat=17)
        doc.Close()
        os.remove(docx_path)  # delete temp docx
    word.Quit()

# --- Background worker ---
def generate_reports_worker(ids, file_type, auto_open, generate_button):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        pdf_jobs = []
        generated_files = []
        first_file_path = None

        for unique_id in ids:
            cursor.execute("SELECT name, email, score, DOB FROM candidates WHERE id = ?", (unique_id,))
            data = cursor.fetchone()
            if data:
                name_clean = data[0].replace(" ", "_")
                output_docx = f"{name_clean}_{unique_id}.docx"
                output_pdf = f"{name_clean}_{unique_id}.pdf"

                if file_type == "docx":
                    fill_word_template(data, output_path=output_docx)
                    generated_files.append(output_docx)
                    if not first_file_path:
                        first_file_path = output_docx

                elif file_type == "pdf":
                    fill_word_template(data, output_path=output_docx)
                    pdf_jobs.append((output_docx, output_pdf))
                    generated_files.append(output_pdf)
                    if not first_file_path:
                        first_file_path = output_pdf
            else:
                print(f"No candidate found with ID: {unique_id}")

        if file_type == "pdf" and pdf_jobs:
            convert_multiple_docx_to_pdf(pdf_jobs)

        conn.close()

        # Notify user after work completes
        root.after(0, lambda: post_generation_feedback(generated_files, auto_open, first_file_path, generate_button))

    except Exception as e:
        root.after(0, lambda: messagebox.showerror("Error", str(e)))
        generate_button.config(state=NORMAL)

# --- After work completes ---
def post_generation_feedback(generated_files, auto_open, first_file_path, button):
    if generated_files:
        messagebox.showinfo("Success", f"{len(generated_files)} file(s) generated successfully.")
        if auto_open and first_file_path:
            subprocess.Popen(['start', first_file_path], shell=True)
    else:
        messagebox.showwarning("No Files", "No reports were generated.")
    button.config(state=NORMAL)

# --- Trigger Thread ---
def start_report_generation():
    ids_input = entry.get().strip()
    file_type = file_choice.get()
    auto_open = open_after.get()
    generate_button.config(state=DISABLED)

    if not ids_input:
        messagebox.showerror("Invalid Input", "Please enter at least one candidate ID.")
        generate_button.config(state=NORMAL)
        return

    ids = [id.strip() for id in ids_input.split(',') if id.strip().isdigit()]
    if not ids:
        messagebox.showerror("Invalid Input", "Please enter only numeric IDs separated by commas.")
        generate_button.config(state=NORMAL)
        return

    # Start background thread
    threading.Thread(target=generate_reports_worker, args=(ids, file_type, auto_open, generate_button)).start()

# --- GUI Setup ---
root = Tk()
root.title("Candidate Report Generator")
root.geometry("420x280")

Label(root, text="Enter Candidate ID(s): (e.g. 1, 3, 5)").pack(pady=8)
entry = Entry(root, width=40)
entry.pack()

file_choice = StringVar()
file_choice.set("pdf")  # Default

Label(root, text="Select Output Format:").pack(pady=5)
Radiobutton(root, text="Generate PDF", variable=file_choice, value="pdf").pack()
Radiobutton(root, text="Generate DOCX", variable=file_choice, value="docx").pack()

open_after = BooleanVar()
Checkbutton(root, text="Open first file after generation", variable=open_after).pack(pady=8)

generate_button = Button(root, text="Generate Report(s)", command=start_report_generation)
generate_button.pack(pady=10)

root.mainloop()
