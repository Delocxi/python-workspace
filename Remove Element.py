nums = [2,2,3,3]
val = 3

for i in range(len(nums)):
    if val in nums:
        nums.remove(val)
    else:
        lt = nums
        print(lt)
        break