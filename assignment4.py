"""WPS to check wheather a given number is prime or not."""

# inp=int(input('Enter a number\n'))
# if inp>1:
#      for i in range(2,inp):
#          if inp%i==0:
#              print('Is not a prime number')
#              break
#      else:
#          print('Is a Prime Number')


"""WPS to print next prime number of a given number."""
# inp = int(input('Enter a number\n'))
# while inp>1:
#     inp+=1
#     for i in range(2,inp):
#         if inp%i==0:
#             break
#     else:
#         print('Next prime number is--',inp)
#         break

"""WPS to print first N prime number . Value of N given by the user."""
# inp = int(input('Enter a number\n'))
# while inp>1:
#     inp -= 1
#     for i in range(2,inp):
#         if inp%i==0:
#             break
#     else:
#         print('prime number is--',inp)


"""WPS to print all prime numbers between two given numbers."""

# inp1 = int(input('Enter a number\n'))
# inp2 = int(input('Enter a number\n'))
# value=0
# while inp1>1:
#     inp1 += 1
#     for i in range(2,inp1):
#         if inp1%i==0:
#             break
#         elif inp1>inp2:
#             break
#     else:
#         print('prime number is--',inp1)

"""WPS to check wheather two given numbers are co-prime or not."""
# inp1 = int(input('Enter a number\n'))
# inp2 = int(input('Enter a number\n'))
#
# for i in range(2, inp1, inp2):
#     if inp1 % i == 0 and inp2 % i == 0:
#         print('Not co-prime numbers')
#         break
# else:
#     print('co-prime numbers')


"""WPS to print first N odd naturals numbers in reverse order using range function in for loop."""
# inp = int(input('Enter Number\n'))
# for i in range(2*inp-1,0,-2):
#     print('N odd naturals numbers -->',i)

"""WPS to print first N even natural numbers in reverse order using range function in for loop."""
# inp = int(input('Enter Number\n'))
# for i in range(2*inp,0,-2):
#     print('N odd naturals numbers -->',i)

"""WPS to print all prime factors of a given number."""
# inp = int(input('Enter Number\n'))
# i=2
#
# while inp>1:
#     if inp%i==0:
#         print('prime factor-->',i)
#         inp=inp/i
#     else:
#         i+=1

"""WPS to check how many numbers of  "a" present in your full name, input take from the user"""
# inp=input('Enter a String\n')
# count=0
# for i in inp:
#     if i == 'a' or i=='A':
#         count+=1
#         # print('a-->',i)
# print('a/A is',count,'times available in this string')


"""WPS to check a string is a Palindrome or not"""
# inp=input('Enter a String\n')
# x=''
# for i in inp:
#     x=i+x
# print('String in reverse order -',x)
# if inp == x:
#     print('String is palindrome')
# else:
#     print('Not palindrome')

"""WPS to calculate LCM of two numbers."""
# inpx=int(input('Enter a String\n'))
# inpy=int(input('Enter a String\n'))
# l=1
#
# while l<=inpx*inpy:
#     l+=1
#     if l%inpx==0 and l%inpy==0:
#         break
# print('LCM of two numbers-->',l)


"""WPS to calculate HCF of two numbers."""
# inpx=int(input('Enter a String\n'))
# inpy=int(input('Enter a String\n'))
# l=1
# h=''
# if inpx<inpy :
#     h=inpx
# elif inpy<inpx:
#     h = inpy
#
# while l<=h:
#     if inpx%h==0 and inpy%h==0:
#         break
#     h -= 1
# print('HCF of two numbers-->',h)