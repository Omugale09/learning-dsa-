#find smallest number
array = [10,50,20,80,30]

smallest=array[0]
index = 0

for i in range(len(array)):
    if array[i] < smallest:
       smallest = array[i] 
       index= i
print("smallest number:",smallest)
print("index:",index)