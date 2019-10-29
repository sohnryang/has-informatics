import tkinter as tk

def update():
    label.configure(text=ent.get())

window = tk.Tk()
window.geometry("500x500")
ent = tk.Entry(window)
label = tk.Label(window)
bt = tk.Button(window, text="Update", command=update)

ent.pack()
label.pack()
bt.pack()

window.mainloop()
