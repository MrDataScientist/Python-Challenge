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

# In[5]:

import math

input_number = input("Please input your number :")

input_number_int = int(input_number)

for number in range(1, int(math.sqrt(input_number_int)) + 1):
    if input_number_int % number == 0:
        #check if 2 divisor is same
        if number != input_number_int/number:
            print(number, int(input_number_int / number))
        else:
            print(number)
