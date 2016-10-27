
# coding: utf-8

# Generate a random number between 1 and 9 (including 1 and 9).
# 
# Ask the user to guess the number, then tell them whether 
# they guessed too low, too high, or exactly right.
# 
# Keep the game going until the user types “exit”.
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

# In[2]:

import random

random_num = random.randint(1,9)

counter = 0

while True:
    
    input_num = input("Please input your number : ")
    
    if input_num == "exit":
        break
        
    input_num_int = int(input_num)
    
    counter = counter + 1
    
    if input_num_int > random_num:
        print("Number is too high")
    elif input_num_int < random_num:
        print("Number is too low")
    else:
        print("Correct, you are win after", counter," try")
        break
        
    
    


# In[ ]:



