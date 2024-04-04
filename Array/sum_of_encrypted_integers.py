# nums=[10,21,31]
# newarr=[]
# res=[]
# for i in range (len(nums)):
#     x=list(map(int,str(nums[i])))
    
#     # print(x)
#     add=[max(x)]
#     print(add)
#     for i in range (nums):
#         res=res.append(add[i]+nums[i])
#     print (res)
    # print(type(add),type(nums))
    # res=nums[i]+add[i]

    # for i in range(len(x)):
    #     max_x=max(x[i])
    # print (max_x)
    # add=nums[i]+x
    # newarr.append(add)
    # print(newarr)

nums = [10, 21, 31]
newarr = []

# Iterate through each number in nums
for num in nums:
    # Convert the number to a list of its digits
    digits = list(map(int, str(num)))
    print (digits)
    
    # Find the maximum digit
    max_digit = max(digits)
    print(max_digit)
    
    # Create a new number with all digits being the maximum digit
    new_num = int(str(max_digit) * len(digits))
    print (new_num)
    
    # Append the new number to newarr
    newarr.append(new_num)
    print(sum(newarr),"here AGAYA ANSWER BHAI BEHENCHOD ")


