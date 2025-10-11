n = int(input())

for i in range(n):
    num = int(input())
    if num == 0:
        print(0)
        continue
    while num > 0:
        remainder = num % 10
        print(remainder, end=" ")
        num //= 10
    print()