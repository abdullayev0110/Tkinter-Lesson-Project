from tkinter import *

root = Tk()
l1 = Label(root, text='Timer')
l2 = Label(root, text='COUNT')
count = 10
tmp = 0


def f():
    global count, tmp
    l1.config(text=count)
    root.after(1000, f)
    if count == 0:
        count = 10
        tmp += 1
        l2.config(text=tmp)
    else:
        count -= 1


l1.pack()
l2.pack()
f()
root.mainloop()
