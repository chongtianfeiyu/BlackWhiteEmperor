import functools

def oauth(func):
    @functools.wraps(func)
    def wrapper(*argv, **kwgs):
        print 1
        kwgs['player'] = {"id": 1}
        return func(*argv, **kwgs)
    return wrapper
