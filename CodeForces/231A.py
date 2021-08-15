# passed

q = 0
for i in range(int(input())):
    x = 0

    arr = input().split()
    for a in arr:
        if a == '1':
            x += 1
        else:
            continue
    if x > 1:
        q += 1
print(q)