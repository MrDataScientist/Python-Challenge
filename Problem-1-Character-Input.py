
# coding: utf-8

# Problem 1 : Character input
# 
# Input
# User input their name and their age
# 
# Output
# Print a message to user that tells them the year that they will turn 100 years old.

# In[17]:

input_name = input("Pleae input your name :")

input_age = input("Pleae input your age :")

year_user_turn_100 = 2016 + (100 - int(input_age))

print (input_name + " will turn to 100 at " + str(year_user_turn_100))


# In[ ]:



