# Find largest number and its index

array = [10, 50, 20, 80, 30]

largest = array[0]
index = 0
for i in range(len(array)):
    if array[i] > largest:
        largest = array[i]
        index = i
print("largest number:",largest)
print("index:",index)