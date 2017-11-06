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


# Exercise 05