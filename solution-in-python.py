import math

def is_prime(n):

    for i in range(2 , int(math.sqrt(n)) + 1):

        if n % i == 0:
            return False
    
    return True

# Input

n = int(input("Digite um número inteiro positivo par:"))

while n % 2 != 0 or n < 2 or n > 4294967294:

    n = int(input("Digite um número inteiro positivo par:"))

# # # # #

# Set of Primes less than n

P = []

for i in range(2,n):

    if is_prime(i) == True:

        P.append(i)

# # # # #

# Decomposition 

loop = False

i = 0
j = 0

if n == 2:

    print(-1)

else:
    
    while loop == False:
        
        if j == len(P):

            j = 0
            i += 1
        
        if i > len(P):

            loop = True
            print(-1)

        k = P[i] + P[j]
            
        if k == n:

            loop = True

        j += 1

    if k == n:
        
        print(f"{P[i]}\n{P[j - 1]}")