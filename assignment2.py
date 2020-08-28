"""WPS to check wheather a given number is even or odd."""
# inp=int(input('Enter a number\n'))
# if inp%2==0:
#     print('Even Number')
# else:
#     print('Odd Number')


"""WPS to check wheather a given number is divisible by 5 or not."""

# inp=float(input('Enter a number\n'))
# if inp%5==0:
#     print('Divisible')
# else:
#     print('Not Divisible')


"""WPS to check wheather a given number is positive , negative or zero."""

# inp=float(input('Enter a number\n'))
#
# if inp>0:
#     print('positive number')
# elif inp<0:
#     print('negative number')
# else:
#     print('Zero')


"""WPS to find greatest among three numbers."""

# inp1,inp2,inp3=int(input('Enter First Number\n')),int(input('Enter Second Number\n')),int(input('Enter Third Number\n'))
#
# if inp1>inp2>inp3:
#     print('Num 1 is greatest among three nos')
# elif inp2>inp1>inp3:
#     print('Num 2 is greatest among three nos')
# elif inp3>inp1>inp2:
#     print('Num 2 is greatest among three nos')


"""WPS to check if a year is leap year or not."""
#
# inp = int(input('Enter year\n'))
#
# if inp % 4 == 0 and inp % 100 == 0 and inp % 400 == 0:
#     print('leap year',inp)
# else:
#     print('Not a leap year')

# year = int(input("Enter a year: "))
#
# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("{0} is a leap year".format(year))
#        else:
#            print("{0} is not a leap year".format(year))
#    else:
#        print("{0} is a leap year".format(year))
# else:
#    print("{0} is not a leap year".format(year))


"""WPS to make month value numeric format and display number of days in it."""

# month=int(input('Enter Month Number Between 1-12\n'))
# if month == 1:
#     print('January - 31 days')
# elif month == 2:
#     print('February - 28 days in a common year and 29 days in leap years')
# elif month == 3:
#     print('March - 31 days')
# elif month == 4:
#     print('April - 30 days')
# elif month == 5:
#     print('May - 31 days')
# elif month == 6:
#     print('June - 30 days')
# elif month == 7:
#     print('July - 31 days')
# elif month == 8:
#     print('August - 31 days')
# elif month == 9:
#     print('September - 30 days')
# elif month == 10:
#     print('October - 31 days')
# elif month == 11:
#     print('November - 30 days')
# elif month == 12:
#     print('December - 31 days')
# else:
#     print('Invalid Number')


"""WPS to check nature of roots of a given quadratic equation"""

# equation='x^2-7x+3=0'
# inp=int(input('Enter a number to satisfy quadratic equation x^2-7x+3=0\n'))
# ans=(inp**2)-(7*inp)-8
# print (ans)
# if ans==0:
#     print('equation satisfied')
# else:
#     print('equation not satisfied')

"""WPS to print set of three words in dictionary order. Words are given by the user"""
# first,second,third=input('First word\n'),input('Second word\n'),input('Second word\n')
# my_dict={'first word':first,'Second word':second,'Third word':third}
# print('my_dict-->',my_dict)

"""WPS to accept one complex number from user and display the greater number between real part and imaginary part. """

# inp1,inp2=int(input('Enter first number\n')),int(input('Enter Second number\n'))
# convert_complex=complex(inp1,inp2)
# print('convert_complex -->',convert_complex)
# print('Real Part -->',convert_complex.real)
# print('Imaginary Part -->',convert_complex.imag)

"""WPS to accept marks of five subjects from the user (assuming maximum marks as 100) .
Display students results PASS or FAIL 
.If the student is PASS then only display his percentage or division. (*Min pass mark is 30)"""

mathematics, physics, chem, bio, eng = int(input('Enter math mark\n')), int(input('Enter physics mark\n')), int(
    input('Enter chem mark\n')), int(input('Enter bio mark\n')), int(input('Enter eng mark\n'))
total_marks = 500
min_pass_mark = 30

if mathematics >= min_pass_mark:
    if physics >= min_pass_mark:
        if chem >= min_pass_mark:
            if bio >= min_pass_mark:
                if eng >= min_pass_mark:

                    sum = mathematics + physics + chem + bio + eng

                    if sum > total_marks:
                        print('Enter marks correctly because your total mark crossed 500')
                    elif sum < total_marks:
                        percentage = (sum / total_marks) * 100
                        print('Total scored-->', sum)
                        print('Congratulations you passed with having', percentage, '%')
                else:
                    print('Sorry You are failed in eng')
            else:
                print('Sorry You are failed in bio')
        else:
            print('Sorry You are failed in chem')
    else:
        print('Sorry You are failed in phy')
else:
    print('Sorry You are failed in math')
