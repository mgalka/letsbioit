% Procrdural programming in Python
% Exercises

# Exercise 01
Implement a function named `square` that will return a given argument to the power of 2.

_Tips_

- `**` is the power operator in python.
```python
# Calculate 2 to the power of 3
2 ** 3  
# Calculate 4 to the power of 3
# and assign the result to the variable a
a = 4 ** 3  
```

# Exercise 02
Write a function `my_sum` that takes a list of numbers as an argument and return their sum.

_Tips_

- Lists in python are declared as a comma separated sequences in square brackets.
- Lists can be iterated over with a `for` loop.
- List can consist of any type of values.

```python
list_of_numbers = [1, 2, 3]
list_of_words = ['dog', 'cat', 'apple']
other_list = [1, 2, 'd', 1.3, None, True]

for num in list_of_numbers:
    print(num)

# Result:
# 1
# 2
# 3
```

# Exercise 03
Write a function `remove_negative`.
The function should take a list of numbers as an argument and return a new list as a result.
The returned list should contain only positive numbers from the list provided as an argument.

_Tips_

- To branch the code execution due to a logical condition use the `if` instruction.
- To add element to the list use it's `.append()` method.
```python
l = []
l.append(1)
print(l)
# prints [1]

k = [1, 2]
k.append(3)
print(k)
# prints [1, 2, 3]

a = 9
if a != 10:  # != means is not equal
    print('a is not equal 10')
else:
    print('a is equal 10)
# expected result:
# a is not equal 10
```

# Exercise 04
Write a function `minimum_value`.
The function should take a list of numbers as an argument and return a single number value.
Returned value should be the smallest number from the list provided as an argument.

# Exercise 05
Write a function `reverse_words`.
The function should take a string parameter and return new string.
The input string should be a sentence.
Returned string should be the same sentence, but each word should have the letters in reversed order.

_Example_

For a string 'Quick brown fox' the result string should be 'kciuQ nworb xof'.

```python
s = 'Quick brown fox'

print(reverse_words(s))
# kciuQ nworb xof
```

_Tips_

- String is an iterable type in Python.
- You can easily get a reversed copy of the string using the extended slice operator.
- To convert a sentence to a list of words you may use the built-in string `split()` method.
    - When no parameter is provided to `split()` it'll try to get the largest possible continuous sequence of white characters.

```python
s = 'Quick brown fox'
words = s.split()
print(words)
# ['Quick', 'brown', 'fox']

s = 'BioIT'
rev = s[::-1]

print(rev)
# TIoiB
```

# Exercise 06
Write a function `swap_first_last`.
The function should take a string containing a sentence as an input parameter.
The function should return a string.
Returned string should contain the same sentence, but with swapped first and last word.

_Example_

For an input string 'Quick brown fox jumps' the function should return 'jumps brown fox Quick'

_Tips_

- You can use a `+` operator to concatenate strings.
- You can access list elements with an index provided in square brackets.
- Slice operator may be useful to get several words from the list

```python
l = ['Quick', 'brown', 'fox']
print(l[0])
# Quick

print(l[1])
# brown

print(l[-1])
# fox

print(l[:-1])
# ['Quick', 'brown']

print(l[1:])
# ['brown', 'fox']

a = 'Python'
b = 'language'
c = a + ' is a programming ' + b

print(c)
# Python is a programming language

k = l[0] + ' ' + l[-1]

print(k)
# Quick fox
```

# Exercise 07
Write a function `icompare`.
The function should take two strings as input parameters.
The function should return `True` or `False`.
Returned value should be `True` when input parameters are equal otherwise it should return `False`
**The comparison should should be case insensitive**

_Example_

For input strings 'Quick' and 'quicK' the result should be `True`.
For input strings 'Quick' and 'QUICK' the result should be `True`.
For input strings 'fox' and 'duck' the result should be `False`.

_Tips_

- Each string has a build-in methods `upper()` and `lower()` which return appropriately upper cased and lower cased string.
- Strings can be compared with a `==` operator, but this one **is case sensitive**.

```python
a = 'Python'

a_upper = a.upper()
print(a_upper)
# PYTHON

a_lower = a.lower()
print(a_lower)
# python
```
