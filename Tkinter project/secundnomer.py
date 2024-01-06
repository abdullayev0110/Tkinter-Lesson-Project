import datetime
from tkinter import *

root = Tk()
label = Label(root, font=('times', 24), bg='red', width=15)


def f():
    time = datetime.datetime.now()
    label.config(text=time.strftime("%H:%M:%S %p"))
    root.after(1000, f)


def createLabel():
    l = Label(root, font=('times', 24), text=datetime.datetime.now(), bg='white', width=15)
    l.pack()


btn = Button(root, text='Stop', font=('times', 24), width=15, command=createLabel)

label.pack()
btn.pack()
f()

root.mainloop()
