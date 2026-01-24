#Find the sum of n prime number .
'''
find the prime number from 2 to n 
if (this_is_prime) : += i 
if(this_is_not_prime) : move to next number 
'''

def check_is_prime(n):
    if(n<2):
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False 
    return True

num = int(input("Enter the number: "))
total_sum = 0 

for i in range (2,num+1):
    if(check_is_prime(i)):
        total_sum += i

print(f"The sum of prime number is : {total_sum}")
