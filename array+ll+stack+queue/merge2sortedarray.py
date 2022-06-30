#Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).

def merge_lists(lst1, lst2):
    ind1 = 0
    ind2 = 0
    while ind1 < len(lst1) and ind2 < len(lst2):
          if lst1[ind1] > lst2[ind2]:
             lst1.insert(ind1, lst2[ind2])
             ind1 += 1
             ind2 += 1
          else:
              ind1 += 1
    if ind2 < len(lst2):
        lst1.extend(lst2[ind2:])
    return lst1

list1 = [1,3,4,5]
list2 = [2,6,7,8]
print(merge_lists(list1, list2))