def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    while low <= high:
          mid = (low+high)//2
          if arr[mid] == target:
             return mid
          elif arr[mid] < target:
               low = low+1

          else:
               high = high-1
    return -1



arr = [1,3,9,10,12]
print(binary_search(arr, 100))