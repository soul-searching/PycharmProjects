# --------------------递归函数---------------------
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(5))
# ------------------------------------------------

# --------------------尾递归函数--------------------
# def fact(n, product):
#     if n == 1:
#         return product
#     return fact(n - 1, n * product)
#
#
# print(fact(5, 10))

# --> fact(5, 1)
# --> fact(4, 5)
# --> fact(3, 20)
# --> fact(2, 60)
# --> fact(1, 120)
# ------------------------------------------------
# def trim(s):
#
#
#     if s == '':
#         raise TypeError('Fuck')
#     elif s[0] == ' ' and s[-1] == ' ':
#         return s[1:-1]
#     elif s[0] == ' ' and s[-1] != ' ':
#         return s[1:]
#     elif s[0] != ' ' and s[-1] == ' ':
#         return s[:-1]
#     elif s[0] != ' ' and s[-1] != ' ':
#         return s[:]
#     else:
#         return s
# ----------------------切片----------------------
def trim(s):
    if s[:1] == " ":
        return trim(s[1:])
    elif s[-1:] == " ":
        return trim(s[:-1])
    else:
        return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
