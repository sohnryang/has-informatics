import tkinter as tk

window = tk.Tk()
button1 = tk.Button(window, text="Quit", fg="black", command=quit)
button1.pack()
window.mainloop()
