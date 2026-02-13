# A. Lucky?

test_case = int(input())

for i in range(test_case):
    num = input()
    left_check = int(num[0]) + int(num[1]) + int(num[2])
    right_check = int(num[5]) + int(num[4]) + int(num[3])
    if(left_check == right_check):
        print("YES")
    else:
        print("NO")