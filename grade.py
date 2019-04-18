score = int(input())
score //= 10
score = max(score, 5)
score = min(score, 9)
score -= 5
grade = ['F', 'D', 'C', 'B', 'A']
print(grade[score])
