import math


# 最大公约数
def gcd(a: int, b: int) -> int:
    # return a if b == 0 else gcd(b, a % b)
    return math.gcd(a, b)


# 最小公倍数
def lcm(a: int, b: int) -> int:
    # return a // gcd(a, b) * b
    return math.lcm(a, b)


# 同余原理：加法
# (a + b) % m = (a % m + b % m) % m

# 同余原理：减法
# (a - b) % m = ((a % m) - (b % m) + m) % m

# 同余原理：乘法
# (a * b) % m = ((a % m) * (b % m)) % m

# 同余原理：除法 (需要逆元)

"""
若 (a - b) mod 10 = x
则 b mod 10 = (a - x) mod 10

证明
根据 mod 运算性质, 若 (a - b) mod 10 = x
那么存在一个整数 k
使得 a - b = 10k + x
即 b = a - 10k - x
取模 b mod 10 = (a - 10k - x) mod 10
即 b mod 10 = (a - x) mod 10

关于减 10k 为什么能消掉
假设存在数组 a 且 a mod 10 = r 则 a = 10q + r
即 a - 10k = 10q + r - 10k = 10(q - k) + r
10(q - k) + r mod 10 = r
a mod 10 = (a - 10k) mod 10 = r
"""
