import os

if os.path.exists('data3.txt'):
    in_file = open('data1.txt')
    lines = in_file.readlines()
    print(lines)
    in_file.close()
else:
    print('File does not exist')
