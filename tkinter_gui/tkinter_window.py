import tkinter as tk

window = tk.Tk()
window.title('Hello, world!')
window.geometry("500x500")
label1 = tk.Label(window, text="Label 1")
label1.pack()
label2 = tk.Label(window, text="Label 2", fg="white", bg="black",
                  font=("Menlo", 30, "normal"))
label2.pack()
window.mainloop()
