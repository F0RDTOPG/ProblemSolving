def siglenumber(nums):
    res = 0
    for n in nums:
        res = n ^ res
    return res