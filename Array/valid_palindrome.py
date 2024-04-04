# 125. Valid Palindrome
# Easy
# Topics
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: 
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 
# s = "a@"
# s= s.replace(",", "").lower()
# sn=s.replace(":"," ").lower()
# sn=sn.replace(" ","")

# sn=sn.replace(".","")
# pattern = r'[^a-zA-Z0-9\s]'  
# sn =sn.replace(pattern, '')
# # print(reversed)
# print(sn[::-1])
# if sn==sn[::-1]:
#     print("palin")
# print(sn)
# print(sn[::-1])



def isPalindrome(self, s):
        s = "".join(filter(lambda x : x in "qwertyuiopasdfghjklzxcvbnm1234567890", list(s.lower())))
        return s[::-1] == s
#This part filters out any characters in the input string s that are not alphanumeric. It converts the string to lowercase using lower() method and then filters out only those characters that are in the set of alphanumeric characters and numbers.
# "".join(...): After filtering, the remaining alphanumeric characters are joined back together into a string.