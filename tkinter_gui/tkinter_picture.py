import tkinter as tk

window = tk.Tk()
photo = tk.PhotoImage(file="laplacian-profile-photo.png")
label = tk.Label(window, image=photo)
label.pack()
