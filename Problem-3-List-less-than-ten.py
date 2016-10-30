# coding: utf-8

# Problem 3 :List Less Than Ten
# 
# Input
# Take a list example :
# list_number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 
# Output
# prints out all the elements in the list that are less than 10.

# In[4]:

list_number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for item in list_number:
    if item < 10 :
        print (item)
