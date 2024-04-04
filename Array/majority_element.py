nums = [-1,2,2,1,1,1,2,2,1,1,2,2]
# n=nums.__len__()

# numss=max(nums)
# numba=min(nums)
# z=[]

# print(z)
# print(numss)
# if nums.count(numss)>(n/2):n

#     print("majority",numss)
# elif nums[i]not in numss and numba:
#     print(nums[i])
# else:
#     print(numba,"majority")
# for i in range(1,n):
#     if nums.count(numss)>n/2:
#         print("majority",numss)
#         break
    
#     else:
#         print (numba)

from collections import Counter
n=Counter(nums)
print(nums)
a=n.most_common()
print(a[0][0])

