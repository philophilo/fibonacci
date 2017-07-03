import math

def primeNumbers(n):
    seq = []
    for x in range(0, n + 1):
        if x > 1:
            print x
            for i in range(2, x):
                if n % i == 0:
                    break
                else:
                    seq.append(x)
    print seq


if __name__ == "__main__":
    primeNumbers(9)
