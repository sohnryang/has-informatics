def func1():
    num = 1
    print('func1: num = %d' % num)

def func2():
    global num
    num = 2
    print('func2: num = %d' % num)

num = 10
func1()
func2()
print('main: num = %d' % num)
