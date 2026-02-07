
trial = int(input())

for i in range(trial):
    num = list(map(int, input().split()))
    check = ( num[0] + num[1] == num[2] or
            num[0] + num[2] == num[1] or
            num[1] + num[2] == num[0])
    if check:
        print("YES")
    else: 
        print("NO")