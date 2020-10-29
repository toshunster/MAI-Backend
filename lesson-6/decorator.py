#! /usr/bin/env python3

import time

def timer(delay):
    def timer_(func):
        def wrapper(*args, **kwargs):
            start_ts = time.time()
            time.sleep(delay)
            res = func(*args, **kwargs)
            end_ts = time.time()
            print(f"Total time is {end_ts - start_ts} seconds")
            return res
        return wrapper
    return timer_

def echo(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        res = func(*args, **kwargs)
        return res
    return wrapper

@timer(1)
@echo
def calc():
    res = 0
    for num in range(10 ** 6):
        res += num
    return res

def main():
    print(f"Result={calc()}")

if __name__ == "__main__":
    main()
