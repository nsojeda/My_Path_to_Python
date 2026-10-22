#Source: py4e.com
#Teacher/Creator: Chuck Severance
#Course: Programming for Everybody (PY4E)
#Lesson: 03 - Variables, expressions and statements
#Copyright Creative Commons Attribution 4.0
# Exercise 2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.


#Provide Code

#----------------------#
# This first line is provided for you

# hrs = input("Enter Hours:")
#----------------------#


# my solution

hrs = input("Enter Hours: ")

rate = input("Enter Rate: ")

pay = float(hrs) * float(rate)

print('Pay: ' + str(pay))