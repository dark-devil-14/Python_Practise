
num = list(map(int, input().split()))

def is_prime(n):
    if(n<2):
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
        
    return True

new_num = num[0] + 1

while True:
    if is_prime(new_num):
        break
    new_num += 1


if is_prime(num[0]) and is_prime(num[1]) and new_num == num[1] :
    print("YES")
else:
    print("NO")