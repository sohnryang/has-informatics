temp = 0
max_temp = 0
min_temp = 0
result = [0, 987654321]

for i in range(1, 11):
	temp = int(input())
	if i == 1:
		max_temp = int(input())
		min_temp = int(input())
	if temp > max_temp:
		max_temp = temp
	if temp < min_temp:
		min_temp = temp
	result[0] = max(result[0], max_temp)
	result[1] = min(result[1], min_temp)
print(result[0], result[1])