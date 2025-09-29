def twoSum(nums, target):
    for i, val in enumerate(nums):
        a = nums[:i] + [None] + nums[i+1:]
        k = target - val
        if k in a:
            return i, a.index(k)
