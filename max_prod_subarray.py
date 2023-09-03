#nums =[2,3,-2,4]
nums = [-2,0,-1,2, 10]
def maxProduct(nums):
    prod_now = float('-inf')

    prod_end = 1
    for i in range(len(nums)):
        prod_end = prod_end*nums[i]
        prod_simple = nums[i]
        print("now", prod_now)
        print("end", prod_end)
        print("текущее значение", prod_simple)

        if prod_end > prod_now and prod_end == 0 and prod_end >= prod_simple:
            prod_now = prod_end
            prod_end = 1
        elif prod_end > prod_now and prod_end == 0 and prod_end < prod_simple:
            prod_now = prod_simple
            prod_end = 1
        elif prod_end > prod_now and prod_end != 0 and prod_end >= prod_simple:
            prod_now = prod_end
        elif prod_end > prod_now and prod_end != 0 and prod_end < prod_simple:
            prod_now = prod_simple
        elif prod_end<prod_now and prod_end != 0 and prod_end < prod_simple:
            prod_now = prod_simple

    return f"результат {prod_now}"
print(maxProduct(nums))
