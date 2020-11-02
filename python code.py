Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
def helpi():
    he=Toplevel(root)
    he.geometry("500x250")
    he.title("Help")
    msg=Message(he,text="For any querry Please contact on 1234554321",font=("times new roman",20,"bold"),fg='BLACK').place(x=130,y=70)
    
def done():
    success=Toplevel(root)
    success.geometry("1000x500")
    success.title("Status")
    if(cgpavalue.get()==1):
        
        #pputting values in the DBMS
        print("Data Added")
        connection=mysql.connector.connect(host='localhost',
                                      user='root',
                                      passwd='8520',
                                      db='erms')
        cu=connection.cursor()
        cu.execute("insert into employee values('%s',%d,'%s',%d,'%s','%s',%d)"%(namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),emailvalue.get(),adressvalue.get(),experiencevalue.get()))
        cu.close()
        connection.commit()
        connection.close()
        msg=Message(success,text="Application is successfully Submitted ",font=("times new roman",50,"bold"),fg='BLACK').place(x=300,y=100) 
    else:
        msg=Message(success,text="You cannot apply for this job ",font=("times new roman",50,"bold"),fg='BLACK').place(x=300,y=100) 
def check():
    cr=Toplevel(root)
    cr.geometry("424x214")
    if(passvalue.get()==compassvalue.get()):
        connection=mysql.connector.connect(host='localhost',
                                  user='root',
                                  passwd='8520',
                                  db='erms')
        cu=connection.cursor()
        cu.execute("insert into login values('%s',%d)"%(uservalue.get(),passvalue.get()))
        
        cu.close()
        connection.commit()
        connection.close()
        msg=Message(cr,text="Account Created Sucessfully.. ",font=("times new roman",20,"bold"),fg='BLACK').place(x=100,y=50)
        #print("sucessfully created")
    else:
        msg=Message(cr,text="Password and confirnm password didn't Match.. ",font=("times new roman",20,"bold"),fg='BLACK').place(x=100,y=50)
        #print("Not Matched")
def createacc():
    #print("account created")
    main=Toplevel(root)
    main.geometry("424x214")
    #Heading
    Label(main, text="Please Create New Account", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)
    main.title("Create Account")


    #Text for our form
    name = Label(main, text="Name")
    passw = Label(main, text="Password")
    compass = Label(main, text="Confirnm Password")
    email = Label(main, text="Email ID")
    user=Label(main, text="User Name")

    #Pack text for our form
    name.grid(row=1, column=2)
    email.grid(row=2, column=2)
    user.grid(row=3, column=2)
    passw.grid(row=4, column=2)
    compass.grid(row=5, column=2)


    #Entries for our form
    nameentry = Entry(main, textvariable=fnamevalue)
    passentry = Entry(main, textvariable=passvalue)
    compassentry = Entry(main, textvariable=compassvalue)
    emailentry = Entry(main, textvariable=emailidvalue)
    userentry = Entry(main, textvariable=uservalue)

    # Packing the Entries
    nameentry.grid(row=1, column=3)
    emailentry.grid(row=2, column=3)
    userentry.grid(row=3, column=3)
    passentry.grid(row=4, column=3)
    compassentry.grid(row=5, column=3)


    #Button & packing it and assigning it a command
    Button(main,text="Submit the Form", command=check).grid(row=7, column=3)
    main.mainloop()
    
def employee():
    connection=mysql.connector.connect(host='localhost',user='root',passwd='8520',db='erms')
    cu=connection.cursor()
    x=(0,0)
    cu.execute("select * from login where username='%s' and password=%d"%(u.get(),p.get()))
    for i in cu:x=i
    if(u.get()==x[0] and p.get()==x[1]):
        main=Toplevel(root)
        main.geometry("624x314")
        #Heading
        Label(main, text="Welcome to EMPLOYEE RECRUITMENT SYSTEM", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)
        main.title("EMPLOYEE RECRUITMENT MANAGEMENT SYSTEM")
        #Text for our form
        name = Label(main, text="Name")
        phone = Label(main, text="Phone")
        gender = Label(main, text="Gender")
        emergency = Label(main, text="Emergency Contact")
        email = Label(main, text="Email ID")
        adress=Label(main, text="Address")
        experience=Label(main, text="Experience")

        #Pack text for our form
        name.grid(row=1, column=2)
        phone.grid(row=2, column=2)
        gender.grid(row=3, column=2)
        emergency.grid(row=4, column=2)
        email.grid(row=5, column=2)
        adress.grid(row=6, column=2)
        experience.grid(row=7, column=2)
        

        #Entries for our form
        nameentry = Entry(main, textvariable=namevalue)
        phoneentry = Entry(main, textvariable=phonevalue)
        genderentry = Entry(main, textvariable=gendervalue)
        emergencyentry = Entry(main, textvariable=emergencyvalue)
        emailentry = Entry(main, textvariable=emailvalue)
        adressentry = Entry(main, textvariable=adressvalue)
        experienceentry = Entry(main, textvariable=experiencevalue)

        # Packing the Entries
        nameentry.grid(row=1, column=3)
        phoneentry.grid(row=2, column=3)
        genderentry.grid(row=3, column=3)
        emergencyentry.grid(row=4, column=3)
        emailentry.grid(row=5, column=3)
        adressentry.grid(row=6, column=3)
        experienceentry.grid(row=7, column=3)

        #Checkbox & Packing it
        cgpa = Checkbutton(main,text="Is Your Cgpa above 7.5", variable = cgpavalue)
        cgpa.grid(row=8, column=3)

        #Button & packing it and assigning it a command
        Button(main,text="Submit the Form", command=done).grid(row=9, column=3)
        
    else:
        success=Toplevel(root)
        success.geometry("1000x500")
        success.title("Status")
        #var=StringVar()  
        msg=Message(success,text="ACCESS DENIED ",font=("times new roman",50,"bold"),fg='BLACK').place(x=300,y=100)
        b=Button(success,text="PLEASE RETRY",font=("arial",13,"bold"),relief='raised',bg='black',fg='white',activebackground='grey',activeforeground='white',height=2,width=50,command=login).place(x=270,y=400)
        
def login():
    new=Toplevel(root)
    new.geometry("230x120")
    new.title("ERMS")
    login=Label(new,text="Please Login!!")
    user=Label(new,text="username")
    passw=Label(new,text="Password")
    user.grid(row=1,column=2)
    passw.grid(row=2,column=2)
    us=Entry(new,textvariable=u)
    pd=Entry(new,textvariable=p)
    login.grid(row=0,column=3)
    us.grid(row=1,column=3)
    pd.grid(row=2,column=3)
    Button(new,text="Submit",command=employee).grid(column=3)
    
root=Tk()
root.geometry("1000x500")
root.resizable(False,False)

# login variables
u=StringVar()
p=IntVar()

# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = IntVar()
gendervalue = StringVar()
emergencyvalue = IntVar()
emailvalue = StringVar()
cgpavalue = IntVar()
adressvalue=StringVar()
experiencevalue=IntVar()

#variables        
fnamevalue = StringVar()
passvalue = IntVar()
compassvalue = IntVar()
emailidvalue = StringVar()
uservalue=StringVar()

root.title('Employee Recruitment system')
i=Image.open(r"erms.jpg")  
i=i.resize((1000,500), Image.ANTIALIAS)
emp=Image.open(r"erm3.png")
emp=emp.resize((250,200),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(i)  
ph=ImageTk.PhotoImage(emp) 
cv = Canvas() 
cv.pack(side='top', fill='both', expand='yes')  
cv.create_image(0, 0, image=photo, anchor='nw')
b=Label(root,text="WELCOME TO THE EMPLOYEE RECRUITMENT SYSTEM",font=("arial",13,"bold"),relief='raised',bg='black',fg='white',height=2,width=50).place(x=270,y=40)
l=Button(root,text="Login",font=("arial",13,"bold"),relief='raised',bg='black',fg='white',activebackground='grey',activeforeground='white',height=2,width=30,command=login).place(x=100,y=400)
c=Button(root,text="Create Account",font=("arial",13,"bold"),relief='raised',bg='black',fg='white',activebackground='grey',activeforeground='white',height=2,width=30,command=createacc).place(x=600,y=400)
h=Button(root,text="HELP",font=("arial",9,"bold"),relief='raised',bg='black',fg='white',activebackground='grey',activeforeground='white',height=2,width=20,command=helpi).place(x=70,y=40)
e=Label(root,image=ph).place(x=420,y=150)
root.mainloop()