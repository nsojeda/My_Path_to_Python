---
Chanel: Corey Schafer
Video Title: "Python Tutorial for Beginners 3: Integers and Floats - Working with Numeric Data"
Video Description: In this Python Beginner Tutorial, we will begin learning about integers and floats. Integers and Floats allow us to work with numeric data in Python. We will be learning how to perform basic arithmetic, as well as how to compare numeric values. Let's get started.
Course Link: https://youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&si=NAqPVHNCkd3uHpKq
Video Link: https://youtu.be/khKv-8q7YmY
Related File: 03-Integers and Floats.py
published:
tags:
  - python
  - youtube
  - learning
  - notes
  - Integers
  - Floats
  - type_casting
---
# Introduction and Basics
---

Notes

```python
num = 3
num1 = 3.14

print(num)
print(type(num))

print(num1)
print(type(num1))
```

https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Ints/snippets.txt
Arithmetic Operators: 
	Addition: 3 + 2
	Subtraction: 3 - 2
	Multiplication: 3 * 2
	Division: 3 / 2
	Floor Division: 3 // 2
	Exponent: 3 ** 2
	Modulus: 3 % 2

```python
print('Addition: 3 + 2')
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
```

**Test/Extra Exercises Not in Video**

```python
print('Exponent: 3 ** 3')
print(3 ** 3)

print('Division: 10 / 2')
print(10 / 2)

print('Subtraction: 1 - 2')
print(1 - 2)

print(type(1-2))
```

# Module Arithmetic
---

notes

```python
print('Modulus: 2 % 2')
print(2 % 2)

print('Modulus: 3 % 2')
print(3 % 2)

print('Modulus: 4 % 2')
print(4 % 2)

print('Modulus: 5 % 2')
print(5 % 2)
```

**Test/Extra Exercises Not in Video**

```python
print('Modulus: 2 % 3')
print(2 % 3)

print('Modulus: 3 % 3')
print(3 % 3)

print('Modulus: 4 % 3')
print(4 % 3)

print('Modulus: 5 % 3')
print(5 % 3)

```

# Order of Operations
---

```python
print(3*2+1)
print(3*(2+1))
```

**Test/Extra Exercises Not in Video**

```python
print(3*(2+1)/(2-1))
print(3*2+1/2-1)
```

# Incrementing Variables
---

```python
num2 = 1
print(num2)

num2 = num2 + 1
print(num2)

num2 += 1
print(num2)

num2 *= 10
print(num2)
```

**Test/Extra Exercises Not in Video**
Incrementing Variables: 
	Addition: x += 2
	Subtraction: x -= 2
	Multiplication: x *= 2
	Division: x /=2
	Floor Division: x //= 2
	Exponent: x \*\*= 2
	Modulus: x %= 2
	
```python
x=10
print(x)

x += 2
print(x)

x -= 2
print(x)

x *= 2
print(x)

x /=2
print(x)

x //= 2
print(x)

x **= 2
print(x)

x %= 2
print(x)
```

# Built-in Number Functions
---

```python
print(abs(-3))

print(round(3.75))

print(round(3.75,1))
```

**Test/Extra Exercises Not in Video**

```python
print(abs(num2))
```

# Comparison Operators
---

https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Ints/snippets.txt
Comparisons:
    Equal:            3 == 2
    Not Equal:        3 != 2
    Greater Than:     3 > 2
    Less Than:        3 < 2
    Greater or Equal: 3 >= 2
    Less or Equal:    3 <= 2


```python
num3 = 3
num4 = 2

print(num3 == num4)
print(num3 != num4)
print(num3 > num4)
print(num3 < num4)
print(num3 >= num4)
print(num3 <= num4)
```

**Test/Extra Exercises Not in Video**

```python
print(num2)
print(num4)

print(num2 == num4)
print(num2 != num4)
print(num2 > num4)
print(num2 < num4)
print(num2 >= num4)
print(num2 <= num4)
```

# Type Casting
---

```python
num5 = '100'
num6 = '200'

print(num5 + num6)

num7 = '100'
num8 = "200"

num7 = int(num7)
num8 = int(num8)

print(num7 + num8)
```

**Test/Extra Exercises Not in Video**

```python
print(int(num5) + int(num6))

print(int(num5 + num6))

print(int(num2) + num8)
```