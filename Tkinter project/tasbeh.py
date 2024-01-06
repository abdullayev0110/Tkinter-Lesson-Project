from tkinter import *

root = Tk()
root.geometry("400x400")
covert = ['Subhanalloh', 'Alhamdulillah', 'Allohuakbar']
count = 0
con = 1


def increment():
    global count, con
    count += 1
    if count == 34:
        count = 0
        lbCon.config(text=covert[con])
        con += 1
    if con == 3:
        con = 0

    lbCount.config(text=count)


lbCon = Label(root, text=covert[0], font=('times', 32))
lbCount = Label(root, text=count, font=('times', 32))
btnCount = Button(root, text="🕋", font=('times', 32), command=increment)

lbCon.pack(padx=60)
lbCount.pack(padx=60)
btnCount.pack(padx=60)

root.mainloop()
