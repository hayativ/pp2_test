import time
import math
def my_func(x, dealy):
    time.sleep(delay / 1000.0)
    result = math.sqrt(x)
    return result

x = int(input())
delay = int(input())
result = my_func(x, delay)
print(f"Square root of {x} after a {delay} milliseconds is: {result}")