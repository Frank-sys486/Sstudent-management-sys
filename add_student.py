from tkinter import *
class AddStudent:
    def __init__(self, student_data):
        self.student_data = student_data
    
    def input_details_student(self):
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        idnum = input("Enter IDNumber: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")
        self.addstudent(name, age, idnum, email, phone)
    
    def addstudent(self,name, age, idnum, email, phone):
        self.student_data.set_name(name)
        self.student_data.set_age(age)
        self.student_data.set_id_num(idnum)
        self.student_data.set_email(email)
        self.student_data.set_phone_number(phone)
        student = [name, age, idnum, email, phone]
        self.student_data.allstudents.append(student)
        student = f"{name}, {age}, {idnum}, {email}, {phone}"
        self.write_to_file(student)
    
    def write_to_file(self, student):
        with open("student_data.txt", "a+") as file:
            for x in student:
                file.write(f"{x}")
            file.write("\n")
            file.close()
    print("Student Data added to the database")

    def show_gui(self, frame, full_frame):
        # Popup frame for error or success messages
        frame.config(bg='#2d2d30')
        self.Popup_frame = Frame(full_frame, bg="white", borderwidth=2, relief="ridge", background="#2d2d30")
        self.lblPopup = Label(self.Popup_frame, text='', font="Arial 18 bold", bg="white", fg="black", pady=10, padx=10)
        self.lblPopup.pack(fill="x", padx=5, pady=5)
        Button(self.Popup_frame, text="OK", font="Arial 15 bold", bg="#4CAF50", fg="white", 
            command=lambda: self.Popup_frame.place_forget()).pack(pady=10)

        # Registration Labels and Entry Widgets
        self.lblReg = ['Name', 'Age', 'Student ID', 'Email Address', 'Phone Number']
        self.entryReg = []

        Label(frame, text="Register New Student", font="Arial 20 bold", bg="#333", fg="white", pady=10).grid(
            row=0, column=0, columnspan=4, sticky="nsew")

        for i in range(len(self.lblReg)):
            # Labels with a consistent look
            Label(frame, text=self.lblReg[i], font="Arial 15", bg="#4CAF50", fg="white", 
                padx=10, pady=5, border=0, relief="solid", anchor="e").grid(row=i+1, column=0, sticky="nsew")
            
            # Entries with padding and borders
            entry = Entry(frame, font="Arial 15", bg="#2d2d30", fg="white", relief="solid", borderwidth=0.5)
            entry.grid(row=i+1, column=1, columnspan=3, sticky="nsew", padx=5, pady=5)
            self.entryReg.append(entry)
 
        # Register Button
        Button(frame, text="Register Student", font="Arial 15 bold", bg="#4CAF50", fg="white", 
            padx=10, pady=5, command=self.check_entries).grid(row=len(self.lblReg)+1, column=0, columnspan=4, pady=10)

        # Adjust column and row spacing for a clean layout
        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)
        frame.pack()



    def check_entries(self):
        errors = []
        for i in range(len(self.entryReg)):
            if self.entryReg[i].get() == '':
                errors.append(f'\n{self.lblReg[i]}')

        if not errors:
            self.addstudent(*(entry.get() for entry in self.entryReg[:5]))
            [entry.delete(0, END) for entry in self.entryReg]
            self.lblPopup.config(text='Student Added to the Database!', fg='white',bg='#2d2d30')
        else:
            self.lblPopup.config(text=f'Hey! You forgot to fill the following information:{",".join(errors)}', fg='red', bg='#2d2d30')

        self.Popup_frame.place(relx=0.5, rely=0.5, anchor="center")

