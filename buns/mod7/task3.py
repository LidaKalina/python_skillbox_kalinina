import time


def timer(func):

    def wrapped_func(*args):
        started_at = time.time()
        result = func(*args)
        ended_at = time.time()
        run_time = ended_at - started_at
        print('Функция работала {} секунд(ы)'.format(run_time))
        return result

    return wrapped_func


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@timer
@memoize
def fibonacci_memoise(n):
    if n < 2:
        return n
    return fibonacci_memoise(n - 1) + fibonacci_memoise(n - 2)


@timer
def fibonacci_classic(n):
    return fibonacci(n)


print(fibonacci_classic(100))
print(fibonacci_memoise(100))
