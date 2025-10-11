n = int(input())
num = input()
nums = num.split()
new_list = []
for num in nums:
    new_list.append(int(num))

mn = new_list[0]
for num in new_list:
    if num < mn:
        mn = num
idx = new_list.index(mn)

print(mn,idx+1)