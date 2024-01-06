import tkinter as tk
from datetime import datetime

def update_color():
    current_time = datetime.now().second
    if current_time % 3 == 0:
        label["bg"] = "red"
    elif current_time % 3 == 1:
        label["bg"] = "yellow"
    else:
        label["bg"] = "green"
    label.after(1000, update_color)

root = tk.Tk()

label = tk.Label(root, text="Svitafor", bg="red", fg="white", font=("Arial", 24), width=15, height=5)
label.pack()

root.after(0, update_color)

root.mainloop()