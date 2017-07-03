import math

def primeNumbers(n):
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0 or x == 3 or x < 2:
            return False
    return True

def printer(n):
    seq = []

    for i in range(0, n+1):
        if primeNumbers(i):
            if i != 3 or i <2:
                seq.append(i)
    print seq

if __name__ == "__main__":
    printer(9)
