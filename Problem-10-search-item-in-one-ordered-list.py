
# coding: utf-8

# Input
# Odered list, example [1,2,3,4,5,6,7,8,9,10]
# Ask user for a number.
# 
# Output
# Print out message to show if number exist in list or not

# In[ ]:

input_num = input("Please input your number : ")
list_num = [1,2,3,4,5,6,7,8,9,10]

head = 0

tail = len(list_num) - 1

while True:
    
    middle = int((head + tail)/2)
    
    print("head: ", head)
    print("middle: ", middle)
    print("tail: ", tail)
    print("\n")
    
    if head > tail:
        print("not found")
        break
    
    if list_num[middle] == int(input_num):
        print("found")
        break
    elif list_num[middle] > int(input_num):
        tail = middle - 1
    else:
        head = middle + 1

    


# In[ ]:



