nums1 = [-45, 120, 56, 3, 34, 8, 12, 45, 1]
nums2 = [2.4, 20, 5.6, -3, 34, 8, -12, 45, -19.7]


def minimum(incomelist):
    min_number = incomelist[0]
    for number in incomelist:
        if number < min_number:
            min_number = number
    return min_number


print(minimum(nums1))
print(minimum(nums2))
