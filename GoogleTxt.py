from tkinter import *
small_text_size = 18
xsmall_text_size = 10
maximum_line_of_text = 10
maximum_ascii_char =65336
maximum_char_in_line = 50
class GoogleTxt(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.temp_text = False
        self.text_lbl = []
        for i in range(maximum_line_of_text):
            label = Label(self, pady=1, font=('Helvetica', xsmall_text_size), fg="white", bg="black")
            label.pack(anchor=W, pady=1)
            self.text_lbl.append(label)

    def addText(self, txt: str, prefix):
        new_txt = ''
        for j in range(len(txt)):
            if ord(txt[j]) in range(maximum_ascii_char):
                new_txt = new_txt + txt[j]
        #char_list = [txt[j] for j in range(len(txt)) if ord(txt[j]) in range(65536)]
        for line in new_txt.split('\n'):
            txt = ''
            for word in self.split_word(line):
                if len(txt+word) > maximum_char_in_line:
                    self.add_text_to_lbl(prefix + txt.strip())
                    txt = ''
                txt = txt + word
            if len(txt) > 0:
                self.add_text_to_lbl(prefix + txt.strip())

    def add_text_to_lbl(self, txt):
        for i in range(maximum_line_of_text):
            if i == maximum_line_of_text - 1:
                self.text_lbl[i].config(text=txt.strip())
            else:
                self.text_lbl[i].config(text=self.text_lbl[i+1]["text"])
                
    def split_word(self, s: str):
        lst = []
        break_char = [' ', ',', '\t', '.']
        word = ''
        for i in range(len(s)):
            word = word + s[i]
            if s[i] in break_char:
                lst.append(word)
                word = ""
        if len(word) > 0:
            lst.append(word)
        return lst