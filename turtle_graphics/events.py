import turtle as t

t.onkey(lambda: t.fd(200), 'w')
t.onkey(lambda: t.lt(90), 'a')
t.onkey(lambda: t.bk(200), 's')
t.onkey(lambda: t.rt(90), 'd')
t.onkey(lambda: t.home(), ' ')
t.listen()
t.mainloop()
