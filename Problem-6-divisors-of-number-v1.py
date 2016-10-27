
# coding: utf-8

# Problem 6 : Divisors
# 
# Input :
# User input number
# 
# Output :
# Prints out a list of all the divisors of that number.
# 
# Example divisors of 10 are : 1,2,5,10

# In[13]:

import math

input_num = input("Please input your number:")
input_num_int = int(input_num)

for number in range (1, int(math.sqrt(input_num_int)) + 1):
    if input_num_int % number == 0:
        if number != (input_num_int/number):
            print(number, int(input_num_int / number))
        else:
            print(number)


# In[ ]:



