def validate_args(func):
    def wrapped_func(*args):
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"
        return func(*args)
    return wrapped_func


@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci(3, 4))
print(fibonacci(-2))
print(fibonacci("hello"))
