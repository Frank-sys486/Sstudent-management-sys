from functools import partial; from tkinter import *; win = Tk()
result = Label(win, text="0", width=15, font=("Segoe Print", 29), bg="#212f3d", fg="white", anchor="e")
result.grid(row=0, column=0, columnspan=4, rowspan=1, sticky="ew")
row_num, column_num = 1, 0
buttons = ["^", "//", "mod", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "x", ".", "0", "=", "÷"]
operators = ["+", "-", "x", "÷", "//", "^", "mod"]
def paa(x):
    text = result.cget("text")
    if x == "C": result.config(text="0")
    elif x == "=":
        try: result.config(text=str(eval(text.replace("^", "**").replace("x", "*").replace("mod","%").replace("÷","/"))))
        except: result.config(text="Error")
    else:
        if text == "0" or text == "Error": text = " "
        if any(text.endswith(op) for op in operators) and x in operators:
            for op in operators:
                if text.endswith(op): text = text[:-len(op)]
            text += x
        else: result.config(text=text + x)
for i in range(len(buttons)):
    Button(win, text=buttons[i], width=6, height=2, font=("Gothic Century", 19), command=partial(paa, buttons[i]), bg="#2c3e50", fg="white").grid(row=row_num, column=column_num)
    column_num += 1
    if column_num == 4: row_num += 1; column_num = 0
win.config(bg="#212f3d"); win.geometry(f"400x460+{int(win.winfo_screenwidth()/2 - 400/2)}+{int(win.winfo_screenheight()/2 - 460/2)}"); win.title("Riman's Calculator"); win.mainloop()
