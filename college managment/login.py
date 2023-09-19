#imports
from tkinter import *
#from tkinter.ttk import *
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3

#creating main windows

root=Tk()
root.title("College Managment by VK")
root.geometry("1200x700+220+50")
root.resizable(0,0)
root.iconbitmap("images_u/school.ico")

#loading images

lbg=ImageTk.PhotoImage(Image.open("images_u/logBg.png"))

sbg=Image.open("images_u/graduated.png")
sbg=sbg.resize((100,100),Image.ANTIALIAS)
sbg=ImageTk.PhotoImage(sbg)

sbg1=Image.open("images_u/graduated1.png")
sbg1=sbg1.resize((60,60),Image.ANTIALIAS)
sbg1=ImageTk.PhotoImage(sbg1)

tbg=Image.open("images_u/teacher.png")
tbg=tbg.resize((100,100),Image.ANTIALIAS)
tbg=ImageTk.PhotoImage(tbg)

tbg1=Image.open("images_u/teacher1.png")
tbg1=tbg1.resize((60,60),Image.ANTIALIAS)
tbg1=ImageTk.PhotoImage(tbg1)

abg=Image.open("images_u/settings.png")
abg=abg.resize((100,100),Image.ANTIALIAS)
abg=ImageTk.PhotoImage(abg)

lbgst=ImageTk.PhotoImage(Image.open("images_u/logBgst.png"))
lbgte=ImageTk.PhotoImage(Image.open("images_u/logBgte.png"))
lbgad=ImageTk.PhotoImage(Image.open("images_u/logBgad.png"))
stnav=ImageTk.PhotoImage(Image.open("images_u/stnav.png"))

stloc="temp_/savestimg/"+"195001"+".png"
stimgs=Image.open(stloc)
stimgs=stimgs.resize((300,300),Image.ANTIALIAS)
stimgs=ImageTk.PhotoImage(stimgs)

#functions

def stdetbtnfn():
    c=sqlite3.connect('college-db.db')
    cursor = c.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute("SELECT * FROM std_info WHERE roll_num=?",(195001,))
    stddet=cursor.fetchall()
    c.commit()
    cursor.close()
    if c:
        c.close()
        print("sqlite connection is closed")


    stfr=Frame(root,width=900,height=700)
    stfr.place(x=300,y=0)

    canvas = Canvas(stfr,width=900,height=700, bg='#61a0ff')
    canvas.place(x=0,y=0)   

    stimgl=Label(stfr,image=stimgs,bg="#61a0ff")
    stimgl.place(x=550,y=50)

    stnl=Label(stfr,text="Name : ",font=("",14,""),bg="#61a0ff",fg="White")
    stnl.place(x=113,y=50)

    stne=Entry(stfr,width=15,font=("",14,""),bg="#61a0ff",fg="White")
    stne.place(x=185,y=50)
    stne.insert(0," "+stddet[0][0])
    stne.config(state='disabled')

    strnl=Label(stfr,text="Roll Number : ",font=("",14,""),bg="#61a0ff",fg="White")
    strnl.place(x=57,y=100)
    
    strne=Entry(stfr,width=15,font=("",14,""),bg="#61a0ff",fg="White")
    strne.place(x=185,y=100)
    strne.insert(0," "+stddet[0][1])
    strne.config(state='disabled')

    strgl=Label(stfr,text="Register Number : ",font=("",14,""),bg="#61a0ff",fg="White")
    strgl.place(x=20,y=150)

    strge=Entry(stfr,width=15,font=("",14,""),bg="#61a0ff",fg="White")
    strge.place(x=185,y=150)
    strge.insert(0," "+stddet[0][2])
    strge.config(state='disabled')

    stdpl=Label(stfr,text="Department : ",font=("",14,""),bg="#61a0ff",fg="White")
    stdpl.place(x=63,y=200)

    stdpe=Entry(stfr,width=5,font=("",14,""),bg="#61a0ff",fg="White")
    stdpe.place(x=185,y=200)
    stdpe.insert(0,"   "+stddet[0][3])
    stdpe.config(state='disabled')

    stdobl=Label(stfr,text="Date of Birth : ",font=("",14,""),bg="#61a0ff",fg="White")
    stdobl.place(x=57,y=250)

    stdobe=Entry(stfr,width=15,font=("",14,""),bg="#61a0ff",fg="White")
    stdobe.place(x=185,y=250)
    stdobe.insert(0,"  "+stddet[0][4])
    stdobe.config(state='disabled')

    stdojl=Label(stfr,text="Date of Joining : ",font=("",14,""),bg="#61a0ff",fg="White")
    stdojl.place(x=37,y=300)

    stdoje=Entry(stfr,width=15,font=("",14,""),bg="#61a0ff",fg="White")
    stdoje.place(x=185,y=300)
    stdoje.insert(0,"  "+stddet[0][5])
    stdoje.config(state='disabled')

    stpnol=Label(stfr,text="Phone Number : ",font=("",14,""),bg="#61a0ff",fg="White")
    stpnol.place(x=41,y=350)

    stpnoe=Entry(stfr,width=15,font=("",14,""),bg="#61a0ff",fg="White")
    stpnoe.place(x=185,y=350)
    stpnoe.insert(0,"  "+stddet[0][6])
    stpnoe.config(state='disabled')

    staddl=Label(stfr,text="Address : ",font=("",14,""),bg="#61a0ff",fg="White")
    staddl.place(x=95,y=400)

    staddt=Text(stfr,font=("",14,""),height=5, width=20)
    staddt.place(x=185,y=400)
    staddt.insert(END, " "+stddet[0][7])
    staddt.config(state='disabled')

    stcsl=Label(stfr,text="Current semester : ",font=("",14,""),bg="#61a0ff",fg="White")
    stcsl.place(x=550,y=380)

    stcgpal=Label(stfr,text="CGPA : ",font=("",14,""),bg="#61a0ff",fg="White")
    stcgpal.place(x=642,y=415)

def dets():
    df=Frame(root,width=900,height=700,bg='white')
    df.place(x=300,y=0)

def logoutask(n):
    ans=messagebox.askyesno("Logout","Do you really want to logout")
    if ans:
        logpg()
    else:
        if n==1:
            stport()
        elif n==2:
            teport()
        elif n==3:
            adport()

def stport():
    clr(root)
    dets()
    bgn="#03256c"
    bgn2="#1768ac"

    btnfs=Frame(root,width=300,height=700,bg='white')
    btnfs.place(x=0,y=0)

    canvas = Canvas(btnfs,width=300, height=700, bg='white')
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0,0, image=stnav, anchor=NW)



    welli=Label(btnfs,image=sbg1,bg=bgn)
    welli.place(x=16,y=23)

    well=Label(btnfs,text="Welcome Venkatesh T",font=("",14,""),bg=bgn,fg="white")
    well.place(x=75,y=40)

    detbtnv=Button(btnfs,text="Details",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white",command=stdetbtnfn)
    detbtnv.place(y=130,x=5)

    intmbtnv=Button(btnfs,text="Internal marks",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    intmbtnv.place(y=180,x=5)

    extmbtnv=Button(btnfs,text="External marks",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    extmbtnv.place(y=230,x=5)

    quizbtnv=Button(btnfs,text="CT/CIT",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    quizbtnv.place(y=280,x=5)

    assbtnv=Button(btnfs,text="Assignment",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    assbtnv.place(y=330,x=5)

    stdybtnv=Button(btnfs,text="Study material",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    stdybtnv.place(y=380,x=5)

    attenbtnv=Button(btnfs,text="Attendence",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    attenbtnv.place(y=430,x=5)

    cirbtnv=Button(btnfs,text="Circular",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    cirbtnv.place(y=480,x=5)

    gencombtnv=Button(btnfs,text="Genrate my report",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    gencombtnv.place(y=530,x=5)

    logoutbtnv=Button(btnfs,text="Logout",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white",command=lambda:logoutask(1))
    logoutbtnv.place(y=580,x=5)

    stdetbtnfn()

def teport():
    clr(root)
    dets()
    bgn="#03256c"
    bgn2="#1768ac"

    btnft=Frame(root,width=300,height=700,bg='white')
    btnft.place(x=0,y=0)

    canvas = Canvas(btnft,width=300, height=700, bg='white')
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0,0, image=stnav, anchor=NW)
    
    welli=Label(btnft,image=tbg1,bg=bgn)
    welli.place(x=16,y=23)

    well=Label(btnft,text="  Welcome professor!",font=("",14,""),bg=bgn,fg="white")
    well.place(x=75,y=40)

    detbtnv=Button(btnft,text="Details",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white",command=dets)
    detbtnv.place(y=130,x=5)

    intmbtnv=Button(btnft,text="Student details",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    intmbtnv.place(y=180,x=5)

    extmbtnv=Button(btnft,text="Conduct exams",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    extmbtnv.place(y=230,x=5)

    quizbtnv=Button(btnft,text="Upload Assignment",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    quizbtnv.place(y=280,x=5)

    assbtnv=Button(btnft,text="Upload study material",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    assbtnv.place(y=330,x=5)

    stdybtnv=Button(btnft,text="Make a circular",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    stdybtnv.place(y=380,x=5)

    logoutbtnv=Button(btnft,text="Logout",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white",command=lambda:logoutask(2))
    logoutbtnv.place(y=430,x=5)

def adport():
    clr(root)
    dets()
    bgn="#03256c"
    bgn2="#1768ac"

    btnfs=Frame(root,width=300,height=700,bg='white')
    btnfs.place(x=0,y=0)

    canvas = Canvas(btnfs,width=300, height=700, bg='white')
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0,0, image=stnav, anchor=NW)
    
    welli=Label(btnfs,image=sbg1,bg=bgn)
    welli.place(x=16,y=23)

    well=Label(btnfs,text="Welcome Admin",font=("",14,""),bg=bgn,fg="white")
    well.place(x=75,y=40)

    detbtnv=Button(btnfs,text="Details",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white",command=dets)
    detbtnv.place(y=130,x=5)

    intmbtnv=Button(btnfs,text="Student details",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    intmbtnv.place(y=180,x=5)

    extmbtnv=Button(btnfs,text="Teacher details",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    extmbtnv.place(y=230,x=5)

    quizbtnv=Button(btnfs,text="Add a student",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    quizbtnv.place(y=280,x=5)

    assbtnv=Button(btnfs,text="Add a teacher",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    assbtnv.place(y=330,x=5)

    stdybtnv=Button(btnfs,text="Post a circular",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white")
    stdybtnv.place(y=380,x=5)

    logoutbtnv=Button(btnfs,text="Logout",font=("",14,""),bd=0,bg=bgn,width=26,activebackground=bgn2,fg='white',activeforeground="white",command=lambda:logoutask(3))
    logoutbtnv.place(y=430,x=5)

def stloginch():
    global stlog
    if sle.get()=='195001' and spe.get()=='':
        stlog=sle.get()
        messagebox.showinfo('Success','Login Successful')
        stport()

def teloginch():
    if tle.get()=='' and tpe.get()=='':
        messagebox.showinfo('Success','Login Successful')
        teport()

def adloginch():
    if ale.get()=='' and ape.get()=='':
        messagebox.showinfo('Success','Login Successful')
        adport()
    
def clr(todel):
   for i in todel.winfo_children():
      i.destroy()

def stlog():
    clr(root)
    global sle
    global spe
    canvas = Canvas(width=1200, height=700, bg='blue')
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0,0, image=lbgst, anchor=NW)
    
    sll=Label(root,text="Login",font=("",15,""),bg='white')
    sll.place(x=490,y=365)
    
    sle=Entry(root,width=35,bd=2,relief=GROOVE)
    sle.place(x=490,y=400)

    spl=Label(root,text="Password",font=("",15,""),bg='white')
    spl.place(x=490,y=425)

    spe=Entry(root,width=35,bd=2,show='*',relief=GROOVE)
    spe.place(x=490,y=460)

    fcs=Button(root,text="Forgot Password",bd=2,relief=GROOVE,bg='#287af6',fg='white')
    fcs.place(x=490,y=500)

    slg=Button(root,text="Login",width=10,bd=2,relief=GROOVE,bg='#287af6',fg='white',command=stloginch)
    slg.place(x=630,y=500)
    
    bbtn=Button(root,text='<-',width=5,bd=0,relief=GROOVE,bg='#287af6',fg='white',command=logpg)
    bbtn.place(x=670,y=250)


def telog():
    clr(root)
    global tle
    global tpe
    canvas = Canvas(width=1200, height=700, bg='blue')
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0,0, image=lbgte, anchor=NW)
    
    tll=Label(root,text="Login",font=("",15,""),bg='white')
    tll.place(x=490,y=365)
    
    tle=Entry(root,width=35,bd=2,relief=GROOVE)
    tle.place(x=490,y=400)

    tpl=Label(root,text="Password",font=("",15,""),bg='white')
    tpl.place(x=490,y=425)

    tpe=Entry(root,width=35,bd=2,show='*',relief=GROOVE)
    tpe.place(x=490,y=460)

    fct=Button(root,text="Forgot Password",bd=2,relief=GROOVE,bg='#287af6',fg='white')
    fct.place(x=490,y=500)

    tlg=Button(root,text="Login",width=10,bd=2,relief=GROOVE,bg='#287af6',fg='white',command=teloginch)
    tlg.place(x=630,y=500)

    bbtn=Button(root,text='<-',width=5,bd=0,relief=GROOVE,bg='#287af6',fg='white',command=logpg)
    bbtn.place(x=670,y=250)

def adlog():
    clr(root)
    global ale
    global ape
    canvas = Canvas(width=1200, height=700, bg='blue')
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0,0, image=lbgad, anchor=NW)
    
    all=Label(root,text="Login",font=("",15,""),bg='white')
    all.place(x=490,y=365)
    
    ale=Entry(root,width=35,bd=2,relief=GROOVE)
    ale.place(x=490,y=400)

    apl=Label(root,text="Password",font=("",15,""),bg='white')
    apl.place(x=490,y=425)

    ape=Entry(root,width=35,bd=2,show='*',relief=GROOVE)
    ape.place(x=490,y=460)

    fca=Button(root,text="Forgot Password",bd=2,relief=GROOVE,bg='#287af6',fg='white')
    fca.place(x=490,y=500)

    alg=Button(root,text="Login",width=10,bd=2,relief=GROOVE,bg='#287af6',fg='white',command=adloginch)
    alg.place(x=630,y=500)

    bbtn=Button(root,text='<-',width=5,bd=0,relief=GROOVE,bg='#287af6',fg='white',command=logpg)
    bbtn.place(x=670,y=250)

def logpg():
    #making bg images
    clr(root)
    
    canvas = Canvas(width=1200, height=700, bg='blue')
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0,0, image=lbg, anchor=NW)

    #buttons

    sbtn=Button(root,text='std',image=sbg,bd=0,bg='white',activebackground='white',command=stlog)
    sbtn.place(x=390,y=300)

    tbtn=Button(root,text='teach',image=tbg,bd=0,bg='white',activebackground='white',command=telog)
    tbtn.place(x=530,y=300)

    abtn=Button(root,text='admin',image=abg,bd=0,bg='white',activebackground='white',command=adlog)
    abtn.place(x=670,y=300)

# logpg()
stport()
# teport()
# adport()
# stdbdetail()

root.mainloop()