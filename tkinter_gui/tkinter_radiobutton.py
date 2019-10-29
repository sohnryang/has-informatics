import tkinter as tk

def func():
    print(var.get())

window = tk.Tk()
window.geometry("500x500")
var = tk.IntVar()
rb1 = tk.Radiobutton(window, text="A", variable=var, value=1, command=func)
rb2 = tk.Radiobutton(window, text="B", variable=var, value=2, command=func)
rb3 = tk.Radiobutton(window, text="C", variable=var, value=3, command=func)
rb1.pack()
rb2.pack()
rb3.pack()
window.mainloop()
