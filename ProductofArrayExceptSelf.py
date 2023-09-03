nums = [-1,1,0,-3,3]




def productExceptSelf(nums):
    from functools import reduce

    res_lst = []
    if nums.count(0) == 0:
        total_prod = reduce(lambda a, b: a * b, nums)
        for i in range(len(nums)):
            res_lst.append(int((total_prod/nums[i])))
        return res_lst
    elif nums.count(0) == 1:
        nums_copy = nums.copy()
        nums_copy.remove(0)
        total_prod = reduce(lambda a, b: a * b, nums_copy)
        for i in range(len(nums)):
            if nums[i] != 0:
                res_lst.append(0)
            elif nums[i] == 0:
                res_lst.append(total_prod)
        return res_lst
    else:
        for i in range(len(nums)):
            res_lst.append(0)
        return res_lst


print(productExceptSelf(nums))




