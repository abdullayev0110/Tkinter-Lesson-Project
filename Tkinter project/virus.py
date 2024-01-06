from tkinter import *
import random

root = Tk()


def f():
    for i in range(1, 100):
        top = Toplevel()
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        width = random.randint(100, 400)
        height = random.randint(100, 400)
        top.geometry(f"{width}x{height}+{x}+{y}")
        Label(top, text='msg').pack()


btn = Button(root, text='MK', command=f)
btn.pack()
root.mainloop()
