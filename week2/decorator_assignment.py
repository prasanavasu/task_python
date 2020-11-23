def logged(func):
    def wrapper(*args, **kwargs):
        print(f"you called {func.__name__}{args}")
        return func(*args, **kwargs)

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


a = func(4, 4, 4)
print(f"it returned {a}\n{a}")
