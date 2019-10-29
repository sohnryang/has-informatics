f = open('./fruit.txt')
s = f.readline().strip()
print(len(set(s.split(','))))
