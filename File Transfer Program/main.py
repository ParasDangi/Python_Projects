from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

root=Tk()
root.title("Share_file")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)
    
def Send():
    window=Toplevel(root)
    window.title("send")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)

    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title='Select Image File',
                                            filetype=(('file_type','*.txt'),('all files','*.*')))

    def Sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8000
        s.bind((host,port))
        s.listen(1)
        print(host)
        print('waiting for any incoming connections.........')
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted sucessfully...")


    #icon
    image_icon1=PhotoImage(file="Image/send.png")
    window.iconphoto(False,image_icon1)

    Sbackground=PhotoImage(file="Image/sender.png")
    Label(window,image=Sbackground).place(x=-2,y=0)

    Mbackground=PhotoImage(file="Image/id.png")
    Label(window,image=Mbackground,bg='#f4fdfe').place(x=100,y=260)

    host=socket.gethostname()
    Label(window,text=f'ID:{host}',bg='white',fg='black').place(x=140,y=290)


    Button(window,text="+ select file",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=select_file).place(x=160,y=150)
    Button(window,text="SEND",width=8,height=1,font='arial 14 bold',bg='#000',fg="#fff",command=Sender).place(x=300,y=150)
    window.mainloop()

def Receive():
    window1=Toplevel(root)
    window1.title("Receive")
    window1.geometry('450x560+500+200')
    window1.configure(bg="#f4fdfe")
    window1.resizable(False,False)

    def receiver():
        ID=SenderID.get()
        filename1=incoming_file.get()
        
        s=socket.socket()
        port=8000
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully")
        
    #icon
    image_icon1=PhotoImage(file="Image/receive.png")
    window1.iconphoto(False,image_icon1)

    Hbackground=PhotoImage(file="Image/receiver.png")
    Label(window1,image=Hbackground).place(x=-2,y=0)

    logo=PhotoImage(file="Image/profile.png")
    Label(window1,image=logo,bg="#f4fdfe").place(x=10,y=250)

    Label(window1,text="Receive",font=('arail',20),bg='#f4fdfe').place(x=100,y=280)

    Label(window1,text="Input sender id",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=340)
    SenderID=Entry(window1,width=25,fg="black",border=2,bg='white',font=('arial',15))
    SenderID.place(x=20,y=370)
    SenderID.focus()

    Label(window1,text="filename for the incoming file:",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=420)
    incoming_file=Entry(window1,width=25,fg="black",border=2,bg='white',font=('arial',15))
    incoming_file.place(x=20,y=450)

    imageicon=PhotoImage(file="Image/arrow.png")
    rr=Button(window1,text='Receive',compound=LEFT,image=imageicon,width=130,bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=500)


    window1.mainloop()
#icon
image_icon=PhotoImage(file="Image/icon.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font=('Acumin variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)
Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)

send_image=PhotoImage(file="Image/send.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=Send)
send.place(x=50,y=100)

receive_image=PhotoImage(file="Image/receive.png")
receive=Button(root,image=receive_image,bg="#f4fdfe",bd=0,command=Receive)
receive.place(x=300,y=100)

#label
Label(root,text="send",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=65,y=200)
Label(root,text="Receive",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=300,y=200)

background=PhotoImage(file="Image/background.png")
Label(root,image=background).place(x=-2,y=323)
root.mainloop()