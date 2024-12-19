from tkinter import *

class PrintAllStudent:
    def __init__(self, student_data):
        self.student_data = student_data

    def print_all_students(self):
        print("==========================ALL STUDENT INFORMATION==============================")
        for student in self.student_data.allstudents:
            print(f"\nName: {student[0]}")  
            print(f"Age: {student[1]}")   
            print(f"ID Number: {student[2]}")  
            print(f"Email: {student[3]}")  
            print(f"Phone Number: {student[4]}")  
        print("==========================NOTHING FOLLOWS==============================")

    def show_gui(self, panel):
        panel.config(bg = '#2d2d30')
        # Define column headers
        headers = ['Name', 'Age', 'ID', 'Email', 'Phone']

        # Add a title for the table
        Label(panel, text="Student Information", font="Arial 20 bold", bg="#333", fg="white", pady=10).pack(fill="x")

        # Create a frame for the table with a stylish border
        table_frame = Frame(panel, bg="white", borderwidth=2, relief="ridge")
        table_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Create a frame to hold the canvas and scrollbars
        scroll_frame = Frame(table_frame)
        scroll_frame.pack(fill="both", expand=True)

        # Create canvas and scrollbars
        canvas = Canvas(scroll_frame)
        v_scrollbar = Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
        h_scrollbar = Scrollbar(scroll_frame, orient="horizontal", command=canvas.xview)

        # Configure canvas
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Pack scrollbars and canvas
        v_scrollbar.pack(side="right", fill="y")
        h_scrollbar.pack(side="bottom", fill="x")
        canvas.pack(side="left", fill="both", expand=True)

        # Create another frame inside the canvas
        inner_frame = Frame(canvas)

        # Set specific widths for each column
        column_widths = [200, 50, 100, 200, 150]  # Adjust these values as needed
        for col, width in enumerate(column_widths):
            inner_frame.grid_columnconfigure(col, minsize=width)

        # Add that new frame to a window in the canvas
        canvas_window = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        # Display column headers
        for col in range(len(headers)):
            Label(inner_frame, text=headers[col], font="Arial 13 bold", bg="#4CAF50", fg="white", 
                padx=10, pady=5, borderwidth=1, relief="solid", width=column_widths[col]).grid(row=0, column=col, sticky="nsew")

        # Display student data with alternating row colors
        for row in range(len(self.student_data.allstudents)):
            bg_color = "#2d2d30" if row % 2 == 0 else "#3a3a3d"  # Alternating row colors
            for col in range(len(headers)):
                Label(inner_frame, text=self.student_data.allstudents[row][col], font="Arial 12", 
                    bg=bg_color, fg="white", padx=10, pady=5, borderwidth=1, relief="solid", width=column_widths[col]).grid(row=row+1, column=col, sticky="nsew")

        # Adjust column weight for uniform spacing
        for col in range(len(headers)):
            inner_frame.grid_columnconfigure(col, weight=1)

        def update_scrollregion(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(canvas_window, width=max(event.width, sum(column_widths)))

        canvas.bind('<Configure>', update_scrollregion)

        panel.pack(fill="both", expand=True)

