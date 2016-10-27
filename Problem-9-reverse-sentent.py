
# coding: utf-8

# Problem 9 : Reverse sentent
# 
# Input
# 
# Asks the user for a long string containing multiple words. 
# 
# Output
# 
# Print back to the user the same string, except with the words in backwards order. 
# For example, say I type the string: "Hello World" 
# then I would see the string "World Hello"

# In[12]:

input_sentent = input("Please input your sentent:")

words = input_sentent.split()

reverted_sentent = ""
for word in reversed(words):
    reverted_sentent = reverted_sentent + word + " "
    
print(reverted_sentent)


# In[ ]:



