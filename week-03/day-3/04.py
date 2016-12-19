# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student():

    grades = []

    def add_grade(self, grade):
        if grade >= 1 and grade <= 5:
            self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)

firpo = Student()
firpo.add_grade(2)
firpo.add_grade(4)
firpo.add_grade(5)
print(firpo.get_average())
