import time
from tkinter import *

date_format =  "%b %d, %Y"
large_text_size = 48
small_text_size = 18
class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')

        self.timeLbl = Label(self, font=('Helvetica', large_text_size), fg='white', bg='black')
        self.timeLbl.pack(side=TOP, anchor=E)

        self.day_of_week_Lbl = Label(self , font=('Helvetica', small_text_size), fg="white", bg="black")
        self.day_of_week_Lbl.pack(side=TOP, anchor=E)

        self.dateLbl = Label(self, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.dateLbl.pack(side=TOP, anchor=E)
        self.tick()

    def tick(self):
        temp_time = time.strftime('%I:%M:%S %p')
        temp_day_of_week = time.strftime('%A')
        date = time.strftime(date_format)

        self.timeLbl.config(text=temp_time)
        self.day_of_week_Lbl.config(text=temp_day_of_week)
        self.dateLbl.config(text=date)
        self.timeLbl.after(20, self.tick)
