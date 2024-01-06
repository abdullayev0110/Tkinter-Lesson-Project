from tkinter import *
from tkinter.messagebox import askyesnocancel

root = Tk()


def e():
    for i in range(1, 101):
        a = askyesnocancel('Virus', 'This is a virus')
        print(a)


btn = Button(root, text='click', command=e)
btn.pack()

root.mainloop()
