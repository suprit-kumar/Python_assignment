"""WPS to sort a list given by user"""
# in1, in2, in3, in4, in5 = (input('Enter string\n')), (input('Enter string\n')), (input('Enter string\n')), (
# input('Enter string\n')), (input('Enter string\n'))
# li = []
#
# li.append(in1)
# li.append(in2)
# li.append(in3)
# li.append(in4)
# li.append(in5)
# print('list-->', li)
# li.sort()
# print('sorted list-->',li )

"""WPS to find greatest number in a list of integers given by user"""
# in1, in2, in3, in4, in5 = int(input('Enter number\n')), int(input('Enter number\n')), int(input('Enter number\n')), int(input('Enter number\n')), int(input('Enter number\n'))
# li = []
#
# li.append(in1)
# li.append(in2)
# li.append(in3)
# li.append(in4)
# li.append(in5)
#
# print('list-->', li)
# li.sort()
# print('the largest number in the list-->',li[-1])

"""WPS to calc. sum of all integers of the list given by user"""
# in1, in2, in3, in4, in5 = int(input('Enter number\n')), int(input('Enter number\n')), int(input('Enter number\n')), int(input('Enter number\n')), int(input('Enter number\n'))
# li = []
#
# li.append(in1)
# li.append(in2)
# li.append(in3)
# li.append(in4)
# li.append(in5)
#
# print('list-->', li)
# sum = 0
# for x in li:
#     sum=sum+x
#
# print('sum of all integers-->',sum)

"""WPS to create a list of first N prime numbers.Value of N is given by user"""

# inp=int(input('Enter N number\n'))
# li=[]
# count=inp
# x=1
# while inp>1:
#     x += 1
#     for i in range(2,x):
#         if x%i==0:
#             break
#     else:
#         li.append(x)
#         if count==len(li):
#             break
# print('prime number is--',li)


"""WPS to create a list of squares of first N natural numbers.
Use for loop to fill list with elements.Value of N taken from the user."""

# inp=int(input('Enter N number\n'))
# li=[]
#
# for x in range(inp,0,-1):
#     li.append(x**2)
# li.sort()
# print('squares of first N natural numbers-->',li)


"""WPS to print indices of all occurance of given element in a given list"""

# li=[10,20,30,40,20,10,25,30,60]
# for i in li:
#     print('Index of ',i,'-',li.index(i))


"""WPS to print distinct list elements along with their frequency occurance in the list"""

# li=[10,20,30,40,20,10,25,30,60]
# for i in li:
#     x=li.count(i)
#     if x<2:
#         print('Index of ', i, '-', li.index(i))


"""WPS to calc. sum of all even numbers and sum of all odd numbers of the list,list given by the user"""
# in1, in2, in3, in4, in5, in6, in7, in8, in9, in10 = int(input('Enter number\n')), int(input('Enter number\n')), int(
#     input('Enter number\n')), int(
#     input('Enter number\n')), int(input('Enter number\n')), int(input('Enter number\n')), int(
#     input('Enter number\n')), int(input('Enter number\n')), int(input('Enter number\n')), int(input('Enter number\n'))
# li = []
# li.append(in1)
# li.append(in2)
# li.append(in3)
# li.append(in4)
# li.append(in5)
# li.append(in6)
# li.append(in7)
# li.append(in8)
# li.append(in9)
# li.append(in10)
# sumOdd = 0
# sumEven = 0
# for i in li:
#     if i % 2 == 0:
#         sumEven = sumEven + i
#     else:
#         sumOdd = sumOdd + i
#
# print('sumEven ==>',sumEven)
# print('sumOdd ==>',sumOdd)
