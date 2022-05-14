import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__module__}.{func.__name__}: {end-start}s, result')

    return wrapper


if __name__ == '__main__':

    @timethis
    def countdown(n):
        while n > 0:
            n -= 1

    print(countdown(100))
