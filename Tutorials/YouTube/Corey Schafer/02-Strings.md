---
Chanel: Corey Schafer
Video Title: "Python Tutorial for Beginners 2: Strings - Working with Textual Data"
Description: In this Python Beginner Tutorial, we will begin learning about the string data type. Strings allow us to work with textual data in Python. We will be going over different ways to format strings, and a
Course Link: https://youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&si=NAqPVHNCkd3uHpKq
Video Link: https://youtu.be/k9TUPpGqYTo
Related File: 02 - Strings.py
published:
tags:
  - python
  - youtube
  - learning
  - notes
  - variables
  - Strings
  - str
  - Length
  - len
  - Indexing
  - Slicing
  - Concatenation
  - String_Formatting
  - F-strings
  - Documentation
---
# Variable Naming Conventions
---
## Conventions

- Variables are usually all lowercase 
- If a Variables has multiple words then we separate those with underscore ( _ )
- Variable names should be as descriptive as possible

``` python
message = "Hello World"
my_message = "Hello, Nick!"

pi=3.14

print(message)
print(my_message)
print(pi)
```
## Bad Practices

- Single Letter
	  May be valid variable name, but if anyone reads the code now wouldn't know what value it's supposed to hold

```python
m = "Hello World"

print(m)
```
# String Quotes and Escaping
---
## String Quotes
Strings can made by using Single( ' ' ) or double( " " ) quotes.

```python
print('Hello World')
print("Hello World")
```

You can alternate quotes depending on the text going in the string. 

```python
print('He said, "Hello World"')
print("Bobby's World!")
```

Using the same quotes make will make the interrupter think the string is ends before it does. which will lead to a, SyntaxError: invalid syntax.

```python
print('Bobby's World!)

```

## Escaping
You can use a backslash( \ ) escape or tell the interrupter to not to use that quote to close the string.

```python
print('Bobby\'s World!')
print("He said, \"Hello World\"")
```

# Multi-line Strings
---
By using three quotes you can print on multi-line 
You can use Single( ''' ) or double( """ ) quotes

```python
print("""
1,
2,
3,
""")
```

# String Length and Indexing
---
## Length
You can use len( ) to find the length, the number of characters, in a string or variable but adding inside the brackets as an argument.

Arguments are values you pass into a function or method using parentheses ( )

```python

print(len(message))

print(len("""Bobby's World
was a popular animated television show
that aired from 1990 to 1998. """))
```

## Indexing
Every character in a variable is index with a number starting with 0. 

We can print the characters by know it's index, and putting it in square brackets ( \[ ] )

So with our message the letter of the first index (index 0) is H and our last letter (index10) is d

```python

print(message[0])

print(message[10])

```

If we try to print an index that's not in the range/doesn't exist, of our message, we get an... 
IndexError: string index out of range

```python
print(message[11])
```

# Slicing Strings
---
If we only want part of our message, or variable, let say we only want Hello. Then in square brackets ( \[ ] )  we can add the first index we want (H or 0) a colon ( : ) and the last index we want ( o or 4) +1 (5)

```python
print(message)
print(message[0:5])
```

now we could leaving a blank before the colon ( : ) this will let python know to start at index 0 or H 

```python
print(message[ :5])
print(message[:5])
```

The same thing goes for the last index, if leaving a blank after the colon ( : ). If we want World, we would enter index 6 (W) and python will go to the end. 

```python
print(message[6: ])
print(message[6:])
```

# Useful String Methods
---
A Method is like a function that belongs to an object, like a variable. It performs a task on the object

## .lower() and .upper()
If we want our variable (message) to all lower case, we can add .lower() behind it.
For all upper case, we add .upper()

```python
print(message)
print(message.lower())
print(message.upper())
```

## .count()
If we wanted to know how many time a word or character is used, we can use .count() and put the word or character in the brackets ( ) as an argument.

```python
print(message)
print(message.count('Hello'))
print(message.count('l'))
```

# .find()


```python
print(message)
print(message.find('World'))
print(message.find('Universe'))
```

# Replacing String Content
---


```python
new_message = message.replace('World', 'Universe')
print(message.replace('World', 'Universe'))
print(new_message)
```

# String Concatenation
---


```python
greeting = "Hello"
name = "Michael"
greeting_message = greeting + ", " + name

print (greeting)
print (name)
print (greeting_message)
print (greeting + ", " + name)
print (greeting + ", " + name + ". Welcome!")
```

# String Formatting
---


```python
format_greeting = "{}, {}. Welcome!".format(greeting, name)

print(format_greeting)
```

# Using F-strings
---


```python
f_string_greeting = f"{greeting}, {name}. Welcome!"

print(f_string_greeting)
print(f"{greeting}, {name.upper()}. Welcome!")
```

# Built-in Documentation
---


## dir()
```python
print(dir(name))
```


## help()
```python
print(help(str))
```



```python
print(help(str.lower))
```