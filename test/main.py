# -------------------------指数运算------------------------
# def power(x, n=2.0):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = x * s
#     return s
#
#
# print(power(float(input('please enter x:')), float(input('please enter n:'))))
# --------------------------------------------------------

# --------------------------多参数-----------------------------
# def enroll(name, gender, age=6, city='SuZhou'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
#
#
# print(enroll('wangyihan', 'AAA'))


# ------------------------------------------------------------

# -------------------可变参数陷阱（优化后）-----------------------
# def add_end(L=None):
#     if L is None:
#         L = []
#         L.append('END')
#     return L
#
#
# print(str(add_end([1, 2, 3, 4])))
# ------------------------------------------------------------

# --------------------可变参数平方和----------------------------
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n*n
#     return sum
#
#
# print(calc(1, 2, 3, 5))               # 写法一
#
# w = [1, 2, 3, 5]                      # 存在已知list
# print(calc(*w))                       # 写法二
# print(calc(w[0], w[1], w[2], w[3]))   # 写法三

# -----------------------------------------------------------

# -----------------------------------------------------------
