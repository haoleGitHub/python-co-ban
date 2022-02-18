import math

n = int(input('Enter n: '))

def check_number(n):
    m = math.sqrt(n)
    if n < 2:
        return False
    else:
        for i in range(2, int(m)+1):
            if n % i == 0:
                return False
        return True

if check_number(n):
    print(str(n) + ' is prime!')
else:
    print(str(n) + ' is not prime!')
