# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class Person:

    def __init__(self, name, birthdate):
        self.name = name

        if birthdate < 0 or birthdate > 2016:
            self.birthdate = birthdate
        else:
            raise ValueError
