from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter 
import datetime



class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x150")
        self.root.configure(bg="#3498db")  # Background color

        self.lblUsername = Label(self.root, text="Username:", bg="#3498db", fg="#2c3e50")  # Background and foreground colors
        self.lblUsername.pack()
        self.entUsername = Entry(self.root)
        self.entUsername.pack()

        self.lblPassword = Label(self.root, text="Password:", bg="#3498db", fg="#2c3e50")  # Background and foreground colors
        self.lblPassword.pack()
        self.entPassword = Entry(self.root, show="*")
        self.entPassword.pack()

        self.btnLogin = Button(self.root, text="Login", command=self.login, bg="#3498db", fg="#2c3e50")  # Background and foreground colors
        self.btnLogin.pack()

    def login(self):
        # Check if username and password match predefined values
        username = self.entUsername.get()
        password = self.entPassword.get()

        if username == "admin" and password == "admin":  # Change to your actual username and password
            self.root.destroy()  # Close the login window
            self.open_main_application()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_main_application(self):
        root = Tk()
        obj = LibraryManagementSystem(root)
        root.mainloop()


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("LibraryManagementSystem")
        self.root.geometry("1550x800+0+0")
    #=======================variable===================

        self.MemberType_var=StringVar()
        self.PRNNo_var=StringVar()
        self.IDNo_var=StringVar()
        self.FirstName_var=StringVar()
        self.LastName_var=StringVar()
        self.Address1_var=StringVar()
        self.Address2_var=StringVar()
        self.PostId_var=StringVar()
        self.Mobile_var=StringVar()
        self.BookId_var=StringVar()
        self.BookTitle_var=StringVar()
        self.Author_var=StringVar()
        self.DateBorrowed_var=StringVar()
        self.DueDate_var=StringVar()
        self.DaysOfBook_var=StringVar()
        self.LaterReturnFine_var=StringVar()
        self.DateOverDue_var=StringVar()
        self.ActualPrice_var=StringVar()




        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="#3498db", fg="#2c3e50", bd=14, relief=RIDGE, font=("new times roman", 40, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)



        frame=Frame(self.root,bd=12, relief=RIDGE,padx=20,bg="#3498db")
        frame.place(x=0,y=100,width=1360,height=400)
        #================Data Frame Rate====================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information", bg="#3498db", fg="#2c3e50", bd=12, relief=RIDGE, font=("new times roman", 12, "bold"))
        DataFrameLeft.place(x=-8,y=5,width=820,height=360)

        lblMember=Label(DataFrameLeft,font=("new times roman", 12, "bold"),text="Member Type",padx=2,pady=6,bg="#3498db")
        lblMember.grid(row=0,column=0,sticky=W)


        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.MemberType_var,state="readonly",
                                                        font=("new times roman", 12, "bold"),width=27)
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)



         

        lblPRN_No=Label(DataFrameLeft,bg="#3498db",text="PRN_No",font=("new times roman", 12, "bold"),padx=2)
        lblPRN_No.grid(row=1,column=0,sticky=W)

        textPRN_No=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.PRNNo_var,width=29)
        textPRN_No.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="#3498db",text="ID No",font=("new times roman", 12, "bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)

        textTitle=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.IDNo_var,width=29)
        textTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="#3498db",text="First Name",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)

        textFirstName=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.FirstName_var,width=29)
        textFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="#3498db",text="Last Name",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)

        textLastName=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.LastName_var,width=29)
        textLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="#3498db",text="Address1",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)

        textAddress1=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.Address1_var,width=29)
        textAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="#3498db",text="Address2",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)

        textAddress2=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.Address2_var,width=29)
        textAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="#3498db",text="Post Id",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)

        textPostcode=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.PostId_var,width=29)
        textPostcode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="#3498db",text="Mobile",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)

        textMobile=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.Mobile_var,width=29)
        textMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="#3498db",text="Book Id",font=("new times roman", 12, "bold"),padx=2)
        lblBookId.grid(row=0,column=2,sticky=W)

        textBookId=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.BookId_var,width=29)
        textBookId.grid(row=0,column=3)

        
        lblBookTitle=Label(DataFrameLeft,bg="#3498db",text="Book Title",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)

        textBookTitle=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.BookTitle_var,width=29)
        textBookTitle.grid(row=1,column=3)


        lblAuthor=Label(DataFrameLeft,bg="#3498db",text="Author",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)

        textAuthor=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.Author_var,width=29)
        textAuthor.grid(row=2,column=3)

        lblDataBorrowed=Label(DataFrameLeft,bg="#3498db",text="Data Borrowed",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblDataBorrowed.grid(row=3,column=2,sticky=W)

        textDataBorrowed=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.DateBorrowed_var,width=29)
        textDataBorrowed.grid(row=3,column=3)


        lblDataDue=Label(DataFrameLeft,bg="#3498db",text="Due Date",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblDataDue.grid(row=4,column=2,sticky=W)

        textDataDue=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.DueDate_var,width=29)
        textDataDue.grid(row=4,column=3)

        lblDaysOfBook=Label(DataFrameLeft,bg="#3498db",text="Days of Book",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblDaysOfBook.grid(row=5,column=2,sticky=W)

        textDaysofBook=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.DaysOfBook_var,width=29)
        textDaysofBook.grid(row=5,column=3)

        lblLastReturnFine=Label(DataFrameLeft,bg="#3498db",text="Later Return Fine",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblLastReturnFine.grid(row=6,column=2,sticky=W)

        textLastReturnFine=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.LaterReturnFine_var,width=29)
        textLastReturnFine.grid(row=6,column=3)

        
        lblDataOverDue=Label(DataFrameLeft,bg="#3498db",text="Data Over Due",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblDataOverDue.grid(row=7,column=2,sticky=W)

        textDataOverDue=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.DateOverDue_var,width=29)
        textDataOverDue.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="#3498db",text="Actual Price",font=("new times roman", 12, "bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)

        textActualPrice=Entry(DataFrameLeft,font=("new times roman", 13, "bold"),textvariable=self.ActualPrice_var,width=29)
        textActualPrice.grid(row=8,column=3)






         #===================DataFrame Right==================
        
        DataFrameRight=LabelFrame(frame,text="Book Details", bg="#3498db", 
                                   bd=12, relief=RIDGE, font=("new times roman", 12, "bold"))
        DataFrameRight.place(x=820,y=5,width=480,height=360)

        self.txtBox=Text(DataFrameRight,font=("new times roman", 12, "bold"),width=29,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=3)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listbooks = ['Programming Languages Books', 'C# and C++ Books', 'Java Books', 'Javascript Books',
                     'Matlab Books', 'Objetive-C Books', 'PHP Books', 'Python Books', 'R Books', 'Swift Books',
                     'Agile Methodologies Books', 'Algorithms Books', 'Artificial Intelligence Books', 'Automation Books',
                     'Big Data Books', 'Blockchain Books', 'Books about Computing', 'Books about ICT',
                     'Cloud Computing Books', 'Computer Networks Books', 'Computer Security Books', 'Cryptography Books',
                     'Database Books', 'E-Commerce Books', 'Excel Books']
        
        def SelectBook(event=""):
            value = str(listbox.get(listbox.curselection()))
            x=value
            if x=="Programming Languages Books":
                self.BookId_var.set("BKID001")
                self.BookTitle_var.set("Programming Languages Books")
                self.Author_var.set("Patel Aatif")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.534")

            elif x=="C# and C++ Books":
                self.BookId_var.set("BKID002")
                self.BookTitle_var.set("C# and C++ Books")
                self.Author_var.set("yasmin Khan")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.500")

            elif x=="Java Books":
                self.BookId_var.set("BKID003")
                self.BookTitle_var.set("Java Books")
                self.Author_var.set("R. K. Narayan")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.734")

            elif x=="Javascript Books":
                self.BookId_var.set("BKID004")
                self.BookTitle_var.set("Javascript Books")
                self.Author_var.set("Tarn Adams")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.574")

            elif x=="Matlab Books":
                self.BookId_var.set("BKID005")
                self.BookTitle_var.set("Matlab Books")
                self.Author_var.set("Paul Allen")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.349")

            elif x=="Objetive-C Books":
                self.BookId_var.set("BKID006")
                self.BookTitle_var.set("Objetive-C Books")
                self.Author_var.set("Bill Atiken")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.645")


            elif x=="PHP Books":
                self.BookId_var.set("BKID007")
                self.BookTitle_var.set("PHP Books")
                self.Author_var.set("John Backus")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.409")
            
            elif x=="Python Books":
                self.BookId_var.set("BKID008")
                self.BookTitle_var.set("Python Books")
                self.Author_var.set("Atiken John")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.435")

            elif x=="R Books":
                self.BookId_var.set("BKID009")
                self.BookTitle_var.set("R Books")
                self.Author_var.set("cark john")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.458")

            elif x=="Swift Books":
                self.BookId_var.set("BKID0010")
                self.BookTitle_var.set("Swift Books")
                self.Author_var.set("cark john")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.458")

            elif x=="Agile Methodologies Books":
                self.BookId_var.set("BKID0011")
                self.BookTitle_var.set("Agile Methodologies Books")
                self.Author_var.set("Mark black")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.654")

            elif x=="Algorithms Books":
                self.BookId_var.set("BKID0012")
                self.BookTitle_var.set("Algorithms Books")
                self.Author_var.set("Lars bak")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.435")


            elif x=="Artificial Intelligence Books":
                self.BookId_var.set("BKID0013")
                self.BookTitle_var.set("Artificial Intelligence Books")
                self.Author_var.set("carl backhouse")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.438")


            elif x=="Automation Books":
                self.BookId_var.set("BKID0014")
                self.BookTitle_var.set("Automation Books")
                self.Author_var.set("Richerd goad")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.358")

            elif x=="Big Data Books":
                self.BookId_var.set("BKID0015")
                self.BookTitle_var.set("Big Data Books")
                self.Author_var.set("kent bak")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.899")

            elif x=="Blockchain Books":
                self.BookId_var.set("BKID0016")
                self.BookTitle_var.set("Blockchain Books")
                self.Author_var.set("Doung bel")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.358")
            
            elif x=="Books about Computing":
                self.BookId_var.set("BKID0017")
                self.BookTitle_var.set("Books about Computing")
                self.Author_var.set("Doung bel")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.478")

            elif x=="Books about ICT":
                self.BookId_var.set("BKID0018")
                self.BookTitle_var.set("Books about ICT")
                self.Author_var.set("Kim hang")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.675")

            elif x=="Cloud Computing Books":
                self.BookId_var.set("BKID0019")
                self.BookTitle_var.set("Cloud Computing Books")
                self.Author_var.set("hang fang")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.655")
                

            elif x=="Computer Networks Books":
                self.BookId_var.set("BKID0020")
                self.BookTitle_var.set("Computer Networks Books")
                self.Author_var.set("han Tim ")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.255")





            elif x=="Computer Security Books":
                self.BookId_var.set("BKID0021")
                self.BookTitle_var.set("Computer Security Books")
                self.Author_var.set("Kim hang")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.980")


            elif x=="Cryptography Books":
                self.BookId_var.set("BKID0022")
                self.BookTitle_var.set("Cryptography Books")
                self.Author_var.set("Kim hang")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.665")

            elif x=="Database Books":
                self.BookId_var.set("BKID0023")
                self.BookTitle_var.set("Database Books")
                self.Author_var.set("Tim burner")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.312")

            elif x=="E-Commerce Books":
                self.BookId_var.set("BKID0024")
                self.BookTitle_var.set("E-Commerce Books")
                self.Author_var.set("ganf dog")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.312")

            elif x=="Excel Books":
                self.BookId_var.set("BKID0025")
                self.BookTitle_var.set("Excel Books")
                self.Author_var.set("Muskan Patel")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=7)
                d3=d1+d2
                self.DateBorrowed_var.set(d1)
                self.DueDate_var.set(d3)
                self.DaysOfBook_var.set(7)
                self.LaterReturnFine_var.set("Rs.5")
                self.DateOverDue_var.set("No")
                self.ActualPrice_var.set("Rs.980")








        listbox=Listbox(DataFrameRight,font=("new times roman", 12, "bold"),width=17,height=16)
        listbox.bind("<<ListboxSelect>>", SelectBook)
        listbox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listbox.yview)


        for item in listbooks:
            listbox.insert(END, item)


         #===================Button Frame==================
        framebutton=Frame(self.root,bd=12, relief=RIDGE,padx=20,bg="#3498db")
        framebutton.place(x=0,y=500,width=1366,height=70)

        btnAddData=Button(framebutton,command=self.add_data,text="ADD DATA",font=("new times roman", 12, "bold"),width=21,bg="BLACK",fg="WHITE")
        btnAddData.grid(row=0,column=0)
        btnAddData=Button(framebutton,command=self.showData,text="SHOW DATA",font=("new times roman", 12, "bold"),width=21,bg="BLACK",fg="WHITE")
        btnAddData.grid(row=0,column=1)
        btnAddData=Button(framebutton,command=self.update,text="UPDATE",font=("new times roman", 12, "bold"),width=21,bg="BLACK",fg="WHITE")
        btnAddData.grid(row=0,column=2)
        btnAddData=Button(framebutton,command=self.delete,text="DELETE",font=("new times roman", 12, "bold"),width=21,bg="BLACK",fg="WHITE")
        btnAddData.grid(row=0,column=3)
        btnAddData=Button(framebutton,command=self.reset,text="RESET",font=("new times roman", 12, "bold"),width=21,bg="BLACK",fg="WHITE")
        btnAddData.grid(row=0,column=4)
        btnAddData=Button(framebutton,command=self.iExit,text="EXIT",font=("new times roman", 12, "bold"),width=20,bg="BLACK",fg="WHITE")
        btnAddData.grid(row=0,column=5)

         #===================Information Frame==================
        framedetails=Frame(self.root,bd=12, relief=RIDGE,padx=20,bg="#3498db")
        framedetails.place(x=0,y=570,width=1366,height=175)

        table_frame=Frame(self.root,bd=6, relief=RIDGE,bg="#3498db")
        table_frame.place(x=20,y=590,width=1320,height=137)


        xscroll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.library_table = ttk.Treeview(table_frame, columns=("MemberType", "PRNNo", "IDNo", "FirstName", "LastName", "Address1", "Address2",
                                                       "PostId", "Mobile", "BookId", "BookTitle", "Author", "DateBorrowed", "DueDate",
                                                       "Days", "LaterReturnFine", "DateOverDue", "ActualPrice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)


        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("MemberType", text="Member Type")
        self.library_table.heading("PRNNo",text="PRN No.")
        self.library_table.heading("IDNo",text="ID No.")
        self.library_table.heading("FirstName",text="First Name")
        self.library_table.heading("LastName",text="Last Name")
        self.library_table.heading("Address1",text="Address 1")
        self.library_table.heading("Address2",text="Address 2")
        self.library_table.heading("PostId",text="Post Id")
        self.library_table.heading("Mobile",text="Mobile")
        self.library_table.heading("BookId", text="Book ID")
        self.library_table.heading("BookTitle", text="Book Title")
        self.library_table.heading("Author",text="Author")
        self.library_table.heading("DateBorrowed",text="Date Borrowed")
        self.library_table.heading("DueDate",text="Due Date")
        self.library_table.heading("Days",text="Days")
        self.library_table.heading("LaterReturnFine", text="Later Return Fine")
        self.library_table.heading("DateOverDue",text="Date Over Due")
        self.library_table.heading("ActualPrice",text="Actual Price")

        

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("MemberType",width=100)
        self.library_table.column("PRNNo",width=100)
        self.library_table.column("IDNo",width=100)
        self.library_table.column("FirstName",width=100)
        self.library_table.column("LastName",width=100)
        self.library_table.column("Address1",width=100)
        self.library_table.column("Address2",width=100)
        self.library_table.column("PostId",width=100)
        self.library_table.column("Mobile",width=100)
        self.library_table.column("BookId",width=100)
        self.library_table.column("BookTitle",width=100)
        self.library_table.column("Author",width=100)
        self.library_table.column("DateBorrowed",width=100)
        self.library_table.column("DueDate",width=100)
        self.library_table.column("Days",width=100)
        self.library_table.column("LaterReturnFine",width=100)
        self.library_table.column("DateOverDue",width=100)
        self.library_table.column("ActualPrice",width=100)
        
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)



    def add_data(self):
       
        conn = mysql.connector.connect(host="localhost", port=3306, username="root", password="Myfirstproject@123", database="librarydata")

        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
 
                                                                                                                self.MemberType_var.get(),
                                                                                                                self.PRNNo_var.get(),
                                                                                                                self.IDNo_var.get(),
                                                                                                                self.FirstName_var.get(),
                                                                                                                self.LastName_var.get(),
                                                                                                                self.Address1_var.get(),
                                                                                                                self.Address2_var.get(),
                                                                                                                self.PostId_var.get(),
                                                                                                                self.Mobile_var.get(),
                                                                                                                self.BookId_var.get(),
                                                                                                                self.BookTitle_var.get(),
                                                                                                                self.Author_var.get(),
                                                                                                                self.DateBorrowed_var.get(),
                                                                                                                self.DueDate_var.get(),
                                                                                                                self.DaysOfBook_var.get(),
                                                                                                                self.LaterReturnFine_var.get(),
                                                                                                                self.DateOverDue_var.get(),
                                                                                                                self.ActualPrice_var.get(),
            ))
        conn.commit()
        self.fetch_data()
        conn.close() 


        messagebox.showinfo("Success","Member Has Been Inserted Sucessfully")

    def update(self):
       
        conn = mysql.connector.connect(host="localhost", port=3306, username="root", password="Myfirstproject@123", database="librarydata")

        my_cursor=conn.cursor()
        my_cursor.execute("UPDATE library SET Membertype=%s, IDNo=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, PostId=%s, Mobile=%s, BookId=%s, BookTitle=%s, Author=%s, DateBorrowed=%s, DueDate=%s, DaysOfBook=%s, LaterReturnFine=%s, DateOverDue=%s, ActualPrice=%s WHERE PRNNo=%s", (
            self.MemberType_var.get(),
            self.IDNo_var.get(),
            self.FirstName_var.get(),
            self.LastName_var.get(),
            self.Address1_var.get(),
            self.Address2_var.get(),
            self.PostId_var.get(),
            self.Mobile_var.get(),
            self.BookId_var.get(),
            self.BookTitle_var.get(),
            self.Author_var.get(),
            self.DateBorrowed_var.get(),
            self.DueDate_var.get(),
            self.DaysOfBook_var.get(),
            self.LaterReturnFine_var.get(),
            self.DateOverDue_var.get(),
            self.ActualPrice_var.get(),
            self.PRNNo_var.get(),
                ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close() 


        messagebox.showinfo("Success","Member Has Been Updated Sucessfully")

     





    

    def  fetch_data(self):
        conn = mysql.connector.connect(host="localhost", port=3306, username="root", password="Myfirstproject@123", database="librarydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select *  from library ")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()
           
    def get_cursor(self,event=""):
        cursor_rows=self.library_table.focus()
        content=self.library_table.item(cursor_rows)
        row=content['values']
        self.MemberType_var.set(row[0])
        self.PRNNo_var.set(row[1])
        self.IDNo_var.set(row[2])
        self.FirstName_var.set(row[3])
        self.LastName_var.set(row[4])
        self.Address1_var.set(row[5])
        self.Address2_var.set(row[6])
        self.PostId_var.set(row[7])
        self.Mobile_var.set(row[8])
        self.BookId_var.set(row[9])
        self.BookTitle_var.set(row[10])
        self.Author_var.set(row[11])
        self.DateBorrowed_var.set(row[12])
        self.DueDate_var.set(row[13])
        self.DaysOfBook_var.set(row[14])
        self.LaterReturnFine_var.set(row[15])
        self.DateOverDue_var.set(row[16])
        self.ActualPrice_var.set(row[17])
    
    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.MemberType_var.get()+"\n")
        self.txtBox.insert(END,"ID No:\t\t"+ self.IDNo_var.get()+"\n")
        self.txtBox.insert(END,"PRN No:\t\t"+ self.PRNNo_var.get()+"\n")
        self.txtBox.insert(END,"First Name:\t\t"+ self.FirstName_var.get()+"\n")
        self.txtBox.insert(END,"Last Name:\t\t"+ self.LastName_var.get()+"\n")
        self.txtBox.insert(END,"Address 1:\t\t"+ self.Address1_var.get()+"\n")
        self.txtBox.insert(END,"Address 2:\t\t"+ self.Address2_var.get()+"\n")
        self.txtBox.insert(END,"PostId:\t\t"+ self.PostId_var.get()+"\n")
        self.txtBox.insert(END,"Mobile:\t\t"+ self.Mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book Id:\t\t"+ self.BookId_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.BookTitle_var.get()+"\n")
        self.txtBox.insert(END,"Author:\t\t"+ self.Author_var.get()+"\n")
        self.txtBox.insert(END,"Date Borrowed:\t\t"+ self.DateBorrowed_var.get()+"\n")
        self.txtBox.insert(END,"Due Date:\t\t"+ self.DueDate_var.get()+"\n")
        self.txtBox.insert(END,"Days Of Book\t\t"+ self.DaysOfBook_var.get()+"\n")
        self.txtBox.insert(END,"Later Return Fine:\t\t"+ self.LaterReturnFine_var.get()+"\n")
        self.txtBox.insert(END,"Date Over Due:\t\t"+ self.DateOverDue_var.get()+"\n")
        self.txtBox.insert(END,"Actual Price:\t\t"+ self.ActualPrice_var.get()+"\n")

    def reset(self):
        self.MemberType_var.set(""),
        self.IDNo_var.set(""),
        self.PRNNo_var.set(""),
        self.FirstName_var.set(""),
        self.LastName_var.set(""),
        self.Address1_var.set(""),
        self.Address2_var.set(""),
        self.PostId_var.set(""),
        self.Mobile_var.set(""),
        self.BookId_var.set(""),
        self.BookTitle_var.set(""),
        self.Author_var.set(""),
        self.DateBorrowed_var.set(""),
        self.DueDate_var.set(""),
        self.DaysOfBook_var.set(""),
        self.LaterReturnFine_var.set(""),
        self.DateOverDue_var.set(""),
        self.ActualPrice_var.set(""),
        self.txtBox.delete("1.0",END)
  
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library management system", "Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
        

    def delete(self):
        if self.PRNNo_var.get()=="" or self.IDNo_var.get()=="":
            messagebox.showerror("Error","First Select The Member")
        else:
            conn = mysql.connector.connect(host="localhost", port=3306, username="root", password="Myfirstproject@123", database="librarydata")
            my_cursor=conn.cursor()
            query="delete from library where PRNNo=%s"
            value=(self.PRNNo_var.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close() 


            messagebox.showinfo("Success","Member Has Been Deleted Sucessfully")


    












if __name__ == "__main__":
    login_root = Tk()
    login = LoginWindow(login_root)
    login_root.mainloop()
