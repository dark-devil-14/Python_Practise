
# You are given 4 sticks of lengths 𝑎, 𝑏, 𝑐, and 𝑑. You can not break or bend them.
# Determine whether it is possible to form a square∗ using the given sticks.

t = int(input())   # number of test cases

for i in range(t):
    a = list(map(int, input().split()))
    
    if len(set(a)) == 1:
        print("YES")
    else:
        print("NO")

