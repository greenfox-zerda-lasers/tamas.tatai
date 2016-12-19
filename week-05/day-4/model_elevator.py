# Create an "elevator" class
# The class should track the following things:
#  - elevator position // 0-11
#  - elevator direction // nem kell!
#  - people in the elevator // count, >= 0
#  - add people // max, +1
#  - remove people // min, -1

class Elevator:
    data = {}
    def __init__(self):
        self.data = {
        'position': 7,
        'el_people': 1,
        'top_floor': 11
        }

    def add_people(self):
        self.data['position'] += 1

    def remove_people(self):
        self.data['position'] += 1
