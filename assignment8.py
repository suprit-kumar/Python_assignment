"""WPS to calc. avg. tuple values.Assuming values are integer type only """

# inp=eval(input('Enter a tuple\n'))
# lentgh=(len(inp))
# sum=0
# for i in inp:
#     sum=sum+i
# print(' avg. of tuple---',sum/lentgh)


"""WPS to sort a tuple"""
inp = eval(input('Enter a tuple\n'))
print('inp-->',inp)
new_tuple_list = sorted(inp)
print(' new_tuple_list-->',new_tuple_list)
change_to_tuple=tuple(new_tuple_list)
print(' change_to_tuple-->',change_to_tuple)


"""WPS to merge two sorted tuples"""

# inp1=eval(input('Enter a tuple\n'))
# inp2=eval(input('Enter a tuple\n'))
#
# new_tuple_list1=sorted(inp1)
# new_tuple_list2=sorted(inp2)
#
# merge_lst=sorted(new_tuple_list1+new_tuple_list2)
# mrg_tpl=tuple(merge_lst)
#
# print('mrg_tpl-->',mrg_tpl)

"""WPS to reverse a tuple"""
# inp = eval(input('Enter a tuple\n'))
# print('reverse-->',inp[::-1])

"""WPS to count elements in the tuple"""
# inp = eval(input('Enter a tuple\n'))
# print('count elements in the tuple-->',len(inp))


"""WPS to calc. sum of all elements of the tuple.Tuple input is taken from the keyboard (all values are int type)"""
# inp=eval(input('Enter a tuple\n'))
# sum=0
# for i in inp:
#     sum=sum+i
# print('sum of tuple---',sum)

"""WPS to create tuples with homogeneous elements from tuple containing heterogenous elements"""
# t = (30, 26, 4.5, 3 + 4j, 'abc', True, 5.6, 2 - 3j)
#
# int_typ_lst, float_typ_lst, complex_typ_lst, string_typ_lst, boolean_typ_lst = [], [], [], [], []
#
# for i in t:
#     if type(i) == int:
#         int_typ_lst.append(i)
#     elif type(i) == float:
#         float_typ_lst.append(i)
#     elif type(i) == complex:
#         complex_typ_lst.append(i)
#     elif type(i) == str:
#         string_typ_lst.append(i)
#     elif type(i) == bool:
#         boolean_typ_lst.append(i)
#
# int_typ = tuple(int_typ_lst)
# float_typ = tuple(float_typ_lst)
# complex_typ = tuple(complex_typ_lst)
# string_typ = tuple(string_typ_lst)
# boolean_typ = tuple(boolean_typ_lst)
#
# print('int_typ-->', int_typ)
# print('float_typ-->', float_typ)
# print('complex_typ-->', complex_typ)
# print('string_typ-->', string_typ)
# print('boolean_typ-->', boolean_typ)


"""WPS to compare two tuples, wheather they contain same elements in any order or not """

# t1=(10,20,30,40,2,6,5,9)
# t2=(20,2,6,5,11,13,6,12)
#
# lst=[]
# j,k=0,0
# while j<len(t1) and k<len(t2):
#     if t1[j] == t2[k] :
#         lst.append(t1[j])
#         k+=1
#     else:
#         j+=1
#
# make_tuple=tuple(lst)
# print('make_tuple-->',make_tuple)


"""WPS to compare two tuples, wheather they contain same elements in sameorder or not """
# t1 = (20, 10, 30, 5, 2, 6, 19, 9)
# t2 = (20, 2, 6, 5, 11, 13, 19, 12)
#
# lst = []
# j, k = 0, 0
# while j < len(t1) and k < len(t2):
#     if t1[j] == t2[k] and t1.index(t1[j]) == t2.index(t2[k]):
#         lst.append(t1[j])
#         k+=1
#         j += 1
#     else:
#         j += 1
#         k += 1
#
# make_tuple = tuple(lst)
# print('make_tuple-->', make_tuple)


"""WPS to find the greatest number from tuple int values"""
# inp=eval(input('Enter comma separate numbers\n'))
# print('the greatest number from tuple int values-->',max(inp))

"""WPS to check wheather tuple is a subset of another tuple or not"""
# x = (1, 2, 3)
# y = (1, 2, 3, 4, 5, 6)
#
# z=''
#
# if len(x) < len(y):
#     z = 'x'
# elif len(y) < len(x):
#     z = 'y'
#
# lst = []
# j, k = 0, 0
#
# while j < len(x) and k < len(y):
#     if x[j] == y[k]:
#         lst.append(x[j])
#         k += 1
#     else:
#         j += 1


# if len(lst) > 0:
#     sub_set_element = tuple(lst)
#     print('sub set elements-->', sub_set_element,'\nthe subset is --',z )
# else:
#     print('this is not a subset')


"""WPS to count the frequency of elements of tuple"""

# t1=(10,20,30,1,10,20,3,60,50,10,20,30,10,50,60,100,90)
# z=[]
# for i in t1:
#     if i not in z:
#         z.append(i)
#         print('frequency of ',i,'in this tuple-->',t1.count(i))