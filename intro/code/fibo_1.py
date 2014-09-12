def fib(n):
    """ Return n-th number in Fibonacci sequence."""
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    reqNumber = int(raw_input(
                "Enter index of requested Fibonacci number: "))
    print "Your number is:", fib(reqNumber)
