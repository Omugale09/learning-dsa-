arr = [10,50,80,40,10]
largest = arr[0]
smallest=arr[0]
index1= 0 
index2= 0
for i in range(len(arr)):
    if arr[i] > largest:
     largest = arr[i]
     index1 =i
    
    if arr[i]<smallest:
       smallest=arr[i]
       index2 =i
    count=0
for i in arr:
   if i==smallest:
    count+=1
print("largest number:",largest)
print("index:",index1)

print("smallest number:",smallest)
print("index:",index2)

print("count:",count)