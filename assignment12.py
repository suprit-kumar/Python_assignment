"""Recursion"""

"""WRF to print N even natural numbers"""

# def printN(n):
#     if n > 0:
#         printN(n - 1)
#         if n%2==0:
#             print(n, end=' ')
#
# inp=10
# printN(inp*2)

"""WRF to print N even natural number in reverse order"""
# def printN(n):
#     if n > 0:
#         if n%2==0:
#             print(n, end=' ')
#         printN(n - 1)
# inp=7
# printN(inp*2)

"""WRF to print N odd naturals number"""
# def printN(n):
#     if n > 0:
#         printN(n - 1)
#         if n%2!=0:
#             print(n, end=' ')
#
# inp=10
# printN(inp*2)

"""WRF to print N odd naturals number in reverse order"""
# def printN(n):
#     if n > 0:
#         if n%2!=0:
#             print(n, end=' ')
#         printN(n - 1)
# inp=7
# printN(inp*2)


"""WRF to print sum of first N naturals number"""
# def print_sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+print_sum(n-1)
#
# sum=print_sum(5)
# print('sum of N naturals number: ',sum)

"""WRF to print squares of first N naturals number"""
# def print_squares(n):
#     if n==0:
#         return 0
#     else:
#         print_squares(n-1)
#         print(n*n,end=', ')
#
# print_squares(5)

"""WRF to print squares of first N natural numbers in reverse order"""

# def print_squares(n):
#     if n==0:
#         return 0
#     else:
#         print(n * n, end=', ')
#         print_squares(n-1)
#
# print_squares(5)

"""WRF to print cubes of first N natural numbers"""
def print_cubes(n):
    if n==0:
        return 0
    n+print_cubes(n-1)
    print(n**3,end=', ')



"""WRF to print cubes of firsrt N natural numbers in  reverse order"""
# def print_cubes(n):
#     if n==0:
#         return 0
#     else:
#         print(n ** 3, end=', ')
#         print_cubes(n-1)
#
# print_cubes(5)
