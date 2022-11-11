
def intersect(nums1,nums2):

    nums = {}

    for i in nums1:
        if i in nums2:
            nums.add(i)

    return list(nums)