# 2444. Count Subarrays With Fixed Bounds
# Hard
# Topics
# Companies
# Hint
# You are given an integer array nums and two integers minK and maxK.

# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
# Example 2:

# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
# from numpy import unique
# import numpy as np
num = [1,1,1,1]
mink = 1
maxk = 1
l = []

# for num in num1:
#     if num >= mink and num <= maxk:
#         l.append(num)
# l=unique(l)
# # l=set(l)
# print(l)



##the solution works but not for num = [1,1,1,1]mink = 1maxk = 1
# def minarray(num,maxk,mink):
#     count=0
#     for start in range (len(num)):
#         for end in range(len(num)):
#             subarr=num[start:end+1]
#         if min(subarr)==mink or max(subarr)==maxk:
#             count=count+1
#     return count
# print(minarray(num,mink,maxk))

def count_fixed_bound_subarrays(nums, minK, maxK):
    return count_subarrays_max(nums, maxK) - count_subarrays_max(nums, minK - 1)

def count_subarrays_max(nums, max_val):
    count = 0
    current_count = 0

    for num in nums:
        if num <= max_val:
            current_count += 1
        else:
            current_count = 0
        count += current_count

    return count

nums = [1,1,1,1]
minK = 1
maxK = 1
print(count_fixed_bound_subarrays(nums, minK, maxK))
