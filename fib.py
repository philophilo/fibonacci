def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-1))
def printer(n):
    seq = []
    if isinstance(n, int):
        if n >= 1:
            for i in range(n):
                seq.append(fib(i))
            return seq
        else:
            return "integer must be greater than 1"
    else:
        return "please input integer"

if __name__ == "__main__":
    printer(1)
