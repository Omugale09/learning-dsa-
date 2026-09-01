array = [0, 5, 0, 10, 20, 0]
result = []
for num in array:
    if num != 0:
        result.append(num)

for num in array:
    if num == 0:
        result.append(num)
print(result)