"""WPF to calc. LCM of two numbers (Takes Something,Return Something)"""

# def lcm(a,b):
#     l=1
#     while l<=a*b:
#         l+=1
#         if l%a==0 and l%b==0:
#             break
#     print('LCM of two numbers-->', l)
#
# lcm(4,6)


"""WPF to count words in a given string (Takes Something,Return Something)"""

# def count_words(word):
#     print('no of words in this given string-->',len(word))
#
# count_words('Suprit')

"""WPF to calc. sum of all even numbers and sum of all odd numbers from a given list of int values.(Takes Something,Return Something)"""

# def sum_odd_even(mylist):
#     odd=[]
#     even=[]
#     for i in mylist:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     print("even :",even)
#     print("odd :",odd)
#     print('Sum of all even numbers :',sum(even))
#     print('Sum of all odd numbers :',sum(odd))
#
# mylist=[1,2,33,44,55,66,77,88,99,100,111,15,16,18,20]
# sum_odd_even(mylist)

"""WPF to find next prime number of a given number (Takes Something,Return Something)"""

# def nxt_prime(n):
#     while n>1:
#         n+=1
#         for i in range(2,n):
#             if n%i==0:
#                 break
#         else:
#             print('next prime number is :',n)
#             break
#
# nxt_prime(9)

"""WPF to print fist N prime numbers (Takes Something,Return Something)"""


# def getprimes(x):
# 	primes = []
# 	# Loop through 9999 possible prime numbers
# 	for a in range(1, 10000):
# 		# Loop through every number it could divide by
# 		for b in range(2, a):
# 			# Does b divide evenly into a ?
# 			if a % b == 0:
# 				break
# 		# Loop exited without breaking ? (It is prime)
# 		else:
# 			# Add the prime number to our list
# 			primes.append(a)
# 		# We have enough to stop ?
# 		if len(primes) == x:
# 			return primes
#
#
# def prime():
#     check=getprimes(20)
#     print('prime numbers :',check)
# prime()


"""WPF which takes a list of strings as an argument and returns a dictionary 
whose each item is a pair of alphabet(as key)and list of strings begin with that alphabet"""

# mylist=['sunday',1,'monday',2,'tuesday',3,'wednesday',4,'thursday',5,'friday',6,'saturday',7]
#
# def return_dictioary(mylist):
# 	mydict={mylist[i]:mylist[i+1] for i in range(0,len(mylist),2)}
# 	print('mydict: ',mydict)
# 	# for i in range(0, len(mylist), 2):
# 	# 	print('i: ',mylist[i],i,'-',mylist[i+1])
# return_dictioary(mylist)



"""WPF which takes tuple of int values and returns a dictionary 
whose each item is a pair of int value and its frequency in the tuple"""

def return_tuple_dictionary():
	inp=eval(input('Enter a number tuple\n'))
	sort_tuple=sorted(inp)
	for i in sort_tuple:
		my_dict={i:sort_tuple.count(i)}
		print('my_dict: ',my_dict)

return_tuple_dictionary()