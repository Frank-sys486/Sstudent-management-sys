from tkinter import *
class SearchStudent:
    def __init__(self, student_data):
        self.student_data = student_data

    def search_by_id(self):
        id_to_search = input("Enter ID Number to search: ")
        found = False
        for student in self.student_data.allstudents:
            if student[2] == id_to_search:  
                print("\n===== Student Found =====")
                print(f"Name: {student[0]}")
                print(f"Age: {student[1]}")
                print(f"ID Number: {student[2]}")
                print(f"Email: {student[3]}")
                print(f"Phone Number: {student[4]}")
                print("=========================\n")
                found = True
                
                break
        if not found:
            print("Student not found!")


    def show_gui(self, frame, full_frame):
        self.Popup_frame = Frame(full_frame, bg="#f0f0f0", borderwidth=2, relief="groove")
        self.lblReg, self.entryReg = ['Enter ID to search'], []        
        Label(frame, text="Student Search", font="Arial 20 bold", bg="#333", fg="white", pady=10).pack(fill="x")
        input_frame = Frame(frame, bg="#2d2d30")
        input_frame.pack(pady=20)

        for i in range(len(self.lblReg)):
            Label(input_frame, text=self.lblReg[i], font="Arial 15", width=15, anchor='e', bg="#2d2d30", fg='white').grid(row=i, column=0, padx=10, pady=5)
            self.entryReg.append(Entry(input_frame, font="Arial 15", width=20, borderwidth=2, relief="ridge", bg="#2d2d30", fg="white"))
            self.entryReg[i].grid(row=i, column=1, padx=10, pady=5)

        Button(frame, text="Search", font="Arial 15 bold", bg="#4CAF50", fg="white", 
            activebackground="#45a049", activeforeground="white", command=self.check_entries).pack(pady=10)

    def check_entries(self):
        for widget in self.Popup_frame.winfo_children():
            widget.destroy()

        text, found = ['Name', 'Age', 'ID Number', 'Email', 'Phone Number'], False

        griD = Frame(self.Popup_frame, bg="white", borderwidth=2, relief="ridge")
        griD.pack(padx=10, pady=10)

        for student in self.student_data.allstudents:
            if student[2] == self.entryReg[0].get():
                # Display search results
                for i in range(len(text)):
                    Label(griD, text=text[i], font="Arial 13 bold", bg="white", fg="#333", width=15, anchor='e').grid(column=0, row=i, padx=5, pady=5)
                    Label(griD, text=student[i], font="Arial 13", bg="white", fg="#555", width=20, anchor='w').grid(column=1, row=i, padx=5, pady=5)
                found = True
                break

        if not found:
            Label(griD, text="Student not found!", font="Arial 15 bold", fg="red", bg="white").pack(padx=10, pady=10)

        Button(self.Popup_frame, text="OK", font="Arial 15 bold", bg="#f44336", fg="white", 
            activebackground="#e53935", activeforeground="white", 
            command=lambda: self.Popup_frame.place_forget()).pack(pady=10)

        self.Popup_frame.place(relx=0.5, rely=0.5, anchor="center")

                
            
        
        