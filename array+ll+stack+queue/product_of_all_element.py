#Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.

#i/p: [1,2,3,4]
# arr = [24,12,8,6]

def find_product(lst):
    left = 1
    prod = []
    for ele in lst:
        prod.append(left)
        left = left*ele
    right = 1
    for i in range(len(lst)-1, -1, -1):
        prod[i] = prod[i] * right
        right = right * lst[i]
    return prod

lst = [1,2,3,4]
print(find_product(lst))