% Object Oriented Programming in Python
% Exercises

# Exercise 01
Define a class `Vehicle`.
Each vehicle instance should have following attributes:
    - production_year
    - make

_Tips_
- remember that instance attributes must be defined inside the `__init__()` function.

# Exercise 02
## Step 1
Define classes `Car` and `Truck`.
Both should extend the class `Vehicle`.

## Step 2
Define additional attribute `color` that will be available in each `Car` instance.

## Step 3
Define additional attribute `max_load` that will be available in each `Truck` instance.

## Step 4
Define a method `repaint()` for each `Car` instance.
This method should take a single argument - the color name and change the value of the `color` attribute of the instance.


# Exercise 03
In the `ex01.py` there is the "Paper, rock, scissors" game implementation. This implementation makes use of Object Oriented Programming 
mechanisms.

## Step 1
Together with the tutor analyse what concept are used and what is the purpose.

## Step 2
Implement `HumanPlayer` class so it can be used as a second player in the game.
The `HumanPlayer` class should conform to the `Player` class interface.

`get_name()` method should let the player enter their name from the keyboard and return it.
`next_move()` method should let the player enter their move choice. The possible choices are 'p', 'r' or 's' for 
paper, rock or scissors respectively. It should validate the input and return the choice only if it is one of the valid letters.

## Steps 3
How the code can be changed so the game is played by 2 computer players?
Apply necessary changes.

