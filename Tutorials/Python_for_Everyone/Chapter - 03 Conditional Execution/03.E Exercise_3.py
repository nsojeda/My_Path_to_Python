#---
#title: "3.E: Conditional Execution (Exercises)"
#source: "https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Python_for_Everybody_4e_(Severance)/03%3A_Conditional_Execution/3.0E%3A_3.E%3A_Conditional_Execution_(Exercises)"
#author:
#  - "[[Libretexts]]"
#published: 2017-12-17
#created: 2026-11-19
#description:

#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
# < 0.6    F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F

# my solution

score = input("Enter Score:")
try:
    s = float(score)
    s < 1
except:
    print("Score must be 1 or less")
    score = input("Enter Score:")

if s>= 0.9 :
    print ("A")
elif s>= 0.8:
    print("B")
elif s>= 0.7: 
    print("C")
elif s>= 0.6:
    print("D")
elif s < 0.6:
    print("F")