array = [10,20,30,30,40,40,50,20]

result = []
for num in array:
    if num not in result:
        result.append(num)
print(result)