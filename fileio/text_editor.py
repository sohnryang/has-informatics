with open('mydata.txt', 'w') as f:
    while True:
        line = input()
        if line:
            f.writelines(line + '\n')
        else:
            break
