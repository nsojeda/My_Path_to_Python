'''
Source: YouTube
Channel: Corey Schafer
Course: Python Programming Beginner Tutorials
Title: Python Tutorial for Beginners 3: Integers and Floats - Working with Numeric Data
Description: from Video - In this Python Beginner Tutorial, we will begin learning about integers and floats. Integers and Floats allow us to work with numeric data in Python. We will be learning how to perform basic arithmetic, as well as how to compare numeric values. Let's get started.
This is a scratchpad of snippets for this source.
See matching .md for my notes.
'''
hr = "----------------------"

print('\n\n')
print(hr)
print('Introduction and Basics')
print(hr)
print('\n\n')

num = 3
num1 = 3.14
print(num)
print(type(num))

print(num1)
print(type(num1))

# https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Ints/snippets.txt
# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

print('\n\nAddition: 3 + 2')
print(3 + 2)
print('Subtraction: 3 - 2')
print(3 - 2)
print('Multiplication: 3 * 2')
print(3 * 2)
print('Division: 3 / 2')
print(3 / 2)
print('Floor Division: 3 // 2')
print(3 // 2)
print('Exponent: 3 ** 2')
print(3 ** 2)

print('\n')
print(hr)
print('Test/Extra Exercises Not in Video')
print('Exponent: 3 ** 3')
print(3 ** 3)
print('Division: 10 / 2')
print(10 / 2)
print('Subtraction: 1 - 2')
print(1 - 2)
print(type(1-2))
print(hr)
print('\n')

print('\n\n')
print(hr)
print('Module Arithmetic')
print(hr)
print('\n\n')

print('Modulus: 2 % 2')
print(2 % 2)
print('Modulus: 3 % 2')
print(3 % 2)
print('Modulus: 4 % 2')
print(4 % 2)
print('Modulus: 5 % 2')
print(5 % 2)

print('\n')
print(hr)
print('Test/Extra Exercises Not in Video')
print('Modulus: 2 % 3')
print(2 % 3)
print('Modulus: 3 % 3')
print(3 % 3)
print('Modulus: 4 % 3')
print(4 % 3)
print('Modulus: 5 % 3')
print(5 % 3)
print(hr)


print('\n\n')
print(hr)
print('Order of Operations')
print(hr)
print('\n\n')

print(3*2+1)
print(3*(2+1))

print('\n')
print(hr)
print('Test/Extra Exercises Not in Video')

print(3*(2+1)/(2-1))
print(3*2+1/2-1)

print(hr)
print('\n')

print('\n\n')
print(hr)
print('Incrementing Variables')
print(hr)
print('\n\n')

num2 = 1
print(num2)
num2 = num2 + 1
print(num2)

num2 += 1
print(num2) 

num2 *= 10
print(num2)

print('\n')
print(hr)
print('Test/Extra Exercises Not in Video')

print(num2)
num2 /= 10
print(num2)
num2 -= 1
print(num2)

print(hr)
print('\n')

print('\n\n')
print(hr)
print('Built-in Number Functions')
print(hr)
print('\n\n')

print(abs(-3))
print(round(3.75))
print(round(3.75,1))


print('\n')
print(hr)
print('Test/Extra Exercises Not in Video')

print(abs(num2))

print(hr)
print('\n')

print('\n\n')
print(hr)
print('Comparison Operators')
print(hr)
print('\n\n')

# https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Ints/snippets.txt
# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num3 = 3
num4 = 2
print(num3 == num4)
print(num3 != num4)
print(num3 > num4)
print(num3 < num4)
print(num3 >= num4)
print(num3 <= num4)

print('\n')
print(hr)
print('Test/Extra Exercises Not in Video')

print(num2) 
print(num4)
print(num2 == num4)
print(num2 != num4)
print(num2 > num4)
print(num2 < num4)
print(num2 >= num4)
print(num2 <= num4)

print(hr)
print('\n')

print('\n\n')
print(hr)
print('Type Casting')
print(hr)
print('\n\n')

num5 = '100'
num6 = '200'

print(num5 + num6)

num7 = int(num5)
num8 = int(num6)
print(num7 + num8)

print('\n')
print(hr)
print('Test/Extra Exercises Not in Video')


print(int(num5) + int(num6))
print(float(num5) + float(num6))
print(float(num5) + int(num6))

print(hr)
print('\n')