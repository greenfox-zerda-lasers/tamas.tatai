# Create an elevator controller class
# It should take a user input by listening to user input
# List of commands:
#
#  - Move elevator up
#  - Move elevator down
#  - Add people
#  - Remove people
#
#  Features to implement:
#   - Always draw the state of the elevator as depicted in "art.txt"
#   - [ x ] is the elevator. X means it has at least 1 person inside
#   - Moving floors should take time
#   - don't move beyond limits
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects

import model_elevator
import view_elevator

class Controller:

    def __init__(self):
        self.model = model_elevator.Elevator()
        self.view = view_elevator.DisplayElevator()

    def test(self):
        self.view.display(self.model.data)

test_el = Controller()
test_el.test()

    # def get_input(self):
    #     pass
    #
    # def get_command(self):
    #     command =
