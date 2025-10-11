# nums = input()
# numbers = nums.split()
#
# x = int(numbers[0])
# y = int(numbers[1])
#
# last_digit  = (x%10) + (y%10)
#
# print(last_digit)
# for i in range(5,0,-1):
#         if i % 2 == 0:
#             continue
#         if i == 3:
#             break
#         print(i,end="")


# msg = "red,green,blue"
# color = msg.split(",")
# print("-".join(color[::-1]))
#
# num = [2,4,6,8,10]
# num[2] = num[2]*num[0]
# print(num)

# l = ['a','b','c','d','e']
# print(l[1:4][::-2])

# s = []
# for i in range(4):
#     s.append(i)
# s.pop()
# print(s[-1])

# q = [1,2,3,2,4]
# q.remove(4)
# q.pop()
# print(q)

model_accuracy = 0.83333

print(f"the model accuracy is {model_accuracy:.2%}")
