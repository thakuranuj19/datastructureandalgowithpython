def reverse_array(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate_array(nums, n):
    length = len(nums)

    n = n%length
    if n<0:
        n += length
    
    reverse_array(nums, 0, length-1)

    reverse_array(nums, 0, n-1)

    reverse_array(nums, n, length-1)

    return nums



def main():
    arr = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
    print("Array Before Rotation")
    print(arr)

    nums = rotate_array(arr, 2)
    print("Array After 2 Rotations")
    print(nums)


if __name__ == '__main__':
    main()