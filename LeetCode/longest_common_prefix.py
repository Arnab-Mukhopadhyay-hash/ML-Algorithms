def findPrefix(s1, s2):
    prefix = ""
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix = prefix + s1[i]
        else:
            break
    return prefix

strs = []
n = int(input("Number of Strings: "))
for _ in range(n):
    str = input("String Input: ")
    strs.append(str)
ans = strs[0]
for i in range(1, len(strs)):
    ans = findPrefix(ans, strs[i])
print(ans)
