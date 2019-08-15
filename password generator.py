from string import ascii_letters, digits
from random import choice
from tkinter import *
import pyperclip

symbols = ascii_letters + digits

root=Tk()
root.title = "Password Generator"
root.geometry("300x200")

pass_number = IntVar(root)
pass_number.set(0)

entry1 = Entry(text="enter the number", textvariable=pass_number, 
width=40)
entry1.place(x=25, y=70)
    
#Defing the password generator command
def button1_clicked():
    pas = ''
    for x in range(pass_number.get()):
        pas = pas + choice(symbols)
    entry1.delete(0, END)
    entry1.insert(0, pas)

button1 = Button(text="Generate parole", command=button1_clicked, 
width=25)
button1.place(x=25, y=90)

#Defining clipboard command
def button2_clicked():
    pyperclip.copy(entry1.get())
    
button2 = Button(text="copy", command=button2_clicked, height=1, width=7)
button2.place(x=210, y=90)
     
root.mainloop()
