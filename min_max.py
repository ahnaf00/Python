# li = input()
# nums = li.split()
# x = int(nums[0])
# y = int(nums[1])
# z = int(nums[2])
#
# mn = x
# if mn > y:
#     mn = y
# if mn > z:
#     mn = z
#
# mx = x
# if mx < y:
#     mx = y
# if mx < z:
#     mx = z
#
# print(mn, mx)

from functools import reduce
n = int(input())
nums = list(map(int, input().split()))

mn = reduce(lambda x,y: x if x< y else y, nums)
mx = reduce(lambda x, y : x if x > y else y, nums)

print(f"{mn} {mx}")
