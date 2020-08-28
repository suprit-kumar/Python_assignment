"""WPS to print table of 5."""
# for x in range(1,6):
#     print('table of 5 -- ',x*5)



"""WPS to print table of user choice."""
# inp=int(input('Enter a number\n'))
# for x in range(1,inp+1):
#     print('table of',inp,'-',x*inp)

"""WPS to print all Armstrong number under 1000."""
# for n in range(1, 1000):
#     s = 0
#     x = n
#     while x != 0:
#         r = x % 10
#         s = s + r**3
#         x = x // 10
#     if s==n:
#         print('armstrong number--',n)

"""WPS to print squares of numbers from a to b. values of a and b given by the user."""
# inp1 = int(input('Enter a number\n'))
# inp2 = int(input('Enter a number\n'))
#
# for n in range(inp1, inp2):
#     print('squares of numbers from ', inp1, 'to', inp2,'-' ,n, '-', n ** 2)

"""WPS to print sequence of number with given step size and boundary values. 
For example boundary values are 10 and 30, Step is 2 then your output should be 10,12,14,16,18,20,22,24,26,28."""

# inp1 = int(input('Enter start value\n'))
# inp2 = int(input('Enter End value\n'))
#
# if inp2 > inp1:
#     step = int(input('Enter step value\n'))
#     for x in range(inp1,inp2,step):
#         print(x)
# else:
#     print('Enter greater End value than start value')
