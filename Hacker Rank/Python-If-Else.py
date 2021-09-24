# passed

"""Problem Statement:
Given an integer n do the following:
* if n is odd, print Weird
* if n is even and in the inclusive range of 2 to 5, print Not Weird
* if n is even and in the inclusive range of 6 to 20, print Weird
* if n is even and greater than 20, print Not Weird

Constraints:
1<=n<=100"""

n = int(input("Enter a number: "))
if 1 <= n <= 100:
    if n % 2 == 0:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
    else:
        print("Weird")