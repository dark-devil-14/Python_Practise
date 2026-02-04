
num = list(map(int, input().split()))

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
        
    return True

if is_prime(num[0]) and is_prime(num[1]):
    print("YES")
else:
    print("NO")