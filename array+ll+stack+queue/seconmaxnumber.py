"FIRST APPROACH"
# def second_max_number(lst):
#     first_no = float("-inf")
#     second_no = float("-inf")
#     for i in lst:
#         if i > first_no:
#            first_no = i
#     for i in lst:
#         if i > second_no and i != first_no:
#             second_no = i
#     return second_no
#
# lst = [9,2,4,16]
#
# print(second_max_number(lst))

#iteraing in single for loop
def find_sec_max(lst):
    first_no = second_no = float("-inf")
    for i in range(len(lst)):
        if lst[i] > first_no:
            second_no = first_no
            first_no = lst[i]
        elif lst[i] != first_no and lst[i] > second_no:
            second_no = lst[i]
    return second_no

lst = [9,2,4,6]
print(find_sec_max(lst))

