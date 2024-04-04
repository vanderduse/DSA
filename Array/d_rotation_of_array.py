d=2
arr=[5,4,1,2,3]
n=len(arr)
temp=[]
for i in range(d,n):
    temp.append(arr[i])
newl=temp+arr[0:d]
print (newl)
