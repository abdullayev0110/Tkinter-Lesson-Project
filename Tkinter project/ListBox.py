# from Tkinter import Listbox
#
# from Tkinter import *
# root = Tk()
# listbox = Listbox(root, width=20, font=('times', 24))
# listbox.insert(0, 'Apple')
# listbox.insert(1, 'Banana')
# listbox.insert(2, 'Cherry')
# listbox.insert(3, 'Mango')
# listbox.insert(4, 'Kivi')
# listbox.pack()
#
# root.mainloop()


# from Tkinter import *
# root = Tk()
# data = ['apple', 'banana', 'cherry', 'mango', 'kivi', 'orange']
# listbox = Listbox(root, width=20, font=('times', 24))
# for i in data:
#     listbox.insert(data.index(i), i)
# listbox.pack()
#
# root.mainloop()


# from Tkinter import *
# root = Tk()
# data = ['apple', 'banana', 'cherry', 'mango', 'kivi', 'orange']
# listbox = Listbox(root, width=20, font=('times', 24))
# btn = Button(root, text='Submit', width=20, font=('times', 24),
#              command=lambda: print(listbox.curselection()[0]))
# for i in data:
#     listbox.insert(data.index(i), i)
# listbox.pack()
# btn.pack()
#
# root.mainloop()


# from Tkinter import *
# root = Tk()
# data = ['apple', 'banana', 'cherry', 'mango', 'kivi', 'orange']
# listbox = Listbox(root, width=20, font=('times', 24))
# btn = Button(root, text='Submit', width=20, font=('times', 24),
#              command=lambda: print(listbox.curselection()[0]))
# btn_delete = Button(root, text='Delete', width=20, font=('times', 24),
#              command=lambda: listbox.delete(listbox.curselection()[0]))
# for i in data:
#     listbox.insert(data.index(i), i)
# listbox.pack()
# btn.pack()
# btn_delete.pack()
#
# root.mainloop()

from tkinter import *
root = Tk()
data = ['apple', 'banana', 'cherry', 'mango', 'kivi', 'orange']
listbox = Listbox(root, width=20, font=('times', 24))
for i in data:
    listbox.insert(data.index(i), i)
listbox.pack()

root.mainloop()