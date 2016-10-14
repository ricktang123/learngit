#!/usr/bin/env python
from Tkinter import *
def anti_vowel(text):
    textnew=''
    for i in text:
        if not (i=='a' or i=='e' or i=='o' or i=='u' or i=='i'):
            textnew=textnew+i
    return textnew

print anti_vowel('please')

top= Tk()
label=Label(top, text="Welcome to TA")
label.pack()

button = Button(top, text="Quit", command=top.quit, bg='yellow', fg='red')
button.pack()

frm =  Frame(top)
#left
frm_L = Frame(frm)
Label(frm, text='Left is good').pack(side=TOP)
#frm_L.pack()
frm.pack()
var=StringVar()
e=Entry(top,textvariable=var)
var.set('Test is a test')
e.pack()


top.mainloop()
