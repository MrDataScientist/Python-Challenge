
# coding: utf-8

# Ask the user for a number and determine whether the number is prime or not.

# In[3]:

import math

def get_all_divisors(input_number_int):
    
    result = []
    
    for number in range(1, int(math.sqrt(input_number_int)) + 1):
        if input_number_int % number == 0:
            #check if 2 divisor is same
            if number != input_number_int/number:
                result.append(number)
                result.append(int(input_number_int / number))
                print(number, int(input_number_int / number))
            else:
                result.append(number)
                print(number)
                
    return result

input_number = input("Please input your number :")
input_number_int = int(input_number)

list_divisors = get_all_divisors(input_number_int)

if len(list_divisors) == 2:
    print(input_number + " is prime")
else:
    print(input_number + " is not a prime")


# In[ ]:



