from tkinter import *
from functools import partial
#from main import *

win = Tk()
win.title("Student System")
win.geometry('1280x720')
#====== Frames
#login frame
login_frame = LabelFrame(win, width=200, height=100, background='lightgray', text='login')
login_frame.pack_propagate(False)
login_frame.pack(pady = 300)
# top frame
top_frame = Frame(win, bg = 'gray', height= 50)
top_frame.pack_propagate(False)
# Left Frame 30% of 1280 = 384
left_frame = Frame(win, bg="lightblue", width=384)  
left_frame.pack_propagate(False)
# Right Frame (70% width)
right_frame = Frame(win, bg="lightgray")
right_frame.pack_propagate(False)
# header page
lblHeader = Label(right_frame,text="Initializing header. This shouldn't be displayed!", font = "arial 15")

#===== functions/pages
current_page = 0
panel = Frame(right_frame)
def main_menu():
    global name, age, id, email, phone, current_page, panel, bttnHome
    print('Main Menu Clicked!')
    bttnHome.config(state=DISABLED)
    panel = Frame(right_frame)
    lblHeader.config(text=f"Welcome, {name}!", font = "arial 15")    
    lblHeader.pack()
    if current_page != 1:
        profile = PhotoImage(file=r"media\blnk_profile.png")
        lblImage = Label(panel, image=profile, height= 100, width= 100)
        lblImage.image = profile
        lblImage.pack(pady=20)
    current_page = 1
    panel.pack()
    bttnHome.config(state=NORMAL)   
def add_student():
    global current_page, panel, bttnAdd
    bttnAdd.config(state=DISABLED)
    print('Add_student Clicked!')
    panel.destroy()
    if current_page != 2:
        lblHeader.config(text = "This is header of Add student")
        lblHeader.pack()
    
    current_page = 2
    bttnAdd.config(state=NORMAL)
def print_all_student():
    global current_page, panel
    print('print all student Clicked!')
    panel.destroy()
    if current_page != 3:
        lblHeader.config(text = "This is header of print all student")
        lblHeader.pack()
    current_page = 3
def search_student():
    global current_page, panel
    print('search student clicked!')
    panel.destroy()
    if current_page != 4:
        lblHeader.config(text = "This is header of Search student")
        lblHeader.pack()
    current_page = 4

#===== design
def bttnLeft(frame, display_text, function=""):
    return Button(
        frame,
        text = str(display_text),
        font = "Arial 12 bold",
        bg = "lightblue",
        height = 2,
        border=0,
        command= partial(function),
        anchor="w"
    )

#===== logic
name, age, id, email, phone = '','','','',''

def success():
    print(1)
    top_frame.pack(side='top', fill="x")
    left_frame.pack(side="left", fill="y")
    right_frame.pack(side="right", fill="both", expand=True)
    login_frame.pack_forget()
    main_menu()

def log_out():
    left_frame.pack_forget()
    right_frame.pack_forget()
    top_frame.pack_forget()
    panel.pack_forget()
    login_frame.pack(pady=300)

def validation():
    global name, age, id, email, phone
    #validating = MainMenu(addstud, printall, search)
    if True: #validating.login(txtUser.get()):
        #name, age, id, email, phone = validating.current_student
        success()
    else:
        print('wrong user')
    pass

def test():
    global name, age, id, email, phone
    print(name, age, id, email, phone)

#menu
bttnHome = bttnLeft(left_frame, "Home", main_menu)
bttnAdd = bttnLeft(left_frame, "Add student", add_student)
bttnPrnt = bttnLeft(left_frame, "Print All Sudent", print_all_student)
bttnSrch = bttnLeft(left_frame, "Seacrh Student", search_student)
bttnOut = bttnLeft(left_frame, "Log Out", log_out)
for i in [bttnHome,bttnAdd,bttnPrnt,bttnSrch,bttnOut]: i.pack(expand= True,fill='x',padx=20,)


#login
bttnLogin = Button(login_frame, text="Login", command=partial(validation))
txtUser = Entry(login_frame,width=50, text = 'Email')
txtPass = Entry(login_frame, width=50, show='*')
txtUser.pack()
txtPass.pack()
bttnLogin.pack() 



win.mainloop()