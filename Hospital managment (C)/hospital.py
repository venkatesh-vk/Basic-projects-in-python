from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Managment System")
        self.root.geometry("1540x800+0+0")

        lbtitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGMENT SYSTEM",fg='red',bg='white',font=("times new roman",50,"bold"))
        lbtitle.pack(side=TOP,fill=X)

        #dataframes
        dataframe=Frame(self.root,bd=20,relief=RIDGE)
        dataframe.place(x=0,y=130,width=1530,height=400)

        dataframel=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",15,"bold"),text="Patient Information")
        dataframel.place(x=0,y=5,width=980,height=350)

        dataframer=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",15,"bold"),text="Prescription")
        dataframer.place(x=990,y=5,width=460,height=350)

        #buttonframe
        buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        buttonframe.place(x=0,y=530,width=1530,height=70)

        #detailsframe
        detailframe=Frame(self.root,bd=20,relief=RIDGE)
        detailframe.place(x=0,y=600,width=1530,height=190)

        #dataframel
        lblnametablet=Label(dataframel,text='Names of Tablets',padx=2,pady=6,font=("times new roman",15,"bold"))
        lblnametablet.grid(row=0,column=0)

        comnametablet=ttk.Combobox(dataframel,width=33,font=("times new roman",15,"bold"))
        comnametablet['values']=('Abacavir','Ativan','Azithromycin','Adderall','Azithromycin')
        comnametablet.grid(row=0,column=1,padx=5)
        



        
root=Tk()
ob=Hospital(root)
root.mainloop()
