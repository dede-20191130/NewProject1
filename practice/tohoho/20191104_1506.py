def mydecolater(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Funcname:", func.__name__)
        print("Arguments:", args)
        print("Keywords:", kwargs)
        ret = func(*args, **kwargs)
        print("Return:", ret)
        return ret

    return wrapper


@mydecolater
def func_AAABBB(msg1, msg2, flag=1, mode=2):
    """A sample function for test with tester'Ishikawa'"""
    print("----", msg1, msg2, "----")
    return 1234


n = func_AAABBB("Hello", "Hello2", flag=1)
print(n)

print(repr(func_AAABBB))
print(func_AAABBB.__doc__)
