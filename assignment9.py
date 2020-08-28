"""WPS to find the common elements between two sets"""
# s=set([10,20,30,40,50,6,0])
# v=set([30,50,12,16,28,9,0])

# similar=s.intersection(v)
# print('common elements between two sets-->',similar)
import math

"""WPS to create a set of first N prime numbers"""
# inp=int(input('Enter a number\n'))
# multiply=inp*2
# s=set()
#
# while multiply>1:
#     multiply -= 1
#     for i in range(2,multiply):
#         if multiply%i==0:
#             break
#
#     else:
#         s.add(multiply)
#
# print('set-->',s)


"""WPS to take union of two sets"""

# s=set([10,20,30,40,50,6,0])
# v=set([30,50,12,16,28,9,0])
#
# union_set=s.union(v)


"""WPS to count elements of a set given by user"""
# people = {"Jay", "Idrish", "Archi"}
#
# print('count elements-->',len(people))

""""WPS to count distinct elements in a list using set"""

# list1=[1,2,3,4,5,6,7,8,9,10]
# list2=[10,7,5,3,13,22,11,21]
#
# set1=set(list1)
# set2=set(list2)
#
# first_distinct=set1-set2
# second_distinct=set2-set1
#
# first_distinct.update(second_distinct)
# print(first_distinct)


"""WPS to check wheather a given set is a subset of another given set or not"""
# s1,s2,s3={1,2,3,4},{2,3},{2,3,5}
#
# print('s2 is subset of s1---',s2.issubset(s1))
# print('s3 is subset of s1---',s3.issubset(s1))
# print('s1 is superset of s2---',s1.issuperset(s2))


