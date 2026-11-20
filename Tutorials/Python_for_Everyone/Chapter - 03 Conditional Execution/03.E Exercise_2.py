#---
#title: "3.E: Conditional Execution (Exercises)"
#source: "https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Python_for_Everybody_4e_(Severance)/03%3A_Conditional_Execution/3.0E%3A_3.E%3A_Conditional_Execution_(Exercises)"
#author:
#  - "[[Libretexts]]"
#published: 2017-12-17
#created: 2026-11-19
#description:

#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input

#Enter Hours: forty
#Error, please enter numeric input




# my solution

hrs = input("Enter Hours: ")
try:
    h = float(hrs)
except:
    print('Error, please enter numeric input')
    exit()

rate = input("Enter Rate: ")
try:
    r = float(rate)
except:
    print('Error, please enter numeric input')
    exit()

if h > 40 :
    ot = h - 40 #ot = over time
    ot_rate = r * 1.5
    pay = (40 * r) + (ot * ot_rate)
else :
    pay = float(hrs) * float(rate)

print('Pay: ' + str(pay))
