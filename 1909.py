# def check_increa(nums):
#     i = 0
#     diff = float('-inf')
#     x = True
#
#     while x:
#         if nums[i] < diff :
#             nums.remove(diff)
#             x = False
#         elif nums[i]> diff or nums[i] == diff:
#             diff = nums[i]
#             i += 1
#             if i == len(nums):
#                 x = False
#
#     while i < len(nums):
#         if nums[i] < diff or nums[i] == diff:
#             return False
#         else:
#             diff = nums[i]
#             i += 1
#
#     return True
#
#
# nums = [1, 1, 1]
# print(check_increa(nums))





# def check_increa(nums):
#     i = 0
#     diff = float('-inf')
#     x = True
#
#     while i < len(nums) and x:
#         if nums[i] < diff:
#             nums.remove(diff)
#             x = False
#         else:
#             diff = nums[i]
#             i += 1
#
#     while i < len(nums):
#         if nums[i] <= diff:
#             return False
#         diff = nums[i]
#         i += 1
#
#     return True
#
#
# nums = [1, 1, 1, 2]
# print(check_increa(nums))




def check_increa(nums):
    i = 0
    diff = float('-inf')
    x = True

    while x:
        if nums[i] < diff:
            nums.remove(diff)
            x = False
        elif nums[i] >= diff:
            diff = nums[i]
            i += 1
            if i == len(nums):
                x = False

    if i < len(nums) and (nums[i] <= diff or (i > 1 and nums[i] <= nums[i - 2])):
        return False

    return True


nums = [1, 1, 1]
print(check_increa(nums))
