"""WRF to print sum of first N naturals number"""
# def print_sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+print_sum(n-1)
#
# sum=print_sum(5)
# print('sum of N naturals number: ',sum)

"""WRF calculate sum of squares of first N natural numbers"""
# sums=[]
# def sum_of_squares(n):
#     if n>0:
#         sums.append(n*n)
#         sum_of_squares(n-1)
#         return sums
# output=sum_of_squares(5)
# print("sum of squares:",sum(output))

"""WRF to calculate sum of cubes of first N natural numbers"""
# sums=[]
# def sum_of_squares(n):
#     if n>0:
#         sums.append(n**3)
#         sum_of_squares(n-1)
#         return sums
# output=sum_of_squares(5)
# print("sum of squares:",sum(output))

"""WRF to calculate sum of firsrt N odd natural numbers"""
# add = []
# def sum_odd(n):
#     if n > 0:
#         sum_odd(n - 1)
#         if n % 2 != 0:
#             print(n, end=' ')
#             add.append(n)
#         return add
#
# inp = 5
# result = sum_odd(inp * 2)
# print('sum of odd : ', sum(result))

# or
# def ret_sum(n):
#     if n == 1:
#         return 1
#     else:
#         return (2 * n - 1 + ret_sum(n - 1))
#
#
# result = ret_sum(5)
# print('sum of odd naturals number:', result)


"""WRF to calculate sum of first N even natural numbers"""
# def ret_sum(n):
#     if n == 1:
#         return 2
#     return (2 * n + ret_sum(n - 1))
#
# result = ret_sum(5)
# print('sum of even naturals number:', result)

"""WRF calculate sum of digits of a given number"""

# def sum_of_digit(n):
#     if n == 0:
#         return 0
#     return (n % 10 + sum_of_digit(int(n / 10)))
#
#
# # Driven code to check above
# num = 12345
# result = sum_of_digit(num)
# print("Sum of digits in", num, "is", result)
