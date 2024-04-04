# 39. Combination Sum
# Medium
# Topics
# Companies
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []



#this code works but time exceeds
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         from itertools import combinations
#         result=[]
#         from itertools import combinations_with_replacement
        
#         for r in range(1, target + 1):
#             for combo in combinations_with_replacement(candidates, r):
#                 if sum(combo) == target:
#                     result.append(combo)
#         return result

# candidates = [2, 3, 5]
# target = 8
# print(combinationSum(candidates, target))
    

candidates = [2, 3, 5]
target = 8
    
#perfected code using backtracking
def combinationSum(self,candidates, target):
        def backtrack(start, path, target):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                backtrack(i, path + [candidates[i]], target - candidates[i])

        result = []
        candidates.sort()
        backtrack(0, [], target)
        return result


    
    # print(combinationSum(candidates, target))