#Source: py4e.com lessons 3 and Book/Libretexts.org Chapter 2 https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Python_for_Everybody_4e_(Severance)/02%3A_Variables_Expressions_and_Statements/2.0E%3A_2.E%3A_Variables_Expressions_and_Statements_(Exercises)
#Teacher/Creator: Chuck Severance
#Course: Programming for Everybody (PY4E)
#Lesson: 02 - Variables, expressions and statements
#Copyright Creative Commons Attribution 4.0
#Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.


#Source - CalculatorSoup.com https://www.calculatorsoup.com/calculators/conversions/celsius-to-fahrenheit.php
# Celsius °C to Fahrenheit °F Formula
#°F equals °C multiplied by 9/5, plus 32.
#°F = °C * 9/5 + 32
#Alternatively, since 9/5 = 1.8 we can say °F equals °C multiplied by 1.8, plus 32.
#°F = °C * 1.8 + 32

print ('Hello and Welcome, to my Celsius to Fahrenheit Converter')

c = input ('What Temperature in Celsius(°C) would you convert? \n') # c = Celsius

f = float(c) * 1.8 + 32 # f = Fahrenheit

print (f'{c} Celsius is equal to {f} Fahrenheit')
