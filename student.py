class StudentInfo:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.idnum = ""
        self.email = ""
        self.phone = ""
        self.allstudents = []
        self.read_file()

    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
    
    def set_id_num(self, idnum):
        self.idnum = idnum
    
    def set_email(self, email):
        self.email = email
    
    def set_phone_number(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_id_num(self):
        return self.idnum
    
    def get_email(self):
        return self.email
    
    def get_phone_number(self):
        return self.phone
    
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"ID Number: {self.idnum}\n"
                f"Email: {self.email}\n"
                f"Phone Number: {self.phone}")
    
    def read_file(self):
        try: 
            with open("student_data.txt", "r") as file:
                lines = file.readlines()
                for line in lines[0:]:
                    student_data = line.strip().split(", ")
                    self.allstudents.append(student_data)
            print("All students")
        except FileNotFoundError:
            print("No existing student data found")

