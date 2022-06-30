#Find Minimum Value in List

def minivalue(lst):
    if len(lst) is None:
        return "Not found"
    try:
        minimum = lst[0]
        for ele in lst:
            if ele < minimum:
                minimum = ele
        return minimum
    except Exception as e:
        raise e

lst = []
print(minivalue(lst))