import tkinter
from tkinter import *
import dataase as db
import smtplib


#Creating Window Object
app=Tk()

#Student Details 
#name
student_name=StringVar()
name_label=Label(app,text='Name',font=('bold',10),pady=20,padx=10,bg="orange").grid(row=0,column=0)
name_entry=Entry(app,textvariable=student_name,width=30,border=0)
name_entry.grid(row=0,column=1)

#email
student_email=StringVar()
email_label=Label(app,text='Email',font=('bold',10),padx=10,bg="orange").grid(row=1,column=0)
email_entry=Entry(app,textvariable=student_email,width=30,border=0)
email_entry.grid(row=1,column=1)

#phone
student_phone=StringVar()
phone_label=Label(app,text='Phone',font=('bold',10),pady=20,padx=10,bg="orange").grid(row=2,column=0)
phone_entry=Entry(app,textvariable=student_phone,width=30,border=0)
phone_entry.grid(row=2,column=1)

def _clear():
    name_entry.delete(0,END)
    email_entry.delete(0,END)
    phone_entry.delete(0,END)
    student_game.set('')

#Clear Buttons
clear=Button(app,text='Clear',width=8,height=1,command=_clear,bg="green",activebackground="red",activeforeground="white",border=0)
clear.grid(row=3,column=1,pady=10)

#show club 
def show_club():
    selecteditem=listbox.curselection()
    for item in selecteditem:
        student_game.set(listbox.get(item))

#select game
student_game=StringVar()
game_label=Label(app,text="Game Club",font=('bold',10),pady=20,padx=10,bg="orange").grid(row=4,column=0)
game_text=Label(app,textvariable=student_game,height=1,width=20,bg="white")
game_text.grid(row=4,column=1)
game_select=Button(app,text="Select",height=1,width=6,bg="blue",activebackground="yellow",activeforeground="blue",command=show_club,border=0)
game_select.grid(row=4,column=2)
listbox=Listbox(app,height=3,width=33,border=0,selectmode=EXTENDED)
listbox.grid(row=5,column=1,columnspan=2)
game_select=Scrollbar(app)
game_select.grid(row=5,column=2)
listbox.configure(yscrollcommand=game_select.set)
game_select.configure(command=listbox.yview)
listbox.insert(1,'Football Club')
listbox.insert(2,'Cricket Club')
listbox.insert(3,'BasketBall Club')
listbox.insert(4,'Table Tennis Club')
listbox.insert(5,'VolleyBall Club')
listbox.insert(6,'PUBG Club')



#insert function calling
def register():
    #Validation for empty fields
    if student_name.get()=='' or student_email.get()=='' or student_phone.get()=='':
        Label(app,text='Fill all the fields',font=("bold",10),bg="orange").grid(row=7,column=1)
    else:
        db.insert(student_name.get(),student_email.get(),student_phone.get(),student_game.get())
        Label(app,text='Entry Registered',font=("bold",10),bg="orange").grid(row=7,column=1)
                #Sending confirmation mail:
#Creating SMTP server
        s=smtplib.SMTP('smtp.gmail.com',587)

#Start TLS for security
        s.starttls()

#Authentication
        s.login('errorfruit@gmail.com','esymjffxcfidrslj')

#message to be sent
        sender="errorfruit@gmail.com"
        receiver=student_email.get()
        msg="To: "+student_name.get()+"("+student_email.get()+")"+"\n"+"From: "+sender+"\n"+"You have successfully registered yourself in "+student_game.get()
        _clear()
#sending the mail
        s.sendmail(sender,receiver,msg)

#terminating the session
        s.quit


#Register Buttons
register=Button(app,text='Register',width=8,height=1,command=register,bg="green",activebackground="blue",activeforeground="white",border=0)
register.grid(row=6,column=1,pady=20)
i=1

#Window for members
def new_window():
    app2=Tk()
    #cancel function
    def cancel():
        app2.destroy()
        
#Retreiving from database
    def football():
        mem_listbox.delete(0,END)
        rem=db.football_members()
        for x in rem:
            mem_listbox.insert(END,str(x[0])+" "+x[1]+"     "+x[2]+'\n')
        

    def volleyball():
        mem_listbox.delete(0,END)
        for x in db.volleyball_members():
            mem_listbox.insert(END,str(x[0])+" "+x[1]+"     "+x[2]+'\n')

    def table_tennis():
        mem_listbox.delete(0,END)
        for x in db.tt_members():
            mem_listbox.insert(END,str(x[0])+" "+x[1]+"     "+x[2]+'\n')

    def cricket():
        mem_listbox.delete(0,END)
        for x in db.Cricket_members():
            mem_listbox.insert(END,str(x[0])+" "+x[1]+"     "+x[2]+'\n')
        

    def pubg():
        mem_listbox.delete(0,END)
        for x in db.pubg_members():
            mem_listbox.insert(END,str(x[0])+" "+x[1]+"     "+x[2]+'\n')

    def basketball():
        mem_listbox.delete(0,END)
        for x in db.Basketball_members():
            mem_listbox.insert(END,str(x[0])+" "+x[1]+"     "+x[2]+'\n')

    #cancel button
    mem_cancel=Button(app2,text='Cancel',height=1,width=10,command=cancel,bg="yellow",activebackground="red",activeforeground="white",border=0)
    mem_cancel.grid(row=2,column=1,pady=20)

    #volleyball Club
    mem_vol=Button(app2,height=1,width=10,text='VolleyBall',bg="orange",command=volleyball,activebackground="yellow",activeforeground="blue",border=0)
    mem_vol.grid(row=0,column=0,pady=20,padx=20)

    #Football Club
    mem_foot=Button(app2,height=1,width=10,text='FootBall',bg="orange",command=football,activebackground="yellow",activeforeground="blue",border=0)
    mem_foot.grid(row=0,column=1,pady=20,padx=20)

    #Cricket Club
    mem_cri=Button(app2,height=1,width=10,text='Cricket',bg="orange",command=cricket,activebackground="yellow",activeforeground="blue",border=0)
    mem_cri.grid(row=0,column=2,pady=20,padx=20)

    #BaseketBall Club
    mem_bas=Button(app2,height=1,width=10,text='BasketBall',bg="orange",command=basketball,activebackground="yellow",activeforeground="blue",border=0)
    mem_bas.grid(row=1,column=0,pady=20,padx=20) 

    #TableTennis Club
    mem_tt=Button(app2,height=1,width=10,text='Table Tennis',bg="orange",command=table_tennis,activebackground="yellow",activeforeground="blue",border=0)
    mem_tt.grid(row=1,column=1,pady=20,padx=20)

    #PUBG Club
    mem_pubg=Button(app2,height=1,width=10,text='PUBG',bg="orange",command=pubg,activebackground="yellow",activeforeground="blue",border=0)
    mem_pubg.grid(row=1,column=2,pady=20,padx=20)   

    #main list box
    mem_listbox=Listbox(app2,width=50)
    mem_listbox.grid(row=3,column=0,columnspan=3,pady=20)



    app2.title('Registered Members')
    app2.configure(background="green")
    app2.geometry('360x420+500+100')

    #Start Program
    app2.mainloop()

#to see all registered members members 
Button(app,text='See Registered Members',command=new_window,bg="green",activebackground="red",activeforeground="white",border=0).grid(row=8,column=1,pady=20)

app.title('SPORTS CLUB')
app.configure(background="orange")
app.geometry('350x460+400+100')

#Starting Program
app.mainloop()