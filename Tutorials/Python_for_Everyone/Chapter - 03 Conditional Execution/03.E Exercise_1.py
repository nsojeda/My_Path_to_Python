#---
#title: "3.E: Conditional Execution (Exercises)"
#source: "https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Python_for_Everybody_4e_(Severance)/03%3A_Conditional_Execution/3.0E%3A_3.E%3A_Conditional_Execution_(Exercises)"
#author:
#  - "[[Libretexts]]"
#published: 2017-12-17
#created: 2026-11-19
#description:

#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# my solution

hrs = input("Enter Hours: ")
h = float(hrs)

rate = input("Enter Rate: ")
r = float(rate)

if h > 40 :
    ot = h - 40 #ot = over time
    ot_rate = r * 1.5
    pay = (40 * r) + (ot * ot_rate)
else :
    pay = float(hrs) * float(rate)

print('Pay: ' + str(pay))
