n = int(input())

for i in range(n):

    s = input()
    s1 = s.count("010")
    s2 = s.count("101")
    if s1 > 0:
        print("Good")
    elif s2 > 0:
        print("Good")
    else:
        print("Bad")