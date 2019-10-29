import tkinter as tk

def func(event):
    print(event)

window = tk.Tk()
window.bind("<space>", func)
window.mainloop()
