'''

                                        Author: Parthik Bhardwaj
                                        Roll no.: 16CSU243
                                        Topic: Faculty Database

'''

# module for GUI
from tkinter import *
from tkinter import messagebox

#             ***** Function to add records *****
def add():
    w = h = 500          # size of window
    root = Toplevel(main_window)
    root.geometry("%dx%d+0+0" % (w, h))     # sets window size
    root["bg"] = "black"            # sets background color of window
    details = []        # list to put details

    def AddToFile():

        # check for invalid input
        try:
            eval(salary.get())
            if (name.get() == ""):
                raise ValueError('Invalid Input')
            if (department.get() == ""):
                raise ValueError('Invalid Input')
            if (designation.get() == ""):
                raise ValueError('Invalid Input')
            if (status.get() == ""):
                raise ValueError('Invalid Input')
        except:
            messagebox._show("Invalid Input", "Please enter valid inputs. Closing this window.")
            root.destroy()

        # adding details to list
        details.append(name.get() + "\n")
        details.append(department.get() + "\n")
        details.append(designation.get() + "\n")
        details.append(status.get() + "\n")
        details.append(str(eval(salary.get())) + "\n")

        with open('db.txt', 'a') as output:     # opens file in append mode
            output.writelines(details)      # print list to  file
        messagebox.showinfo("Successful!", "New Record is added successfully!")     # operation done successfully message
        root.destroy()

    # defining label, message and entry(to get user input)
    enterDetail_message = Message(root,
                                  text="\nEnter your details: ",
                                  fg="#006699",
                                  bg="#000000",
                                  padx=3,
                                  pady=3,
                                  anchor=N,
                                  font=('Arial', 20, "bold"),
                                  width=w).pack()

    name_label = Label(root,
                       text="Name:",
                       font=('Arial', 15),
                       fg="#0099ff",
                       bg="#000000").place(x=100, y=130)
    name = Entry(root,
                 bd=5,
                 fg="#00ffff",
                 bg="#000000")

    department_label = Label(root,
                             text="Department:",
                             font=('Arial', 15),
                             fg="#0099ff",
                             bg="#000000").place(x=100, y=165)
    department = Entry(root,
                       bd=5,
                       fg="#00ffff",
                       bg="#000000")

    designation_label = Label(root,
                              text="Designation:",
                              font=('Arial', 15),
                              fg="#0099ff",
                              bg="#000000").place(x=100, y=200)

    designation = Entry(root,
                        bd=5,
                        fg="#00ffff",
                        bg="#000000")

    status_label = Label(root,
                         text="Status:",
                         font=('Arial', 15),
                         fg="#0099ff",
                         bg="#000000").place(x=100, y=235)

    status = Entry(root,
                   bd=5,
                   fg="#00ffff",
                   bg="#000000")

    salary_label = Label(root,
                         text="Salary:",
                         font=('Arial', 15),
                         fg="#0099ff",
                         bg="#000000").place(x=100, y=270)

    salary = Entry(root,
                   bd=5,
                   fg="#00ffff",
                   bg="#000000")

    submit_button = Button(root,
                           text="SUBMIT",
                           fg="#99ccff",
                           padx=5,
                           pady=4,
                           bg="#000000",
                           command=AddToFile,
                           font=('Georgia', 15)).place(x=350, y=400)

    # placing entry declared above
    name.place(x=220, y=130)
    department.place(x=220, y=165)
    designation.place(x=220, y=200)
    status.place(x=220, y=235)
    salary.place(x=220, y=270)

    root.mainloop()



#             ***** Function to delete records *****
def delete():
    def Del_record():

        count = 0
        newlist = []

        # error checking if file isn't present
        try:
            with open("db.txt", "r") as input:
                recordList = input.readlines()
        except:
            messagebox._show("Error", "An error occured. Check if file is present or not.")
            root.destroy()
            return

        if (var.get() == 1):
            iterator = 0
            while count < (len(recordList) / 5):
                if (recordList[iterator] == (name.get() + "\n")):
                    print(recordList[iterator] == name.get())
                else:
                    newlist.append(recordList[iterator])
                    newlist.append(recordList[iterator + 1])
                    newlist.append(recordList[iterator + 2])
                    newlist.append(recordList[iterator + 3])
                    newlist.append(recordList[iterator + 4])

                iterator += 5
                count += 1


        elif (var.get() == 2):

            iterator = 2
            while count < (len(recordList) / 5):
                if (recordList[iterator] == (desig.get() + "\n")):
                    pass
                else:
                    newlist.append(recordList[iterator - 2])
                    newlist.append(recordList[iterator - 1])
                    newlist.append(recordList[iterator])
                    newlist.append(recordList[iterator + 1])
                    newlist.append(recordList[iterator + 2])

                iterator += 5
                count += 1

        elif (var.get() == 3):

            iterator = 1
            while count < (len(recordList) / 5):

                if (recordList[iterator] == (dept.get() + "\n")):
                    pass
                else:
                    newlist.append(recordList[iterator - 1])
                    newlist.append(recordList[iterator])
                    newlist.append(recordList[iterator + 1])
                    newlist.append(recordList[iterator + 2])
                    newlist.append(recordList[iterator + 3])

                iterator += 5
                count += 1

        # if record doesn't exist
        if (len(newlist) == len(recordList)):
            messagebox._show("Error", "Entered record doesn't exist.")
            root.destroy()
            return

        # deletes the record and r=write the content to file
        with open("db.txt", "w") as output:
            output.writelines(newlist)
        messagebox._show("Deletion Complete", "Successfully  deleted record.")
        root.destroy()

    # setting GUI Screen
    w = 600
    h = 500
    root = Toplevel(main_window)
    root.geometry("%dx%d+0+0" % (w, h))
    root["bg"] = "black"
    var = IntVar()

    name = Entry(root,
                 bd=5,
                 fg="#00ffff",
                 bg="#000000")

    desig = Entry(root,
                  bd=5,
                  fg="#00ffff",
                  bg="#000000")

    dept = Entry(root,
                 bd=5,
                 fg="#00ffff",
                 bg="#000000")

    def choice():
        if (var.get() == 1):
            name_label = Label(root,
                               text="Name:        ",
                               font=('Arial', 15),
                               fg="#0099ff",
                               bg="#000000").place(x=160, y=200)

            name.place(x=285, y=200)

        elif (var.get() == 2):
            desig_label = Label(root,
                                text="Designation:",
                                font=('Arial', 15),
                                fg="#0099ff",
                                bg="#000000").place(x=160, y=200)

            desig.place(x=285, y=200)

        else:
            dept_label = Label(root,
                               text="Department: ",
                               font=('Arial', 15),
                               fg="#77ff33",
                               bg="#000000").place(x=160, y=200)

            dept.place(x=285, y=200)

    deleteby_message = Message(root,
                               text="\nDelete By: ",
                               fg="#00cc66",
                               bg="#000000",
                               padx=3,
                               pady=3,
                               anchor=N,
                               font=('Arial', 23, "bold"),
                               width=w).pack()

    name_RadioButton = Radiobutton(root,
                                   text="Delete by name",
                                   bg="#000000",
                                   fg="#99ff66",
                                   variable=var,
                                   font=('Arial', 13),
                                   value=1,
                                   command=choice).place(x=30, y=120)

    desig_RadioButton = Radiobutton(root,
                                    text="Delete by designation",
                                    bg="#000000",
                                    fg="#99ff66",
                                    font=('Arial', 13),
                                    variable=var,
                                    value=2,
                                    command=choice).place(x=190, y=120)

    dept_RadioButton = Radiobutton(root,
                                   text="Delete by department",
                                   font=('Arial', 13),
                                   bg="#000000",
                                   fg="#99ff66",
                                   variable=var,
                                   value=3,
                                   command=choice).place(x=390, y=120)

    delete_button = Button(root,
                           text="DELETE",
                           fg="#99ccff",
                           padx=5,
                           pady=4,
                           bg="#000000",
                           command=Del_record,
                           font=('Georgia', 15)).place(x=350, y=400)

    root.mainloop()


#             ***** Function to search records *****


def search():
    w, h = 600, 500

    root = Toplevel(main_window)
    root.geometry("%dx%d+0+0" % (w, h))
    root["bg"] = "black"

    # error checking if file doesn't exists
    try:
        with open("db.txt", "r") as input:
            recordList = input.readlines()
    except:
        messagebox._show("Error", "An error occured. Check if file is present or not.")
        root.destroy()
        return

    nameFlag = IntVar()
    deptFlag = IntVar()
    desigFlag = IntVar()
    statusFlag = IntVar()
    salaryFlag = IntVar()

    def find():
        shortlisted_entries = []


        if (nameFlag.get() == 1):
            iterator = 0
            count = 0
            while count < (len(recordList) / 5):
                if recordList[iterator] == (name.get() + "\n"):
                    shortlisted_entries.append(recordList[iterator])
                    shortlisted_entries.append(recordList[iterator + 1])
                    shortlisted_entries.append(recordList[iterator + 2])
                    shortlisted_entries.append(recordList[iterator + 3])
                    shortlisted_entries.append(recordList[iterator + 4])

                iterator += 5
                count += 1

        if (desigFlag.get() == 1):
            count = 0
            iterator = 2

            if (nameFlag.get() == 1 and len(shortlisted_entries) == 0):
                messagebox.showinfo("Ooopss...", "No Record Found!")
                root.destroy()
                return
            elif (nameFlag.get() == 1 and len(shortlisted_entries) > 0):
                templist = []
                while count < (len(shortlisted_entries) / 5):
                    if (shortlisted_entries[iterator] == (designation.get() + "\n")):
                        templist.append(shortlisted_entries[iterator - 2])
                        templist.append(shortlisted_entries[iterator - 1])
                        templist.append(shortlisted_entries[iterator])
                        templist.append(shortlisted_entries[iterator + 1])
                        templist.append(shortlisted_entries[iterator + 2])

                    iterator += 5
                    count += 1
                shortlisted_entries = templist
            else:
                while count < (len(recordList) / 5):
                    if recordList[iterator] == (designation.get() + "\n"):
                        shortlisted_entries.append(recordList[iterator - 2])
                        shortlisted_entries.append(recordList[iterator - 1])
                        shortlisted_entries.append(recordList[iterator])
                        shortlisted_entries.append(recordList[iterator + 1])
                        shortlisted_entries.append(recordList[iterator + 2])

                    iterator += 5
                    count += 1

        if (deptFlag.get() == 1):

            count = 0
            iterator = 1

            if (desigFlag.get() == 1 and len(shortlisted_entries) == 0):
                messagebox.showinfo("Ooopss...", "No Record Found!")
                root.destroy()
                return
            elif (desigFlag.get() == 1 and len(shortlisted_entries) > 0):
                templist = []
                while count < (len(shortlisted_entries) / 5):
                    if (shortlisted_entries[iterator] == (department.get() + "\n")):
                        templist.append(shortlisted_entries[iterator - 1])
                        templist.append(shortlisted_entries[iterator])
                        templist.append(shortlisted_entries[iterator + 1])
                        templist.append(shortlisted_entries[iterator + 2])
                        templist.append(shortlisted_entries[iterator + 3])

                    iterator += 5
                    count += 1
                shortlisted_entries = templist
            else:

                while count < (len(recordList) / 5):
                    if recordList[iterator] == (department.get() + "\n"):
                        shortlisted_entries.append(recordList[iterator - 1])
                        shortlisted_entries.append(recordList[iterator])
                        shortlisted_entries.append(recordList[iterator + 1])
                        shortlisted_entries.append(recordList[iterator + 2])
                        shortlisted_entries.append(recordList[iterator + 3])

                    iterator += 5
                    count += 1

        if (salaryFlag.get() == 1):

            count = 0
            iterator = 4

            if (deptFlag.get() == 1 and len(shortlisted_entries) == 0):
                messagebox.showinfo("Ooopss...", "No Record Found!")
                root.destroy()
                return
            elif (deptFlag.get() == 1 and len(shortlisted_entries) > 0):
                templist = []
                while count < (len(shortlisted_entries) / 5):
                    if (shortlisted_entries[iterator] == (salary.get() + "\n")):
                        templist.append(shortlisted_entries[iterator - 4])
                        templist.append(shortlisted_entries[iterator - 3])
                        templist.append(shortlisted_entries[iterator - 2])
                        templist.append(shortlisted_entries[iterator - 1])
                        templist.append(shortlisted_entries[iterator])

                    iterator += 5
                    count += 1
                shortlisted_entries = templist

            else:
                while count < (len(recordList) / 5):
                    if recordList[iterator] == (department.get() + "\n"):
                        shortlisted_entries.append(recordList[iterator - 4])
                        shortlisted_entries.append(recordList[iterator - 3])
                        shortlisted_entries.append(recordList[iterator - 2])
                        shortlisted_entries.append(recordList[iterator - 1])
                        shortlisted_entries.append(recordList[iterator])

                    iterator += 5
                    count += 1

        if (statusFlag.get() == 1):

            count = 0
            iterator = 3

            if (salaryFlag.get() == 1 and len(shortlisted_entries) == 0):
                messagebox.showinfo("Ooopss...", "No Record Found!")
                root.destroy()
                return
            elif (salaryFlag.get() == 1 and len(shortlisted_entries) > 0):
                templist = []
                while count < (len(shortlisted_entries) / 5):
                    if (shortlisted_entries[iterator] == (status.get() + "\n")):
                        templist.append(shortlisted_entries[iterator - 3])
                        templist.append(shortlisted_entries[iterator - 2])
                        templist.append(shortlisted_entries[iterator - 1])
                        templist.append(shortlisted_entries[iterator])
                        templist.append(shortlisted_entries[iterator + 1])

                    iterator += 5
                    count += 1
                shortlisted_entries = templist
            else:

                while count < (len(recordList) / 5):
                    if recordList[iterator] == (department.get() + "\n"):
                        shortlisted_entries.append(recordList[iterator - 3])
                        shortlisted_entries.append(recordList[iterator - 2])
                        shortlisted_entries.append(recordList[iterator - 1])
                        shortlisted_entries.append(recordList[iterator])
                        shortlisted_entries.append(recordList[iterator + 1])

                    iterator += 5
                    count += 1
        if (len(shortlisted_entries) == 0):
            messagebox._show("Oooppss...", "No Record Found!")
            root.destroy()
            return
        else:
            show(shortlisted_entries, root)

    def onCheckButtonClick():
        if (nameFlag.get() == 1):
            name.config(state=NORMAL)
        else:
            name.delete(0, END)
            name.config(state=DISABLED)

        if (desigFlag.get() == 1):
            designation.config(state=NORMAL)
        else:
            designation.delete(0, END)
            designation.config(state=DISABLED)

        if (deptFlag.get() == 1):
            department.config(state=NORMAL)
        else:
            department.delete(0, END)
            department.config(state=DISABLED)

        if (salaryFlag.get() == 1):
            salary.config(state=NORMAL)
        else:
            salary.delete(0, END)
            salary.config(state=DISABLED)

        if (statusFlag.get() == 1):
            status.config(state=NORMAL)
        else:
            status.delete(0, END)
            status.config(state=DISABLED)


    search_message = Message(root,
                             text="Tick the boxes you want to search: ",
                             fg="#cc00cc",
                             bg="#000000",
                             padx=3,
                             pady=3,
                             anchor=N,
                             font=('Arial', 20, "bold"),
                             width=w).pack()

    name_check_button = Checkbutton(root,
                                    text="Name",
                                    variable=nameFlag,
                                    fg="#ff33cc",
                                    bg="#000000",
                                    command=onCheckButtonClick,
                                    font=('Arial', 10),
                                    onvalue=1,
                                    offvalue=0).place(x=60, y=60)

    dept_check_button = Checkbutton(root,
                                    text="Department",
                                    variable=deptFlag,
                                    command=onCheckButtonClick,
                                    fg="#ff33cc",
                                    bg="#000000",
                                    font=('Arial', 10),
                                    onvalue=1,
                                    offvalue=0).place(x=130, y=60)

    desig_check_button = Checkbutton(root,
                                     text="Designation",
                                     variable=desigFlag,
                                     fg="#ff33cc",
                                     bg="#000000",
                                     command=onCheckButtonClick,
                                     font=('Arial', 10),
                                     onvalue=1,
                                     offvalue=0).place(x=230, y=60)

    salary_check_button = Checkbutton(root,
                                      text="Salary",
                                      variable=salaryFlag,
                                      fg="#ff33cc",
                                      bg="#000000",
                                      command=onCheckButtonClick,
                                      font=('Arial', 10),
                                      onvalue=1,
                                      offvalue=0).place(x=330, y=60)

    status_check_button = Checkbutton(root,
                                      text="Status",
                                      variable=statusFlag,
                                      fg="#ff33cc",
                                      bg="#000000",
                                      command=onCheckButtonClick,
                                      font=('Arial', 10),
                                      onvalue=1,
                                      offvalue=0).place(x=410, y=60)

    name_label = Label(root,
                       text="Name:",
                       font=('Arial', 15),
                       fg="#ff99cc",
                       bg="#000000").place(x=100, y=140)
    name = Entry(root,
                 bd=5,
                 state=DISABLED,
                 fg="#ff99cc",
                 bg="#000000")

    department_label = Label(root,
                             text="Department:",
                             font=('Arial', 15),
                             fg="#ff99cc",
                             bg="#000000").place(x=100, y=175)
    department = Entry(root,
                       bd=5,
                       state=DISABLED,
                       fg="#ff99cc",
                       bg="#000000")

    designation_label = Label(root,
                              text="Designation:",
                              font=('Arial', 15),
                              fg="#ff99cc",
                              bg="#000000").place(x=100, y=210)

    designation = Entry(root,
                        bd=5,
                        state=DISABLED,
                        fg="#ff99cc",
                        bg="#000000")

    status_label = Label(root,
                         text="Status:",
                         font=('Arial', 15),
                         fg="#ff99cc",
                         bg="#000000").place(x=100, y=245)

    status = Entry(root,
                   bd=5,
                   state=DISABLED,
                   fg="#ff99cc",
                   bg="#000000")

    salary_label = Label(root,
                         text="Salary:",
                         font=('Arial', 15),
                         fg="#ff99cc",
                         bg="#000000").place(x=100, y=280)

    salary = Entry(root,
                   bd=5,
                   state=DISABLED,
                   fg="#ff99cc",
                   bg="#000000")

    search_button = Button(root,
                           text="SEARCH",
                           fg="#99ccff",
                           padx=5,
                           pady=4,
                           bg="#000000",
                           command = find,
                           font=('Georgia', 15)).place(x=450, y=420)

    name.place(x=220, y=140)
    department.place(x=220, y=175)
    designation.place(x=220, y=210)
    status.place(x=220, y=245)
    salary.place(x=220, y=280)

    root.mainloop()


#             ***** Function to update records *****


def update():
    def applyChange():

        nonlocal root

        # check for valid inputs
        try:
            if (dept.get() == ""):
                raise ValueError('Invalid Input')
            if (desig.get() == ""):
                raise ValueError('Invalid Input')
            if (name.get() == ""):
                raise ValueError('Invalid Input')
        except:

            messagebox._show("Invalid Input", "Please enter valid inputs. Closing this window.")
            root.destroy()

        nonlocal uname, udept, udesig

        uname = name.get() + "\n"
        udesig = desig.get() + "\n"
        udept = dept.get() + "\n"

        nonlocal count
        nonlocal iterator

        while count < (len(record) / 5):
            if (record[iterator] == uname and record[iterator + 1] == udept and record[iterator + 2] == udesig):
                detailWindow()
                return
            iterator += 5
            count += 1

        messagebox._show("Error", "No record found by given information.")
        root.destroy()

    def detailWindow():

        def ToFile():

            nonlocal salary, name_, department, designation, status, win

            try:
                eval(salary.get())
                if (name_.get() == ""):
                    raise ValueError('Invalid Input')
                if (department.get() == ""):
                    raise ValueError('Invalid Input')
                if (designation.get() == ""):
                    raise ValueError('Invalid Input')
                if (status.get() == ""):
                    raise ValueError('Invalid Input')
            except:
                messagebox._show("Invalid Input", "Please enter valid inputs. Closing this window.")
                win.destroy()

            nonlocal uname, udesig, udept, usalary, ustatus, iterator, count, record

            uname = name_.get() + "\n"
            ustatus = status.get() + "\n"
            udept = department.get() + "\n"
            udesig = designation.get() + "\n"
            usalary = salary.get() + "\n"

            record[iterator] = uname
            record[iterator + 1] = udept
            record[iterator + 2] = udesig
            record[iterator + 3] = ustatus
            record[iterator + 4] = usalary

            # writing updated record to file
            with open("db.txt", 'w') as output:
                output.writelines(record)
            messagebox._show("Success", "Record successfully updated.")
            win.destroy()

        nonlocal root
        root.destroy()

        w = h = 500
        win = Toplevel(main_window)
        win.geometry("%dx%d+0+0" % (w, h))
        win["bg"] = "black"

        enterDetail_message = Message(win,
                                      text="\nEnter your details: ",
                                      fg="#006699",
                                      bg="#000000",
                                      padx=3,
                                      pady=3,
                                      anchor=N,
                                      font=('Arial', 20, "bold"),
                                      width=w).pack()

        name_label = Label(win,
                           text="Name:",
                           font=('Arial', 15),
                           fg="#0099ff",
                           bg="#000000").place(x=100, y=130)
        name_ = Entry(win,
                      bd=5,
                      fg="#00ffff",
                      bg="#000000")

        department_label = Label(win,
                                 text="Department:",
                                 font=('Arial', 15),
                                 fg="#0099ff",
                                 bg="#000000").place(x=100, y=165)
        department = Entry(win,
                           bd=5,
                           fg="#00ffff",
                           bg="#000000")

        designation_label = Label(win,
                                  text="Designation:",
                                  font=('Arial', 15),
                                  fg="#0099ff",
                                  bg="#000000").place(x=100, y=200)

        designation = Entry(win,
                            bd=5,
                            fg="#00ffff",
                            bg="#000000")

        status_label = Label(win,
                             text="Status:",
                             font=('Arial', 15),
                             fg="#0099ff",
                             bg="#000000").place(x=100, y=235)

        status = Entry(win,
                       bd=5,
                       fg="#00ffff",
                       bg="#000000")

        salary_label = Label(win,
                             text="Salary:",
                             font=('Arial', 15),
                             fg="#0099ff",
                             bg="#000000").place(x=100, y=270)

        salary = Entry(win,
                       bd=5,
                       fg="#00ffff",
                       bg="#000000")

        submit_button = Button(win,
                               text="SUBMIT",
                               fg="#99ccff",
                               padx=5,
                               pady=4,
                               bg="#000000",
                               command=ToFile,
                               font=('Georgia', 15)).place(x=350, y=400)

        name_.place(x=220, y=130)
        department.place(x=220, y=165)
        designation.place(x=220, y=200)
        status.place(x=220, y=235)
        salary.place(x=220, y=270)

        win.mainloop()

    w = h = 500
    iterator = 0
    count = 0
    record = []
    root = Toplevel(main_window)
    root.geometry("%dx%d+0+0" % (w, h))
    root["bg"] = "black"

    uname = ""
    udept = ""
    udesig = ""
    ustatus = ""
    usalary = ""

    try:
        with open("db.txt", "r") as input:
            record = input.readlines()
    except:
        messagebox._show("Error", "An error occured. Check if file is present or not.")
        root.destroy()
        return

    if (len(record) == 0):
        messagebox._show("Empty File", "Empty File. Cannot Update.")
        return

    enterDetail_message = Message(root,
                                  text="\nEnter your details: ",
                                  fg="#ff9933",
                                  bg="#000000",
                                  padx=3,
                                  pady=3,
                                  anchor=N,
                                  font=('Arial', 20, "bold"),
                                  width=w).pack()

    name_label = Label(root,
                       text="Name:",
                       font=('Arial', 15),
                       fg="#ffcc00",
                       bg="#000000").place(x=100, y=130)
    name = Entry(root,
                 bd=5,
                 fg="#00ffff",
                 bg="#000000")

    dept_label = Label(root,
                       text="Department:",
                       font=('Arial', 15),
                       fg="#ffcc00",
                       bg="#000000").place(x=100, y=180)
    dept = Entry(root,
                 bd=5,
                 fg="#00ffff",
                 bg="#000000")

    desig_label = Label(root,
                        text="Designation:",
                        font=('Arial', 15),
                        fg="#ffcc00",
                        bg="#000000").place(x=100, y=230)
    desig = Entry(root,
                  bd=5,
                  fg="#00ffff",
                  bg="#000000")

    Update_button = Button(root,
                           text="UPDATE",
                           fg="#ffff99",
                           padx=5,
                           pady=4,
                           bg="#000000",
                           command=applyChange,
                           font=('Georgia', 15)).place(x=350, y=420)

    name.place(x=220, y=130)
    dept.place(x=220, y=180)
    desig.place(x=220, y=230)

    root.mainloop()

#             ***** Function to show records to users *****

def show(rec , _root):

    _root.destroy() # closing the window which called this method
    iterator = 0
    count = 0
    prevFlag = False
    nextFlag = True

    w = 750
    h = 550
    root = Toplevel(main_window)
    root.geometry("%dx%d+0+0" % (w, h))
    root["bg"] = "black"

    nameSTR = StringVar()
    salarySTR = StringVar()
    statusSTR = StringVar()
    desigSTR = StringVar()
    deptSTR = StringVar()

    def change():

        nonlocal iterator, nameSTR, salarySTR, statusSTR, desigSTR, deptSTR

        nameSTR.set("Name:          " + rec[iterator])
        salarySTR.set("Salary:         " + rec[iterator + 4])
        statusSTR.set("Status:         " + rec[iterator + 3])
        desigSTR.set("Designation: " + rec[iterator + 2])
        deptSTR.set("Department: " + rec[iterator + 1])
        print(nameSTR.get())

    change()

    def next_fn():
        nonlocal iterator, count, prevFlag, nextFlag

        if (count == ((len(rec)) / 5) - 1):
            next_button['state'] = DISABLED
            nextFlag = False
            if (prevFlag == False):
                prev_button['state'] = NORMAL
                prevFlag = True
            return
        if (prevFlag == False):
            prev_button['state'] = NORMAL
            prevFlag = True
        iterator += 5
        count += 1
        change()

    def prev_fn():
        nonlocal iterator, count, prevFlag, nextFlag

        if (count == 0):
            prev_button['state'] = DISABLED
            prevFlag = False
            if (nextFlag == False):
                next_button['state'] = NORMAL
                nextFlag = True
            return
        if (nextFlag == False):
            next_button['state'] = NORMAL
            nextFlag = True
        iterator -= 5
        count -= 1
        change()

    def first_fn():
        nonlocal iterator, count, prevFlag, nextFlag

        prev_button['state'] = DISABLED
        prevFlag = False
        if (nextFlag == False):
            next_button['state'] = NORMAL
            nextFlag = True

        iterator = 0
        count = 0
        change()

    def last_fn():
        nonlocal iterator, count, prevFlag, nextFlag

        next_button['state'] = DISABLED
        nextFlag = False
        if (prevFlag == False):
            prev_button['state'] = NORMAL
            prevFlag = True

        iterator = (len(rec) - 5)
        count = (len(rec) / 5) - 1
        change()

    recordDetail_message = Message(root,
                                   text="\nRecord Details: ",
                                   fg="#99ffcc",
                                   bg="#000000",
                                   padx=3,
                                   pady=3,
                                   anchor=N,
                                   font=('Arial', 20, "bold"),
                                   width=w).pack()

    name_label = Label(root,
                         textvariable = nameSTR,
                         font=('Arial', 17),
                         fg="#ffff66",
                         bg="#000000")
    name_label.place(x=270, y=170)

    department_label = Label(root,
                             textvariable=deptSTR,
                             font=('Arial', 17),
                             fg="#ffff66",
                             bg="#000000").place(x=270, y=205)

    designation_label = Label(root,
                              textvariable=desigSTR,
                              font=('Arial', 17),
                              fg="#ffff66",
                              bg="#000000").place(x=270, y=240)

    status_label = Label(root,
                         textvariable=statusSTR,
                         font=('Arial', 17),
                         fg="#ffff66",
                         bg="#000000").place(x=270, y=275)

    salary_label = Label(root,
                         textvariable=salarySTR,
                         font=('Arial', 17),
                         fg="#ffff66",
                         bg="#000000").place(x=270, y=310)

    next_button = Button(root,
                         text=" Next -> ",
                         fg="#00cc99",
                         padx=5,
                         pady=4,
                         bg="#000000",
                         state=NORMAL,
                         command=next_fn,
                         font=('Georgia', 15))

    first_button = Button(root,
                          text="<< First ",
                          fg="#00cc99",
                          padx=3,
                          pady=4,
                          bg="#000000",
                          command=first_fn,
                          font=('Georgia', 15))

    last_button = Button(root,
                         text=" Last >>",
                         fg="#00cc99",
                         padx=5,
                         pady=4,
                         bg="#000000",
                         command=last_fn,
                         font=('Georgia', 15))

    prev_button = Button(root,
                         text=" <- Previous ",
                         fg="#00cc99",
                         padx=5,
                         pady=4,
                         bg="#000000",
                         state=DISABLED,
                         command=prev_fn,
                         font=('Georgia', 15))

    close_button = Button(root,
                          text=" Close (X)",
                          fg="#ff0000",
                          padx=5,
                          pady=4,
                          bg="#000000",
                          command=root.destroy,
                          font=('Georgia', 15)).place(x=330, y=450)

    first_button.place(x=20, y=450)
    prev_button.place(x=130, y=450)
    next_button.place(x=510, y=450)
    last_button.place(x=630, y=450)

    root.mainloop()


#             ***** Function to display records *****


def display():
    w = 750
    h = 550
    root = Toplevel(main_window)
    root.geometry("%dx%d+0+0" % (w, h))
    root["bg"] = "black"

    record = []

    try:
        with open("db.txt", "r") as input:
            record = input.readlines()
    except:
        messagebox._show("Error", "An error occured. Check if file is present or not.")
        root.destroy()
        return

    if (len(record) == 0):
        messagebox._show("Empty File", "File is empty. Insert records.")
        root.destroy()
        return

    show(record, root)



#             ***** Main Window of the program *****

main_window = Tk()
w, h = main_window.winfo_screenwidth(), main_window.winfo_screenheight()
main_window.geometry("%dx%d+0+0" %(w, h))
main_window["bg"] = "black"
main_window.title("Faculty Database")

welcome_message = Message(main_window,
                          text = "\nWELCOME TO FACULTY DATABASE!",
                          fg = "#00ff00",
                          bg = "#000000",
                          padx = 5,
                          pady = 5,
                          anchor = N,
                          font=('Arial', 30, "bold"),
                          width = w).pack()

description = Message(main_window,
                          text = "\nPlease choose your desired option...",
                          fg = "#ccff33",
                          bg = "#000000",
                          padx = 5,
                          pady = 5,
                          anchor = N,
                          font=('Arial', 20),
                          width = w).place(x = (w/2) - 220, y = 150)


display_button = Button(main_window,
                    text = "         Display         ",
                    fg = "#ffff00",
                    padx = 5,
                    pady = 4,
                    bg = "#000000",
                    command = display,
                    font=('Georgia', 15)).place(x = (w/2) - 100, y = 300)


add_button = Button(main_window,
                    text = "Create New Entry",
                    fg = "#ffff00",
                    padx = 5,
                    pady = 4,
                    bg = "#000000",
                    font=('Georgia', 15),
                    command = add).place(x = (w/2) - 100, y = 360)

del_button = Button(main_window,
                    text = "    Delete Entry     ",
                    fg = "#ffff00",
                    padx = 5,
                    pady = 4,
                    bg = "#000000",
                    command = delete,
                    font=('Georgia', 15)).place(x = (w/2) - 100, y = 420)

update_button = Button(main_window,
                    text = "         Update          ",
                    fg = "#ffff00",
                    padx = 5,
                    pady = 4,
                    bg = "#000000",
                    command = update,
                    font=('Georgia', 15)).place(x = (w/2) - 100, y = 480)

search_button = Button(main_window,
                    text = "          Search          ",
                    fg = "#ffff00",
                    padx = 5,
                    pady = 4,
                    bg = "#000000",
                    command = search,
                    font=('Georgia', 15)).place(x = (w/2) - 100, y = 540)

exit_button = Button(main_window,
                    text = "            Exit             ",
                    fg = "#ffff00",
                    padx = 5,
                    pady = 4,
                    bg = "#000000",
                    font=('Georgia', 15),
                    command = main_window.destroy).place(x = (w/2) - 100, y = 600)

main_window.mainloop()