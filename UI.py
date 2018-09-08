from tkinter import *
from Clock import Clock
from GoogleTxt import GoogleTxt
from Weather import Weather, ForcastFrame

date_format =  "%b %d, %Y"
large_text_size = 48
small_text_size = 18

class Screen:
    def __init__(self):
        self.isFullscreen = True

        self.tk = Tk()
        self.tk.config(background='black')
        self.tk.attributes("-fullscreen", self.isFullscreen)


        self.topFrame = Frame(self.tk, background='black')
        self.bottomFrame = Frame(self.tk, background='black')
        self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)

        self.clock = Clock(self.topFrame)
        self.clock.pack(side=RIGHT, anchor=N, padx=100, pady=60)

        self.weather = Weather(self.topFrame)
        self.weather.pack(side=LEFT, anchor=N, padx=100, pady=60)

        self.googletext = GoogleTxt(self.bottomFrame)
        self.googletext.pack(side=RIGHT, anchor=S, padx=100, pady=30)


        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.isFullscreen = True
        self.tk.attributes("-fullscreen", self.isFullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.isFullscreen = False
        self.tk.attributes("-fullscreen", self.isFullscreen)
        return "break"
    
    def update_google_text(self, txt, prefix):
        self.googletext.addText(txt, prefix)
    
