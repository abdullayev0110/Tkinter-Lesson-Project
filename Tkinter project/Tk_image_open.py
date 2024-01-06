from tkinter import *
from PIL import Image, ImageTk
root = Tk()
img = Image.open('../ITpark_school/img.png')
img1 = Image.open('../ITpark_school/new.ico')
img = img.resize((400, 400))
img1.resize((400, 400))
imgTk = ImageTk.PhotoImage(img)
imgTk1 = ImageTk.PhotoImage(img1)
lb = Label(root,image=imgTk)
lb.pack()
root.mainloop()