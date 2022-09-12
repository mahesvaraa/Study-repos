from functools import wraps

def dec(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('== lol ==')
        func(*args, **kwargs)
        print('=== lol ===')
    return inner

@dec
def arr(x):
    '''
    документашка

    :param x:
    :return:
    '''
    print(max(x))

arr([1, 25, 7])
print(arr.__doc__)
print(arr.__name__)