from tkinter import *
from functools import partial
from main import *
from PIL import Image, ImageTk

win = Tk()
win.title("Student System")
win.geometry(f'1280x720+{(win.winfo_screenwidth() - 1280) // 2}+{(win.winfo_screenheight() - 720) // 2}')
win.config(background='#252526')
#====== Frames
#login frame
login_frame = None
#login_frame.pack(pady = 300)
# top frame
top_frame = Frame(win, height= 50, background="#2d2d30")
top_frame.pack_propagate(False)
# Left Frame 30% of 1280 = 384
left_frame = Frame(win, bg="#1e1e1e", width=384)  
left_frame.pack_propagate(False)
# Right Frame (70% width)
right_frame = Frame(win, bg="#252526", width=896)
right_frame.pack_propagate(False)




#===== functions/pages
current_page = 0
panel = Frame(right_frame)
lpanel = Frame(left_frame)
log_info = []
def login():
    global login_frame, log_info
    try: panel.pack_forget()
    except: pass
    login_frame = Frame(win, bg="#2d2d30", padx=20, pady=20)
    log_info.extend([Label(login_frame,text="Login", font='Helvatica 16 bold', bg="#2d2d30", fg='white'),
                    Label(login_frame,text="ID Number", font='Arial 12 bold', bg="#2d2d30", fg='white'),
                    Entry(login_frame,width=30, font='Arial 12 bold'),
                    Button(login_frame, text="Login",font = 'Arial 12 bold',fg="white",bg="#4CAF50",activeforeground="white",activebackground="#45a049",  command=partial(validation,None))])
    log_info[3].configure(command = partial(validation, log_info[2]))    
    for i in range(len(log_info)): 
        log_info[i].pack()
    log_info[1].pack_configure(anchor = 'w')
    login_frame.place( relx=0.5, rely=0.5, anchor='center')
    
    
    
def main_menu():
    global name, age, id, email, phone, current_page, lpanel
    
    print('Main Menu Clicked!')
    try: panel.pack_forget()
    except: pass
    lpanel = Frame(left_frame, bg="#2d2d30", borderwidth=2, relief="ridge")
    lpanel.pack(padx=10, pady=10, fill="both", expand=True)

    lblHeader = Label(lpanel,text=f"Welcome, {name}!", font="Arial 20 bold", fg="white", bg="#4CAF50", pady=10)
    lblHeader.pack(fill="x", padx=5, pady=(0, 10))  # Add padding below

    profile = PhotoImage(file=r"media\blnk_profile.png")
    lblImage = Label(lpanel, image=profile, height=100, width=100, bg="white", borderwidth=2, relief="solid")
    lblImage.image = profile  # Prevent garbage collection
    lblImage.pack(pady=20)

    # Personal Details Section
    current_page = 1
    details = [f"Name: {name}", f"Age: {age}", f"ID: {id}", f"Email: {email}", f"Phone: {phone}"]

    Label(lpanel, text="Your Details", font="Arial 16 bold", bg="#4CAF50", fg="white", pady=5).pack(fill="x")

    for i, detail in enumerate(details):
        lbl = Label(lpanel, text=detail, font="Arial 12", fg="white", bg='#2d2d30', anchor="w", padx=10, pady=5)
        lbl.pack(fill="x")

    # Footer Separator
    Label(lpanel, text="", bg="#4CAF50", height=1).pack(fill="x", pady=(10, 0))
    lpanel.pack()

def add_student():
    global name, age, id, email, phone, current_page, panel
    print('Add_student Click ed!')
    panel.pack_forget()
    panel = Frame(right_frame)
    addstud.show_gui(panel, win)
    panel.place(relx=0.5, rely=0.5, anchor='center')
def print_all_student():
    global current_page, panel
    print('print all student Clicked!')
    panel.pack_forget()
    panel = Frame(right_frame)
    search.show_gui(panel,win)
    printall.show_gui(panel)
    panel.pack()

    
    


#===== design
def bttnLeft(frame, display_text, function=""):
    return Button(frame,text = str(display_text),font = "Arial 12 bold",bg = "lightblue",height = 2, border=0,command= partial(function),anchor="w")

#===== logic
name, age, id, email, phone = '','','','',''

def success():
    global login_frame, log_info
    log_info[2].delete(0,END)
    top_frame.pack(side='top', fill="x")
    
    right_frame.pack(side="left", fill="y", expand=True)
    left_frame.pack(side="right", fill="both")

    login_frame.place_forget()
    main_menu()
    add_student()

def log_out():

    left_frame.pack_forget()
    right_frame.pack_forget()
    top_frame.pack_forget()
    panel.pack_forget()
    lpanel.pack_forget()
    login_frame.place(relx=0.5, rely=0.5, anchor='center')

def validation(k):
    global name, age, id, email, phone
    validating = MainMenu(addstud, printall, search)
    if validating.login(k.get()):
        name, age, id, email, phone = validating.current_student
        success()
    else:print('wrong user')

def test():
    global name, age, id, email, phone
    print(name, age, id, email, phone)

#menu
bttns, func_bttn = ["Admin Student System","Register Student",'All Students','Logout'], [main_menu, add_student, print_all_student, log_out]


for bttn in range(len(bttns)): 
    command = None if bttn == 0 else partial(func_bttn[bttn])
    Button(top_frame, text=str(bttns[bttn]), height=2, padx=30, border=0, command=command, anchor="center",bg='#2d2d30',fg='white').grid(row=0, column=bttn)

#login
bttnLogin = Button(login_frame, text="Login", command=partial(validation))
txtUser = Entry(login_frame,width=50, text = 'Email')
txtPass = Entry(login_frame, width=50, show='*')
login()

win.bind("<KeyRelease>", lambda k: success() if k.keysym == "k" else None)
win.mainloop()
