import tkinter as tk

def a(e):
    b = 'Key {}, (code {}) pressed'.format(e.keysym, e.keycode)
    lvar.set(b)
    print(b)

root = tk.Tk()
root.title('Key event')
lvar = tk.StringVar()
lbl = tk.Label(root, text="kordinata", textvariable=lvar)
lbl.place(x=20, y=20)
root.bind('<Key>', a)
root.geometry("300x250+300+300")
root.mainloop()