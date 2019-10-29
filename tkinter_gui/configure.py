import tkinter as tk

def func():
    if checked.get():
        label.configure(text="Checked")
    else:
        label.configure(text="Unchecked")

window = tk.Tk()
window.geometry("500x500")
checked = tk.BooleanVar()
checked.set(False)
checkbutton = tk.Checkbutton(window, text="Check", variable=checked, command=func, fg="black")
checkbutton.pack()
label = tk.Label(window, text="Undefined")
label.pack()
window.mainloop()
