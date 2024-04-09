# s = "(*))"
# stack = 0
# for i in s:
#     if i == '(':
#         stack += 1
#     elif i == ')':
#         stack -= 1
#     elif stack == -1 and '*' in s:
#         stack += 1
#     elif stack == 1 and '*' in s:
#         stack -= 1

# print(stack)
# if stack == 0:
#     print("true")
# else:
#     print("false")
def isValid(s):
    stack = 0  # Counter for unmatched left parentheses
    min_stack = 0  # Minimum possible number of unmatched left parentheses
    max_stack = 0  # Maximum possible number of unmatched left parentheses
    
    for char in s:
        if char == '(':
            stack += 1
            min_stack += 1
            max_stack += 1
        elif char == ')':
            if stack > 0:
                stack -= 1
            min_stack = max(min_stack - 1, 0)  # Treat '*' as empty if needed
            if max_stack > 0:
                max_stack -= 1
            else:
                return False  # More ')' than '(' and '*' combined
        elif char == '*':
            if stack > 0:
                stack -= 1
            min_stack = max(min_stack - 1, 0)  # Treat '*' as empty if needed
            max_stack += 1  # Treat '*' as '('
    
    return min_stack == 0

# Test cases
print(isValid("(((((()*)(*)*))())())(()())())))((**)))))(()())()"))  # Output: false
