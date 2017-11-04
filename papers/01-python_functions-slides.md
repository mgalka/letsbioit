% Python

# Procedural programming in Python

## What are functions?
- Function is a sequence of programming language instructions that perform a specific task.
- Function can be called whenever this task should be performed.
- Function may return a value.
- The returned value may be used as any other value in the program e.g. assigned to a variable.


## Function definition in Python
~~~python
def new_book(title, author, cover_type='paperback',
             available=True):
    # ... do stuff
    return result
~~~
- Functions in Python are defined with the keyword `def`.
- Each function has a parameter list defined in parenthesis.
- Parameter list may be empty, but the parethesis are mandatory.
- There are 2 types of parameters:
    - positional
    - keyword

## Function definition in Python
~~~python
def new_book(title, author, cover_type='paperback',
             available=True):
    # ... do stuff
    return result
~~~
- A `return` statement breaks function execution at the line where it is used.
- Value placed after the `return` statement becomes function value.

## Function call
- Function is called by specifying its name 

## Parameters vs. arguments
- A **parameter** is a variable which is a part of the function signature.
- An **argument** is a value or expression used when calling the function.
- Each function **has** parameters and **takes** arguments.   

## Positional arguments
~~~python
def new_book(title, author, cover_type='paperback', available=True):
    # ... do stuff
    return result

new_book('The Lord of the Rings', 'J. R. R. Tolkien')
~~~
- Positional arguments are mandatory.
- Every positional argument is assigned to a respective positional parameter.

## Keyword arguments
~~~python
def new_book(title, author, cover_type='paperback', available=True):
    # ... do stuff
    return result
new_book('The Lord of the Rings', 'J. R. R. Tolkien', available=True)
new_book('The Lord of the Rings', 'J. R. R. Tolkien',
        'hardcover', True)
new_book('The Lord of the Rings', 'J. R. R. Tolkien', 'hardcover')
new_book('The Lord of the Rings', 'J. R. R. Tolkien')
~~~
- May be supplied in random order, when each argument explicitly assigned to a key.
- They always have default values defined so may be omitted in the function call.
- May be supplied as positional arguments when they can be unambigously assigned to the parameters.

## Keyword arguments and default values
~~~python
def new_book(title, author, cover_type='paperback', available=True):
    # ... do stuff
    return result
new_book('The Lord of the Rings', 'J. R. R. Tolkien',
         available=True)
~~~
- Keyword parameters **must** be defined **after** the positional ones.
- Default value assignment occurrs at the **moment of the definition not at the moment of function call**.
- As a consequence, usage of a mutable object as a default value will result in usage of **the same** object during each function call.

## Problemy z wartościami domyślnymi - przykład
~~~python
def append_to(element, to=[])
    to.append(element)

append_to(1)
[1]
append_to(2)
[1,2]
~~~

## Arbitrary number of arguments
~~~python
def print_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for kw, kwarg in kwargs.items():
        print('{}={}'.format(kw, kwarg))
~~~
- `*args` - An arbitrary number of positional arguments.
- `**kwargs` - An arbitrary number of keyword arguments.
- `args` and `kwargs` may be empty.
- In the function body:
    - `args` - A tuple of all positional arguments.
    - `kwargs`- A dictionary of all keyword arguments.

## Arbitrary number of arguments
~~~python
def print_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for kw, kwarg in kwargs.items():
        print('{}={}'.format(kw, kwarg))
~~~

---

~~~python
print_args('a','b','c',first=1, second=2, third=3)
a
b
c
second=2
first=1
third=3
~~~
