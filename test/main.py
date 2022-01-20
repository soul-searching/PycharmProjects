# -------------------------必选参数-指数运算------------------------
# def power(x, n=2.0):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = x * s
#     return s
#
#
# print(power(float(input('please enter x:')), float(input('please enter n:'))))
# -------------------------------------------------------------

# --------------------------默认参数-----------------------------
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
# print(calc(1, 2, 3, 5))               # 写法1
#
# w = [1, 2, 3, 5]                      # 存在已知list
# print(calc(w[0], w[1], w[2], w[3]))   # 写法2
# print(calc(*w))                       # 写法3  推荐

# -----------------------------------------------------------

# ----------------------关键字参数-----------------------------
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
#
# person('wm', 34, city='BeiJing', Tel='13300008888')  # 写法1
#
# extra = {'city': 'YanCheng', 'Tel': 18800006666}  # 存在已知dict
# person('pl', 29, city=extra['city'], Tel=extra['Tel'])  # 写法2
# person('pl', 29, **extra)  # 写法3  推荐
# ------------------------------------------------------------

# --------------------------命名关键字--------------------------
# def person1(name, age, *, city, job):    #方法1
#     print('name:', name, 'age:', age, 'city:', city, 'job:', job)
#
#
# def person2(name, age, *kw, city, job):     #方法2
#     print('name:', name, 'age:', age, '坐标:', kw, 'city:', city, 'job:', job)
#
#
# person1('wyh', 3, city="SZ", job='engineer')
# person2('zhx', 60, 123, 133, 35, city='SZ', job='housekeeper')
# ------------------------------------------------------------

# --------------------------组合参数---------------------------
# def f1(a, b, c, *err, **kw):
#     print(a, b, c, err, kw)
#
#
# def f2(a, b, c, *, d, **kw):
#     print(a, b, c, d, kw)
#
#
# m1 = [12, 13, 14, 15, 88]
# m2 = {'r': 45, '#': '^'}
# f1(*m1, **m2)
# ------------------------------------------------------------

# -------------------------练习-多位乘法------------------------
# def mul(*number):
#     if number == ():
#         raise TypeError('Fuck')
#     s = 1
#     for n in number:
#         s = s * n
#     return s
#
#
# # 测试
# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
# if mul(5) != 5:
#     print('测试失败!')
# elif mul(5, 6) != 30:
#     print('测试失败!')
# elif mul(5, 6, 7) != 210:
#     print('测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         mul()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')
