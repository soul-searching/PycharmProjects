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
