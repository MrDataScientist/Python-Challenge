
# coding: utf-8

# Problem 4 : List Overlap
# 
# Input
# 
# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# 
# Output
# 
# Print out list that contains only the elements that are 
# common between the lists (without duplicates).

# In[9]:

a = [1, 1, 2, 3, 5, 8, 13, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a_with_out_duplicate = set(a)
b_with_out_duplicate = set(b)

result = []

for item in a_with_out_duplicate:
    if item in b_with_out_duplicate:
        result.append(item)

print(result)


# In[ ]:



