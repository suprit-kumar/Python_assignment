"""WPS to calc. lentgh of a string. String given by user"""
# inp=input('Enter Something\n')
# print('input -->',inp)
# print('length of the string -->',len(inp))

"""WPS to count vowels in a given string"""
# inp=input('Enter Something\n')
# x=inp.lower()
# count=0
# lst=[]
# for i in x:
#     if i=='a':
#         lst.append(i)
#     if i=='e':
#         lst.append(i)
#     if i=='i':
#         lst.append(i)
#     if i=='o':
#         lst.append(i)
#     if i=='u':
#         lst.append(i)
#
# print('lst-->',lst)
# print('count vowels in a given string-->',len(lst))

"""WPS to reverse a string"""
# inp=input('Enter Something\n')
# print('Reverse String-->',inp[len(inp)::-1])

"""WPS to count occurance of a given character in given string"""
# inp=list(input('Enter Something\n'))
# print(inp)
# for i in inp:
#     x=inp.count(i)
#     print(i,'-',x)

'WPS to count words in given string'
# inp=input('Enter Something\n')
#
# print("The original string length-->",len(inp))
# x=len(inp.split())
# print('count words in given string-->',x)

"""WPS to arrange words in a given string in alphabetical order"""
# inp=input('Enter Something\n')
#
# words=inp.split()
# words.sort()
#
# for word in words:
#     print('alphabetical order-->',word)


"""WPS to check wheather a string is a plaindrome or not"""
# inp=input('Enter Something\n')
# print('The original string-->',inp)

# palindrome=inp[len(inp)::-1]
# print('palindrome-->',palindrome)
#
# if palindrome==inp:
#     print('Yes,This is a palindrome')
# else:
#     print('This is not palindrome')

# checkPalindrome=''
# for i in inp:
#     checkPalindrome=i+checkPalindrome
#
# if inp==checkPalindrome:
#     print('palindrome')
# else:
#     print('Not palidrome')
#
# print('checkPalindrome-->',checkPalindrome)

"""WPS to remove duplicate charcters from string"""
# inp=input('Enter Something\n')
# string=''
# for i in inp:
#    if i  not in string:
#        string=string+i
#
# print('string-->',string)