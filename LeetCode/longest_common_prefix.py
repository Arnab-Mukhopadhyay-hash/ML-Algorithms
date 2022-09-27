def findPrefix(s1, s2):
    # function to check two consecutive strings for prefix
    # we check the prefix and the a new string to find similarities
    # O(n) Complexity
    prefix = ""
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix = prefix + s1[i]
        else:
            break
    return prefix

if __name__ == "__main__":
    strs = []   # list of strings
    n = int(input("Number of Strings: "))
    # taking string inputs
    for _ in range(n):
        str = input("String Input: ")
        strs.append(str)
    
    ans = strs[0]
    for i in range(1, len(strs)):
        ans = findPrefix(ans, strs[i])
    print(ans)
