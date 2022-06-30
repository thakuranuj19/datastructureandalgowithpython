#Find Two Numbers that Add up to "k"

# In this problem, you have to implement the find_sum(lst,k) function which will take a number k as input and return two numbers that add up to k.

def find_sum(lst, sumval):
    foundvalue = set()
    for ele in lst:
        if (sumval-ele) in foundvalue:
            return (sumval-ele, ele)
        foundvalue.add(ele)
    return False


lst = [1,21,3,14,5,60,7,6]
k = 81

print(find_sum(lst,k))