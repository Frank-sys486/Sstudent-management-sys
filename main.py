from student import StudentInfo
from main_menu import MainMenu
from searchstudent import SearchStudent
from add_student import AddStudent
from print_all_students import PrintAllStudent

print(1)
stu = StudentInfo()
print(2)
addstud = AddStudent(stu)  
print(3)
printall = PrintAllStudent(stu)  
print(4)
search = SearchStudent(stu)  
print(5)
menu = MainMenu(addstud, printall, search)
print(6)
#main_menu.display_menu()




