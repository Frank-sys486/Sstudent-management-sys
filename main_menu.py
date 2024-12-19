class MainMenu:
    def __init__(self, add_student, print_all_students, search_student):
        self.add_student = add_student
        self.print_all_students = print_all_students
        self.search_student = search_student
        self.logged_in = False  
        self.current_student = None 

    '''def display_menu(self):
        self.login() 
        while True:
            print("\n===== Main Menu =====")
            print("Please choose from the following options:")
            print("1. View your information")
            print("2. View other student's information")
            print("3. Register a New Student")
            print("4. Print all students in the list")
            print("5. Exit...")

            choice = input("Select an option: ")

            if choice == "1":
                self.view_your_information()
            elif choice == "2":
                self.search_student.search_by_id()
            elif choice == "3":
                self.add_student.input_details_student()
            elif choice == "4":
                self.print_all_students.print_all_students()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")
'''
    def login(self,idnum):
        max_attempts = 3  
        attempts = 0  
        while attempts < max_attempts:
            #idnum = input("Enter your ID Number: ")
            for student in self.add_student.student_data.allstudents:
                if student[2] == idnum:  
                    self.logged_in = True
                    self.current_student = student  
                    print(f"Welcome, {student[0]}!") 

                    return True
            return False
            attempts += 1  
            print(f"ID Number not found! Attempts left: {max_attempts - attempts}")
        
        print("Maximum attempts exceeded. Please try again later.")
        exit() 

    def view_your_information(self):
        if self.logged_in and self.current_student:
            print("\n===== Your Information =====")
            print(f"Name: {self.current_student[0]}")
            print(f"Age: {self.current_student[1]}")
            print(f"ID Number: {self.current_student[2]}")
            print(f"Email: {self.current_student[3]}")
            print(f"Phone Number: {self.current_student[4]}")
            print("============================\n")
        else:
            print("No information available. Please log in first.")


