import time
import math

def sqrt_after_ms(num, ms):
    time.sleep(ms/1000)
    sqrt_result = math.sqrt(num)
    print(f"Square root of {num} after {ms} milliseconds is {sqrt_result}")

num = 25100
ms = 2123
sqrt_after_ms(num, ms)