from tkinter import *
from tkinter import ttk
from component import color
from component import font
import random

bronzeCorrection = []
bronzeLogic = []
bronzeClass = []

silverCorrection = []
silverLogic = []
silverClass = []

goldLogic = []
goldClass = []

class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Frab10 extra exam")
        self.geometry("1512x982+100+10")
        self.config(bg=color.Color.beige)

        self.show_first_page()

    def show_first_page(self):
        self.page1 = Page1(self)
        self.page1.pack(fill="both", expand=True)

    def show_second_page(self, student_id):
        self.page1.destroy()
        self.page2 = Page2(self, student_id)
        self.page2.pack(fill="both", expand=True)

    def show_third_page(self, student_id):
        self.page2.destroy()
        self.page3 = Page3(self, student_id)
        self.page3.pack(fill="both", expand=True)

class Page1(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg=color.Color.beige)

        self.myLabel = Label(self, text="Please enter student ID", fg=color.Color.navy, bg=color.Color.beige, font=font.Text.Header)
        self.myLabel.pack(pady=(300,15))

        self.myLabel = Label(self, text="'YYNN' ex. 6680", fg=color.Color.peri, bg=color.Color.beige, font=font.Text.form)
        self.myLabel.pack(pady=15)

        self.entry = Entry(self, width=40, font=font.Text.form, bg="white", justify="center", fg=color.Color.peri)
        self.entry.pack(pady=15)

        self.myLabel = Label(self, text="Please ensure your ID is correct. After pressing 'Enter', this ID will be officially recorded as having taken the exam.", fg=color.Color.red, bg=color.Color.beige, font=font.Text.warn, wraplength=350)
        self.myLabel.pack(pady=15)

        self.button = Button(self, text="Enter", bg=color.Color.peri, fg="white", width=10, font=font.Text.buttontext, command=self.on_enter)
        self.button.pack(pady=15)

    def on_enter(self):
        student_id = self.entry.get()
        if student_id:
            self.master.show_second_page(student_id)

class Page2(Frame):
    def __init__(self, parent, student_id):
        Frame.__init__(self, parent, bg=color.Color.beige)

        self.label = Label(self, text=f"Welcome: {student_id}", font=font.Text.Header, bg=color.Color.beige, fg=color.Color.navy)
        self.label.pack(pady=(50,0), padx=50, anchor="nw")

        self.canvas = Canvas(self, bg=color.Color.beige, highlightthickness=0, width=1512)
        self.canvas.create_line(50, 30, 1462, 30, fill=color.Color.navy, width=2)
        self.canvas.pack(pady=(0, 0), anchor="nw")

        self.myLabel = Label(self, text="How to take an exam", fg=color.Color.navy, bg=color.Color.beige, font=font.Text.form)
        self.myLabel.pack(pady=(0,10))
        self.myLabel = Label(self, text="1. Choose your topic carefully because each topic can only be selected once per day.", fg=color.Color.peri, bg=color.Color.beige, font=font.Text.topic)
        self.myLabel.pack(pady=(10,10))
        self.myLabel = Label(self, text="2. Please don't close this program before you finish the exam because the TA will be mad at you. \n (Just kidding, but please don't close this program before you finish the exam.).", fg=color.Color.peri, bg=color.Color.beige, font=font.Text.topic)
        self.myLabel.pack(pady=(10,10))
        self.myLabel = Label(self, text="3. Once you click the button, the link to the exam you chose will automatically copy.", fg=color.Color.peri, bg=color.Color.beige, font=font.Text.topic)
        self.myLabel.pack(pady=(10,30))

        self.next_button = Button(self, text="Next", bg=color.Color.peri, fg="white", width=10, font=font.Text.buttontext, command=self.next_to_page3)
        self.next_button.pack(pady=10)


    def next_to_page3(self):
        student_id = self.label.cget("text").split(":")[1].strip()
        self.master.show_third_page(student_id)

class Page3(Frame):
    def __init__(self, parent, student_id):
        Frame.__init__(self, parent, bg=color.Color.beige)

        self.label = Label(self, text=f"Student ID : {student_id}", font=font.Text.Header, bg=color.Color.beige, fg=color.Color.navy)
        self.label.grid(row=0, column=2, columnspan=4, padx=0, pady=(50, 0), sticky="w")

        topics = ["", "Bronze", "Silver", "Gold"] 
        topics2 = ["Code Correction", "Logic / Algorithm", "OOP"]
        cc = ""

        for i, topic in enumerate(topics):
            if(topic == "Bronze"): cc = "#B67F60"
            elif(topic == "Silver"): cc = "#9C9C9C"
            elif(topic == "Gold"): cc = "#D9B060"
            else : cc = color.Color.beige
            label = Label(self, text=topic, bg=cc, fg=color.Color.white, font=font.Text.topic, width=10)
            label.grid(row=1, column=i+1, padx=20, pady=20)

        for i, topic in enumerate(topics2):
            label = Label(self, text=topic, bg=color.Color.white, fg=color.Color.navy, font=font.Text.topic, wraplength=100, width=10)
            label.grid(row=i+2, column=1, padx=20, pady=20)

        self.buttons = []

        for i in range(1, 5):
            buttons_row = []
            for j in range(1, 5):
                if i == 2 and j == 4:
                    continue
                if j == 2:
                    button_text = "3"
                elif j == 3:
                    button_text = "5"
                elif j == 4:
                    button_text = "10"
                if i != 1 and j != 1:
                    button = Button(self, text=button_text, bg=color.Color.peri, fg="white", width=10, font=font.Text.buttontext)
                    button.grid(row=i, column=j, padx=10, pady=10)
                    button.config(command=lambda r=i, c=j: self.hide_buttons_in_row_except_clicked(r, c))
                    buttons_row.append(button)
            self.buttons.append(buttons_row)

        self.label = Label(self, text="Special (Platinum) 20 pts. Please ask Professor or TA", font=font.Text.buttontext, bg=color.Color.white, fg=color.Color.teal)
        self.label.grid(row=6, column=1, columnspan=4, padx=100, pady=(20, 0), sticky="w")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_columnconfigure(7, weight=1)

    def hide_buttons_in_row_except_clicked(self, row, column):
        if row == 2 and column == 2:
            lk = bronzeCorrection[random.randint(0, len(bronzeCorrection)-1)]
            bronzeCorrection.clear()
            bronzeCorrection.append(str(lk))
        if row == 3 and column == 2:
            lk = bronzeLogic[random.randint(0, len(bronzeLogic)-1)]
            bronzeLogic.clear()
            bronzeLogic.append(str(lk))
        if row == 4 and column == 2:
            lk = bronzeClass[random.randint(0, len(bronzeClass)-1)]
            bronzeClass.clear()
            bronzeClass.append(str(lk))

        if row == 2 and column == 3:
            lk = silverCorrection[random.randint(0, len(silverCorrection)-1)]
            silverCorrection.clear()
            silverCorrection.append(str(lk))
        if row == 3 and column == 3:
            lk = silverLogic[random.randint(0, len(silverLogic)-1)]
            silverLogic.clear()
            silverLogic.append(str(lk))
        if row == 4 and column == 3:
            lk = silverClass[random.randint(0, len(silverClass)-1)]
            silverClass.clear()
            silverClass.append(str(lk))
        
        if row == 3 and column == 4:
            lk = goldLogic[random.randint(0, len(goldLogic)-1)]
            goldLogic.clear()
            goldLogic.append(str(lk))
        if row == 4 and column == 4:
            lk = goldClass[random.randint(0, len(goldClass)-1)]
            goldClass.clear()
            goldClass.append(str(lk))

        self.clipboard_clear()
        self.clipboard_append(lk)
        self.label.config(text=f"{lk} \n ' link copied to clipboard! '")
        self.label.grid(row=6, column=2, columnspan=4, padx=100, pady=(20, 0), sticky="w")

        for j in range(2, 5):
            if j != column:
                self.buttons[row - 1][j - 2].grid_forget() 

                
if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
