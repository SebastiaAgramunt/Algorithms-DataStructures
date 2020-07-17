import time


def fibonacci(n):
    # Find the n'th Fibonacci number
    # Slow solution, each time we call fibonaci, the function is called twice
    # in a progression 2, 4, 8, 16... i.e. 2 to the power of n.
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonaci_dynamic(n):
    # a dynamic programming approach.
    # with fib_recursion we store intermediate values
    fib = [0, 1]

    while len(fib) < n + 1:
        fib.append(0)

    fib[n] = fib_recursion(n, fib)

    # we can return the whole fibonacci sequence
    # by calling return fib instead of fib[n]
    return fib[n]


def fib_recursion(n, fib):
    # helper function, that takes fib as the list
    # of fibonnacci numbers (initialized to 0)
    if n <= 1:
        return n
    else:
        if fib[n - 1] == 0:
            fib[n - 1] = fib_recursion(n - 1, fib)
        if fib[n - 2] == 0:
            fib[n - 2] = fib_recursion(n - 2, fib)

    fib[n] = fib[n - 2] + fib[n - 1]

    return fib[n]


def forward_fibonacci(n):

    fib = [0, 1]

    if n <= 1:
        return fib[n]

    else:
        i = 2
        while len(fib) < n + 1:
            fib.append(fib[i - 1] + fib[i - 2])
            i += 1

    return fib[n]


def fib(n):

    F = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)

    return F[0][0]


def multiply(F, M):

    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


# Optimized version of
# power() in method 4
def power(F, n):

    if n == 0 or n == 1:
        return
    M = [[1, 1], [1, 0]]

    power(F, n // 2)
    multiply(F, F)

    if n % 2 != 0:
        multiply(F, M)


if __name__ == "__main__":

    n = 200

    """
	start = time.time()
	f = fibonaci_dynamic(n)
	end = time.time()

	print("the {}th fibonacci number is {}, calculated using dynamig programming O(N). Time elapsed {}".format(n, f, end-start))
	"""
    start = time.time()
    f = forward_fibonacci(n)
    end = time.time()

    print(
        "the {}th fibonacci number is {}, calculated using forward fibonacci O(N). Time elapsed {}".format(
            n, f, end - start
        )
    )

    start = time.time()
    f = fib(n)
    end = time.time()

    print(
        "the {}th fibonacci number is {}, calculated using powr matrix optimized O(log(N)), taken from GeeksToGeeks webpage. Time elapsed {}".format(
            n, f, end - start
        )
    )

    """
	start = time.time()
	f = fibonacci(n)
	end = time.time()

	print("the {}th fibonacci number is {}, calculated using recursion O(2^N). Time elapsed {}".format(n, f, end-start))
	"""
