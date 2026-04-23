n = int(input())
num = input()
nums = num.split()
new_list = []
for i in nums:
    new_list.append(int(i))

mn = new_list[0]
for i in new_list:
    if i < mn:
        mn = i
mn_idx = new_list.index(mn)

mx = new_list[0]
for i in new_list:
    if i > mx:
        mx = i
mx_idx = new_list.index(mx)

new_list[mn_idx], new_list[mx_idx] = new_list[mx_idx], new_list[mn_idx]
for i in new_list:
    print(i, end=" ")
    