import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
checked = tk.IntVar()
checkbutton = tk.Checkbutton(window, text="Check", variable=checked, command=lambda: print(checked.get()))
checkbutton.pack()
window.mainloop()
