import time


m_cache = {}


def factorial(n):
    if n == 0:
        return 1
    elif n in m_cache:
        return m_cache[n]
    else:
        result = n * factorial(n - 1)
        time.sleep(1)
        m_cache[n] = result
        return result


def iterator():
    for n in range(20, 0, -1):
        print(factorial(n))


iterator()
