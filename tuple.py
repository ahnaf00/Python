n = int(input())

nums = list(map(int, input().split()))
t = tuple(nums)
print(hash(t))
