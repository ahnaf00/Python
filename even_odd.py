n = int(input())
inpt = input()

numbers = inpt.split()

even = 0;odd = 0;pos = 0;neg = 0
for i in range(n):
    if int(numbers[i]) % 2 == 0:
        even += 1
    if int(numbers[i]) % 2  == 1:
        odd += 1
    if int(numbers[i]) > 0:
        pos += 1
    if int(numbers[i]) < 0:
        neg += 1

print("Even:",even)
print("Odd:",odd)
print("Positive:",pos)
print("Negative:",neg)