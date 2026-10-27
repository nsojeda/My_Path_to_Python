---
tags:
  - python
  - coding
  - programing
---

```python
print("Hello World")
```

The classic first program for all programs

"print" is function that can display a programs output on the screen.

# Strings

A string is a sequence of characters.
A character is a single symbol such as a letter, number, punctuation, space, etc.
Strings are also a data type.

They are enter/writing inside " " or ' '.

```python
print('Hello World')
print ("Hello Python")
```

You may need to alternate "" and '' to use the other so python doesn't get confuse

```python
print('Nick said "Python is fun"')
print("That's Nick's computer")
```

 \ or brake can stop python from thinking the string has ended.

```python
print('That\'s Nick\'s computer')
```

but it can also, brake a code line and let it continue on the next line.

```python
print('A, B, C,')
print('A,\

B, \

C')
```

\n = line brake print 2 lines with a space between.

```python
print ('Hello')
print ('World')

print('Hello \n')
print('World')
```

## Concatenation
---
Concatenation is the combining of strings/variables with a "+" or a ",".
 "+" will not put in a space between a strings/variables.
 "," will put a space between variables

```python
name=("Nick")
hello=("Hello")

print (hello + name)
print (hello,name)
print (hello + ", " + name)
print (name,"is the man")
print (name+" is the man")
```

A number inside "\[ ]" after a string variables will give you that letters.
print (name[1])
print("the fist letter in",name, "is",name[0])

 to get a range of letters. enter the number of the fist letter then a ":" and the number of the last letter plus 1

print (name[1:3])

print (name[1:4])

# to find the length of a strings/variables, type "len()" entering a strings/variables

print (len(name))

# method work on an objected by uses a " . "

".find(" ") to see if a strings/variables contains a string. what you are looking for.# if it contains what you are looking for you'll get a 0. if not you'll get -1

print (name.find("Nick"))

print (name.find("z"))

print (name.find("1"))

print ("z = zero".find("z"))

print ("1,2,3".find("1"))

print("")

print (name.lower())

print (name.upper())

print("")

print (name.count("Nick"))

print (name.count('Zero'))

print (name.count('i'))

print("")

print ("I am iron man")

print ("I am Tony")

print ("I am whoever I say I am")

print("")

print ("""1

2

3""")

print("")

print("4 \n" + "5 \n" + "6")

print('')

print('''7

8

9''')

print('')

print('''10 \

11 \

12''')
