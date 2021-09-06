# passed
w = int(input())
if 1 <= w <= 100:
    # 2 being an even number cannot be divided into two even weights
    if w % 2 == 0 and w != 2:
        print("YES")
    else:
        print("NO")
