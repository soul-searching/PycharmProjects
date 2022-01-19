# --------------------------幂运算-------------------------
def power(x, n=2.0):
    s = 1
    while n > 0:
        n = n - 1
        s = x * s
    return s


print(power(float(input('please enter x:')), float(input('please enter n:'))))
# --------------------------------------------------------
