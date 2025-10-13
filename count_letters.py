s = input()
dict = {}
for i in range(len(s)):
    dict[s[i]] = dict.get(s[i],0)+1

sorted_dict = list(dict.keys())
sorted_dict.sort()

for i in sorted_dict:
    print(f"{i} : {dict[i]}")