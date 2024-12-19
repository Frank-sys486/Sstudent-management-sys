from tkinter import Tk, Frame, Label, Entry, Button
from functools import partial

# Validation function (dummy for this example)
def validation(entry):
    print(f"ID Number entered: {entry.get()}")

# Forget the login frame
def forget_login_frame():
    global login_frame
    if login_frame:
        login_frame.place_forget()  # Hides the login frame

# Show the login frame again
def show_login_frame():
    global login_frame
    if login_frame:
        login_frame.place(relx=0.5, rely=0.5, anchor='center')  # Brings back the frame

# Create the login form
def login():
    global login_frame
    # Create the login frame
    login_frame = Frame(win, bg="#ffffff", padx=20, pady=20)
    login_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Create widgets
    log_info = [
        Label(login_frame, text="Login", font='Helvetica 16 bold', bg="#ffffff", fg='#333'),
        Label(login_frame, text="ID Number", font='Arial 12 bold', bg="#ffffff", fg='#333'),
        Entry(login_frame, width=30, font='Arial 12 bold'),
        Button(
            login_frame, text="Login", font='Arial 12 bold', fg="white", bg="#4CAF50",
            activeforeground="white", activebackground="#45a049",
            command=partial(validation, None)  # Pass the entry widget to validation
        )
    ]

    # Configure and display widgets
    for i in range(len(log_info)):
        log_info[i].pack(pady=5 if i > 0 else 10)  # Add spacing between widgets

    log_info[1].pack_configure(anchor='w')  # Align "ID Number" label to the left


# Main application window
win = Tk()
win.title("Login Example")
win.geometry("400x300")
win.configure(bg="#f2f2f2")  # Light gray background

# Create buttons to toggle frames
toggle_frame = Frame(win, bg="#f2f2f2", pady=10)
toggle_frame.pack()

show_button = Button(toggle_frame, text="Show Login", command=show_login_frame)
show_button.pack(side="left", padx=10)

hide_button = Button(toggle_frame, text="Hide Login", command=forget_login_frame)
hide_button.pack(side="left", padx=10)

# Initialize the login form
login()

# Run the application
win.mainloop()
