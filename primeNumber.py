import math

def primeNumbers(n):
    for x in range(2, int(math.sqrt(n) + 1)):
        if x % x == 0:
            return False
    return True

def printer(n):
    seq = []

    for i in range(0, n+1):
        """if i == 2:
            iseq.append(i)"""
        if i != 3 or i < 2 :
            if primeNumbers(i):
                seq.append(i)
    print seq

if __name__ == "__main__":
    printer(9)
