from random import randint

def GenPrime():

    small_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                   37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
                   79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
                   131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
                   181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]

    while True:

        PotentialPrime = True

        num = randint(1999, 4999)

        if num % 2 == 0:
            num += 1

        for pr in small_primes:
            if num % pr == 0:
                PotentialPrime = False
                break

        if not PotentialPrime:
            continue

        n = num - 1

        s, d = 0, 0
        while True:
            if n % 2 == 0:
                n //= 2
                s += 1
            else:
                d = n
                n = num - 1
                break

        for i in range(5):

            a = randint(1, n)
            PotentialPrime = False

            for j in range(s):
                test = pow(a, 2 ** j * d, num)
                if test == 1 or test == n:
                    PotentialPrime = True
                    break

            if not PotentialPrime:
                break

        if PotentialPrime:
            return num

def gcd(a, b):

    if (a == 0):
        return b
    else:
        return gcd(b % a, a)

def ChooseG(p):

    p -= 1
    factors = list()

    for i in range(2, int(p ** 0.5)):
        if p % i == 0:
            factors.append(i)
    
    even = True
    p += 1

    for n in factors:
        if pow(2, n, p) == 1:
            even = False
            break

    if even:
        return 2

    else:
        for i in range(3, p - 1):
            if gcd(i, p) == 1:
                root = True
                for n in factors:
                    if pow(i, n, p - 1) == 1:
                        root = False
                        break

                    if root:
                        return n
            else:
                continue

a, b = randint(200, 500), randint(200, 500)
print("Закрытый ключ Алисы:", a)
print("Закрытый ключ Боба:", b)

p = GenPrime()
g = ChooseG(p)
print("p =", p)
print("g =", g)

A, B = pow(g, a, p), pow(g, b, p)
print("Открытый ключ Алисы:", A)
print("Открытый ключ Боба:", B)

Alice_K, Bob_K = pow(B, a, p), pow(A, b, p)

print("Секретный ключ Алисы:", Alice_K)
print("Секретный ключ Боба:", Bob_K)