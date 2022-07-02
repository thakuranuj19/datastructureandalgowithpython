#Rearrange Positive & Negative Values

def rearrange_neg_right_side(lst):
    leftmost = 0
    for current in range(len(lst)):
        if lst[current] < 0:
            if current != leftmost:
                lst[current], lst[leftmost] =  lst[leftmost], lst[current]
            leftmost += 1
    return lst

print(rearrange_neg_right_side([10, -1, 20, 4, 5, -9, -6]))
