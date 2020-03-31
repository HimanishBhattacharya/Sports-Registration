import tkinter
from tkinter import *
import back 

#Creating the window object
app=Tk()

#Adding the labels----------------------------------------------------------------------------------------------------------------
    #Header Label--------------------------------------------------------------------------------------
Label(app,text="MEALS", font=("bold",22),bg="darkblue",fg="white",width=20).grid(row=0, column=0,columnspan=3, padx=20,pady=20)
Label(app,text="RECEIPT", font=("bold",22),bg="darkblue",fg="white").grid(row=0, column=3, padx=20,pady=20)
Button(app,text="Send", font=("bold",14),width=8,bg="yellow",fg="darkblue",command=_clear).grid(row=0,column=4,pady=20)
    #Meal items Label-------------------------------------------------------------------------------
Label(app,text="Veg Burger (40)",font=("bold",14),fg="white",bg="blue").grid(row=1, column=0, padx=20,pady=10)
Label(app,text="Chicken Burger (60)", font=("bold",14),fg="white",bg="blue").grid(row=2, column=0, padx=20,pady=10)
Label(app,text="Cheese Sandwich (50)", font=("bold",14),fg="white",bg="blue").grid(row=3, column=0, padx=20,pady=10)
Label(app,text="Chicken Sandwich (70)", font=("bold",14),fg="white",bg="blue").grid(row=4, column=0, padx=20,pady=10)
Label(app,text="French Fries (35)", font=("bold",14),fg="white",bg="blue").grid(row=5, column=0, padx=20,pady=10)
Label(app,text="Chicken Nuggets (55)", font=("bold",14),fg="white",bg="blue").grid(row=6, column=0, padx=20,pady=10)
Label(app,text="Coke (15)", font=("bold",14),fg="white",bg="blue").grid(row=7, column=0, padx=20,pady=10)
Label(app,text="Milk Shake (25)", font=("bold",14),fg="white",bg="blue").grid(row=8, column=0, padx=20,pady=10)
Label(app,text="Lime Juice (10)", font=("bold",14),fg="white",bg="blue").grid(row=9, column=0, padx=20,pady=10)
Label(app,text="Mango Shake (35)", font=("bold",14),fg="white",bg="blue").grid(row=10, column=0, padx=20,pady=10)


#Functions to show the prices---------------------------------------------------

def showvegbprice():    #VEG BURGER
    #calling function from back.py
    p_vegb['text']=str(back.enter_vegb(int(nvegb.get())))

def showchkbprice():
    #calling function from back.py
    price_chkb.set(str(back.enter_chkb(int(nchkb.get()))))

def showchsndprice():    #VEG BURGER
    #calling function from back.py
    p_chsd['text']=str(back.enter_chsnd(int(nchsd.get())))

def showchksdprice():    #CHICKEN BURGER
    #calling function from back.py
    p_chksd['text']=str(back.enter_chksd(int(nchksd.get())))

def showffprice():    #CHEESE SANDWICH
    #calling function from back.py
    p_ff['text']=str(back.enter_ff(int(nff.get())))

def showchkngprice():    #CHICKEN SANDWICH
    #calling function from back.py
    p_chkng['text']=str(back.enter_chkng(int(nchkng.get())))

def showcokeprice():    #COKE
    #calling function from back.py
    p_coke['text']=str(back.enter_coke(int(ncoke.get())))

def showmilksprice():    #MILK SHAKE
    #calling function from back.py
    p_milks['text']=str(back.enter_milks(int(nmilks.get())))

def showlimejprice():    #LIME JUICE
    #calling function from back.py
    p_limej['text']=str(back.enter_limej(int(nlimej.get())))

def showmanshprice():    #MANGO SHAKE
    #calling function from back.py
    p_mansh['text']=str(back.enter_mansh(int(nmansh.get())))



    #Meal items units-----------------------------------------------------------------
nvegb=StringVar()
n_vegb=Entry(app,width=4,textvariable=nvegb,validate="focusout",validatecommand=showvegbprice)   #vegburger
n_vegb.grid(row=1,column=1,padx=20,pady=5)

nchkb=StringVar()
n_chkb=Entry(app,width=4,textvariable=nchkb,validate="focusout",validatecommand=showchkbprice)   #chickenburger
n_chkb.grid(row=2,column=1,padx=20,pady=5)

nchsd=StringVar()
n_chsd=Entry(app,width=4,textvariable=nchsd,validate="focusout",validatecommand=showchsndprice)   #cheesesandwich
n_chsd.grid(row=3,column=1,padx=20,pady=5)

nchksd=StringVar()
n_chksd=Entry(app,width=4,textvariable=nchksd,validate="focusout",validatecommand=showchksdprice)  #chickensandwich
n_chksd.grid(row=4,column=1,padx=20,pady=5)

nff=StringVar()
n_ff=Entry(app,width=4,textvariable=nff,validate="focusout",validatecommand=showffprice)     #frenchfries
n_ff.grid(row=5,column=1,padx=20,pady=5)

nchkng=StringVar()
n_chkng=Entry(app,width=4,textvariable=nchkng,validate="focusout",validatecommand=showchkngprice)  #chickennuggets
n_chkng.grid(row=6,column=1,padx=20,pady=5)

ncoke=StringVar()
n_coke=Entry(app,width=4,textvariable=ncoke,validate="focusout",validatecommand=showcokeprice)  #coke
n_coke.grid(row=7,column=1,padx=20,pady=5)

nmilks=StringVar()
n_milks=Entry(app,width=4,textvariable=nmilks,validate="focusout",validatecommand=showmilksprice)  #milkshake
n_milks.grid(row=8,column=1,padx=20,pady=5)

nlimej=StringVar()
n_limej=Entry(app,width=4,textvariable=nlimej,validate="focusout",validatecommand=showlimejprice)  #limejuice
n_limej.grid(row=9,column=1,padx=20,pady=5)

nmansh=StringVar()
n_mansh=Entry(app,width=4,textvariable=nmansh,validate="focusout",validatecommand=showmanshprice)  #mangoshake
n_mansh.grid(row=10,column=1,padx=20,pady=5)



#-----------------#Meal item Total prices----------------------------------------
p_vegb=Label(app,width=10,text="")   #vegburger
p_vegb.grid(row=1,column=2,padx=20,pady=5)

price_chkb=StringVar(app,"")
p_chkb=Label(app,width=10,textvariable=price_chkb)   #chickenburger
p_chkb.grid(row=2,column=2,padx=20,pady=5)

p_chsd=Label(app,width=10)   #cheesesandwich
p_chsd.grid(row=3,column=2,padx=20,pady=5)

p_chksd=Label(app,width=10)  #chickensandwich
p_chksd.grid(row=4,column=2,padx=20,pady=5)

p_ff=Label(app,width=10)     #frenchfries
p_ff.grid(row=5,column=2,padx=20,pady=5)

p_chkng=Label(app,width=10)  #chickennuggets
p_chkng.grid(row=6,column=2,padx=20,pady=5)

p_coke=Label(app,width=10)  #coke
p_coke.grid(row=7,column=2,padx=20,pady=5)

p_milks=Label(app,width=10)  #milkshake
p_milks.grid(row=8,column=2,padx=20,pady=5)

p_limej=Label(app,width=10)  #limejuice
p_limej.grid(row=9,column=2,padx=20,pady=5)

p_mansh=Label(app,width=10)  #mangoshake
p_mansh.grid(row=10,column=2,padx=20,pady=5)


#Tax and Subtotal calculations----------------------------------------------------------------------------------------
tax=0
subtotal=0
def cal_tax_and_subtotal():
    global tax
    global subtotal

    if(nvegb.get()!=""):
        tax+=int(nvegb.get())*back.tax_vegb
        subtotal+=int(nvegb.get())*back.cost_vegb
    if(nchkb.get()!=""):
        tax+=int(nchkb.get())*back.tax_chkb
        subtotal+=int(nchkb.get())*back.cost_chkb
    if(nchsd.get()!=""):
        tax+=int(nchsd.get())*back.tax_chsnd
        subtotal+=int(nchsd.get())*back.cost_chsnd
    if(nchksd.get()!=""):
        tax+=int(nchksd.get())*back.tax_chksd
        subtotal+=int(nchksd.get())*back.cost_chksd
    if(nff.get()!=""):
        tax+=int(nff.get())*back.tax_ff
        subtotal+=int(nff.get())*back.cost_ff
    if(nchkng.get()!=""):
        tax+=int(nchkng.get())*back.tax_chkng
        subtotal+=int(nchkng.get())*back.cost_chkng
    if(ncoke.get()!=""):
        tax+=int(ncoke.get())*back.tax_coke
        subtotal+=int(ncoke.get())*back.cost_coke
    if(nmilks.get()!=""):
        tax+=int(nmilks.get())*back.tax_milks
        subtotal+=int(nmilks.get())*back.cost_milks
    if(nlimej.get()!=""):
        tax+=int(nlimej.get())*back.tax_limej
        subtotal+=int(nlimej.get())*back.cost_limej
    if(nmansh.get()!=""):
        tax+=int(nmansh.get())*back.tax_mansh
        subtotal+=int(nmansh.get())*back.cost_mansh
    tax_label['text']=str(tax)
    subtotal_label['text']=str(subtotal)

#Text Box for Bill--------------------------------------------------------------------------------------------

Text(app,width=32,height=28).grid(row=1,column=3,rowspan=10,columnspan=4)



#Buttons and Email----------------------------------------------------------------------------------------------

email=StringVar()
Label(app,text="Customer Email",width=12,font=("bold",14),fg="yellow",bg="blue").grid(row=11,column=0,pady=20)
Entry(app,textvariable=email,width=30,font=("bold",11),validate="focusin",validatecommand=cal_tax_and_subtotal).grid(row=11,column=1,columnspan=2,pady=20)
Button(app,text="Close",width=8,font=("bold",14),bg="red",fg="white",command=close).grid(row=12,column=0,pady=20)
Button(app,text="Receipt",width=8,font=("bold",14),bg="darkblue",fg="white",command=_clear).grid(row=12,column=1,pady=20)
Button(app,text="Clear",width=8,command=_clear,font=("bold",14),bg="black",fg="white").grid(row=12,column=2,pady=20)

def _clear():
    print ("123")
#function to clear contents
def _clear_():
    nvegb.set("")
    n_chkb.delete(0,END)
    n_chkng.delete(0,END)
    n_chksd.delete(0,END)
    n_chsd.delete(0,END)
    n_coke.delete(0,END)
    n_ff.delete(0,END)
    n_limej.delete(0,END)
    n_mansh.delete(0,END)
    n_milks.delete(0,END)
#close the application
def close():
    app.destroy()

#Tax and Subtotal

Label(app,text="Tax",font=('bold',14),width=5,bg="blue",fg="white").grid(row=11,column=3)
tax_label=Label(app,text="",font=('bold',14),width=8)
tax_label.grid(row=11,column=4)

Label(app,text="Sub-Total",font=('bold',14),width=8,bg="blue",fg="white").grid(row=12,column=3)
subtotal_label=Label(app,text="",font=('bold',14),width=8)
subtotal_label.grid(row=12,column=4,padx=10)



#Title of the window
app.title("Billing Application")

#Background color configuration for the window
app.configure(background="blue")

#Sizing and positioning the window
app.geometry("800x700+200+10")



#Start the program
app.mainloop()
