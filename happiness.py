# n,m = map(int,input().split())
# print(n,m)

nm = input().split()
n = int(nm[0])
m = int(nm[1])

arr = input().split()

a = set(input().split())
b = set(input().split())

happiness = 0
for i in arr:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1

print(happiness)