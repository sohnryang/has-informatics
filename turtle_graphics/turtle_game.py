import turtle as t

def reset_screen():
    t.clear()
    t.pu()
    t.home()
    t.pd()

t.onscreenclick(lambda x, y: t.goto(x, y))
t.mainloop()
