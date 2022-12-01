from tkinter import*
from tkinter import ttk
import pymongo
# import mysql.connector
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1500x800+0+0")

        # ==========================variable============================

        self.member_var=StringVar()
        self.enrollNo_var = StringVar()
        self.name_var = StringVar()
        self.address_var = StringVar()
        self.mobileNo_var = StringVar()
        self.bookID_var = StringVar()
        self.bookTitle_var = StringVar()
        self.author_var = StringVar()
        self.borrowDate_var = StringVar()
        self.dueDate_var = StringVar()
        self.lateReturnFine_var = StringVar()
        self.actualPrice_var = StringVar()

        # ==========================================================================================



        lbltitle=Label(self.root, text="Library Management System", bg="light goldenrod", fg="red", bd=20, relief=SUNKEN, font=("Ink Free", 50,"bold"),padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="LemonChiffon1")
        frame.place(x=0, y=130, width=1540, height=400)

        # ---------------------------DATA FRAME LEFT----------------------------

        DataFrameLeft=LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="light slate blue", bd=14, relief=RIDGE, font=("Calibri", 14, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        LableMember=Label(DataFrameLeft, text="Member Type", bg="powder blue", font=("Calibri", 14, "bold"), padx=2, pady=6)
        LableMember.grid(row=0, column=0, sticky=W)

        comMember=ttk.Combobox(DataFrameLeft, textvariable=self.member_var, font=("Calibri", 14, "bold"), width=27, state="readonly")
        comMember["value"] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)


        LablePRN_No=Label(DataFrameLeft, text="Enrollment No.", bg="powder blue", font=("Calibri", 14, "bold"), padx=2, pady=6)
        LablePRN_No.grid(row=1, column=0, sticky=W)


        txtPRN_No=Entry(DataFrameLeft, textvariable=self.enrollNo_var, font=("Calibri", 14, "bold"), width=29)
        txtPRN_No.grid(row=1, column=1)


        LableName = Label(DataFrameLeft, text="Name", bg="powder blue", font=("Calibri", 14, "bold"), padx=2, pady=6)
        LableName.grid(row=2, column=0, sticky=W)

        txtName = Entry(DataFrameLeft, textvariable=self.name_var, font=("Calibri", 14, "bold"), width=29)
        txtName.grid(row=2, column=1)


        LableAddress = Label(DataFrameLeft, text="Adderss", bg="powder blue", font=("Calibri", 14, "bold"), padx=2, pady=6)
        LableAddress.grid(row=3, column=0, sticky=W)
        txtAddress = Entry(DataFrameLeft, textvariable=self.address_var, font=("Calibri", 14, "bold"), width=29)
        txtAddress.grid(row=3, column=1)

        LableMobile = Label(DataFrameLeft, text="Mobile No.", bg="powder blue", font=("Calibri", 14, "bold"), padx=2, pady=6)
        LableMobile.grid(row=4, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, textvariable=self.mobileNo_var, font=("Calibri", 14, "bold"), width=29)
        txtMobile.grid(row=4, column=1)

        LableBookId = Label(DataFrameLeft, text="Book ID", bg="powder blue", font=("Calibri", 14, "bold"), padx=2,
                             pady=6)
        LableBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, textvariable=self.bookID_var, font=("Calibri", 14, "bold"), width=29)
        txtBookId.grid(row=0, column=3)

        LableBookTitle = Label(DataFrameLeft, text="Book Title", bg="powder blue", font=("Calibri", 14, "bold"), padx=2,
                            pady=6)
        LableBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitlt = Entry(DataFrameLeft, textvariable=self.bookTitle_var, font=("Calibri", 14, "bold"), width=29)
        txtBookTitlt.grid(row=1, column=3)

        LableAuthor = Label(DataFrameLeft, text="Author", bg="powder blue", font=("Calibri", 14, "bold"), padx=2,
                            pady=6)
        LableAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, textvariable=self.author_var, font=("Calibri", 14, "bold"), width=29)
        txtAuthor.grid(row=2, column=3)


        LableBorrow = Label(DataFrameLeft, text="Borrow Date", bg="powder blue", font=("Calibri", 14, "bold"), padx=2,
                            pady=6)
        LableBorrow.grid(row=3, column=2, sticky=W)
        txtBorrow = Entry(DataFrameLeft, textvariable=self.borrowDate_var, font=("Calibri", 14, "bold"), width=29)
        txtBorrow.grid(row=3, column=3)


        LableDue = Label(DataFrameLeft, text="Due Date", bg="powder blue", font=("Calibri", 14, "bold"), padx=2,
                            pady=6)
        LableDue.grid(row=4, column=2, sticky=W)
        txtDue = Entry(DataFrameLeft, textvariable=self.dueDate_var, font=("Calibri", 14, "bold"), width=29)
        txtDue.grid(row=4, column=3)

        LableFine = Label(DataFrameLeft, text="Late Return Fine", bg="powder blue", font=("Calibri", 14, "bold"), padx=2
                          , pady=6)
        LableFine.grid(row=5, column=2, sticky=W)
        txtFine = Entry(DataFrameLeft, textvariable=self.lateReturnFine_var, font=("Calibri", 14, "bold"), width=29)
        txtFine.grid(row=5, column=3)


        LablePrice = Label(DataFrameLeft, text="Actual Price", bg="powder blue", font=("Calibri", 15, "bold"), padx=2,
                            pady=6)
        LablePrice.grid(row=6, column=2, sticky=W)
        txtPrice = Entry(DataFrameLeft, textvariable=self.actualPrice_var, font=("Calibri", 15, "bold"), width=29)
        txtPrice.grid(row=6, column=3)




        # ------------------------------DATA FRAME RIGHT-------------------------------



        DataFrameRight=LabelFrame(frame, text="Book Details", padx=18, bg="powder blue", fg="light slate blue", bd=12, relief=RIDGE, font=("Calibri", 14, "bold"))
        DataFrameRight.place(x=910, y=5, width=570, height=350)

        self.txtBox=Text(DataFrameRight, font=("Calibri", 14, "bold"), width=32, height=13, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollBar=Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0, column=1, sticky="ns")

        # listScrollBarTop = Scrollbar(DataFrameRight)
        # listScrollBarTop.grid(row=1, column=0, sticky="ew")

        list_of_Books = ['A Commentary on the UNIX Operating System', 'Accelerate',
                         'Advanced Programming in the Unix Environment',
                         'Algorithms + Data Structures = Programs', 'Let Us C', 'The Art of Computer Programming',
                         'The Art of Unix Programming', 'The AWK Programming Language', 'C++ Primer',
                         ' Effective Modern C++', 'Practical C++ Programming', 'Think Python',
                         'Learn Python 3 the Hard Way', 'Fluent Python', 'Effective Python', 'Python Cookbook',
                         ' Head First Statistics', 'Introduction to Probability', 'Python for data analysis',
                         'The Book of Common Law', 'Carnivorous Gardening', 'The Book of Twelve Seasons',
                         'A Journey Beyond the Veil', 'Raising Weasels With Confidence',
                         'What Lights Shine Forever? A History of Sun Deities', 'A Short History of Dwarves',
                         'What Color Is Your Dragon?', 'Samwell’s Guide to Arms and Armor',
                         'The Silent Bard and Other Myths', 'The Letters of Saint Cuthbert',
                         'Secret Doors and Passages (bad poetry collection)', 'A Journeyman’s Guide to Barrel Making',
                         'The Great Bird Hoax'
                         ]

        listBox=Listbox(DataFrameRight, font=("Calibri", 14, "bold"), width=17, height=13)
        listBox.grid(row=0, column=0, padx=4)
        listScrollBar.config(command=listBox.yview)

        for item in list_of_Books:
            listBox.insert(END, item)


#         ----------------------------BUTTON FRAMES--------------------------------

        framebutton=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framebutton.place(x=0, y=530, width=1540, height=90)

        btnAddData0 = Button(framebutton, command=self.add_data, text="Add Data", font=("Calibri", 14, "bold"), width=23, height=2, bg="#9090EE",
                             fg="white")
        btnAddData0.grid(row=0, column=0, padx=30)

        btnAddData1 = Button(framebutton, text="Show Data", font=("Calibri", 14, "bold"), width=23, height=2, bg="#9090EE",
                             fg="white")
        btnAddData1.grid(row=0, column=1, ipadx=10)

        btnAddData2 = Button(framebutton, text="Update Data", font=("Calibri", 14, "bold"), width=23, height=2,
                             bg="#9090EE", fg="white")
        btnAddData2.grid(row=0, column=2, padx=30)

        btnAddData3 = Button(framebutton, text="Delete", font=("Calibri", 14, "bold"), width=23, height=2, bg="#9090EE",
                             fg="white")
        btnAddData3.grid(row=0, column=3)

        btnAddData4 = Button(framebutton, text="Exit", font=("Calibri", 14, "bold"), width=23, height=2, bg="red", fg="white")
        btnAddData4.grid(row=0, column=4, padx=30)


#         ---------------------------INFORMATION FRAME-----------------------------

        framedetails=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framedetails.place(x=0, y=610, width=1540, height=195)

        # Table_Frame=Frame(framedetails, bd=6, relief=RIDGE, bg="powder blue")
        # Table_Frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(framedetails, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(framedetails, orient=VERTICAL)


        self.library_table=ttk.Treeview(framedetails, columns=("membertype", "enrollmentNo", "Name", "Address",
                                                               "MobileNo", "BookID", "BookTitle", "author",
                                                               "BorrowDate", "DueDate", "LateReturnFine",
                                                               "ActualPrice"),
                                        xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("enrollmentNo", text="Enrollment No.")
        self.library_table.heading("Name", text="Name")
        self.library_table.heading("Address", text="Address")
        self.library_table.heading("MobileNo", text="Mobile No")
        self.library_table.heading("BookID", text="Book ID")
        self.library_table.heading("BookTitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("BorrowDate", text="Borrow Date")
        self.library_table.heading("DueDate", text="Due Date")
        self.library_table.heading("LateReturnFine", text="Late Return Fine")
        self.library_table.heading("ActualPrice", text="Actual Price")


        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("enrollmentNo", width=100)
        self.library_table.column("Name", width=100)
        self.library_table.column("Address", width=100)
        self.library_table.column("MobileNo", width=100)
        self.library_table.column("BookID", width=100)
        self.library_table.column("BookTitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("BorrowDate", width=100)
        self.library_table.column("DueDate", width=100)
        self.library_table.column("LateReturnFine", width=100)
        self.library_table.column("ActualPrice", width=100)



    def add_data(self):
        conn=pymongo.connector.connect(host="localhost", username="root", password="12345678", database="library_data")
        # client = MongoClient(host="localhost", port=27017)
        my_cursor=conn.cursor()
        my_cursor.execute("insert into details values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
            self.member_var.get(),
            self.enrollNo_var.get(),
            self.name_var.get(),
            self.address_var.get(),
            self.mobileNo_var.get(),
            self.bookID_var.get(),
            self.bookTitle_var.get(),
            self.author_var.get(),
            self.borrowDate_var.get(),
            self.dueDate_var.get(),
            self.lateReturnFine_var.get(),
            self.actualPrice_var.get()
        ))


        conn.commit()
        conn.close()

        messagebox.showinfo("success", "Member has been added successfully")





if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
