def calculate_nth_fibonacci(n: int):
    if n == 0:
        return n

    previous = 1
    previous_previous = 0

    while n > 1:
        curr = previous + previous_previous
        previous_previous = previous
        previous = curr
        n -= 1

    return previous


def calculate_all_fibonacci(limit: int):
    all_fib = []
    while limit > 0:
        all_fib.append(calculate_nth_fibonacci(limit - 1))
        limit -= 1
    return all_fib


if __name__ == "__main__":
    calculate_all_fibonacci(7000)
    print("done!")
