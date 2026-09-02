arr = [2,7,11,15]
target = 21/9
found = False
for i in range(len(arr)):
   for j in range(i+1,len(arr)):
    if arr[i] + arr[j]== target:
       print(i,j)
       found = True
if found == False :
  print("pair not found")