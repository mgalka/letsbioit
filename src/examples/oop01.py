class Human:
    def __init__(self, first_name, last_name, age, sex):
        # These are instance attributes.
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def say(self, sentence):
        print('{} SAYS {}'.format(self.first_name,
                                  sentence))

    def lift(self, weight):
        print('{} LIFTS {} {}'.format(self.first_name,
                                      weight.weight, weight.unit))

class Weight:
    # This is a class attribute.
    conversion_table = {
      'kg': {
                'lbs': 0.45359237
      },
      'lbs': {
         'kg': 2.20462262
      }
    }

    def __init__(self, weight, unit='kg'):
        self.weight = weight
        self.unit = unit

    def convert_to(self, new_unit):
        ratio = self.conversion_table[self.unit][new_unit]
        converted_weight = self.weight * ratio
        return converted_weight

# Create class instances
john = Human('John', 'Doe', 28, 'M')
jane = Human('Jane', 'Doe', 24, 'F')


# Let's see if they're really different objects
print(id(john))
print(id(jane))

john.say('Python')

# Accessing class attributes
print(Weight.conversion_table)
# print(Weight.weight)
w = Weight(120)
x = Weight(180)
Weight.conversion_table['kg']['lbs'] = 10000000
print(w.conversion_table, w.weight)
print(x.conversion_table, x.weight)
print(Weight.conversion_table)
