
# coding: utf-8

# Problem 5 : Check palindrome
# 
# Input
# Ask the user for a string 
# 
# Output
# Print out message whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
# Example : radar

# In[9]:

input_string = input("Please input your word:")

reverted_string = input_string[::-1]

if reverted_string == input_string:
    print(input_string + " is palindrome")
else:
    print(input_string + " is not palindrome")


# In[ ]:



