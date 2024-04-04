# 283. Move Zeroes
# Easy
# Topics
# Companies
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
nums = [0,1,0,3,12]

k=[]
n=[]
for i in range(0,len(nums)):
    if nums[i]!=0:
        k.append(nums[i])
        
    else :
        n.append(nums[i])
print (k+n)



# def mv(nums):
    