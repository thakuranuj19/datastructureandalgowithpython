def right_rotate(lst, k):
    if len(lst) == 0:
        k= 0
    else:
        k = k % len(lst)
    return lst[-k:]+lst[:-k]


lst = [10,20,30,40,50]
k = 3
print(right_rotate(lst, abs(k)))