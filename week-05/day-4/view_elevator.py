# Create a class the displays the Elevator art and navigation (list of commands)

import os

class DisplayElevator:
    def __init__(self):
        self.art = {
        'ground': "  .'_______________________________'.",
        'floor_0': "    _||_||_[_{0}_]_||_||_______||_||_",
        'floor_1': "    _||_||_______||_||_______||_||_",
        'empty_floor': "     || ||       || ||       || ||",
        'elevator_floor':"     || || [_{0}_] || ||       || ||",
        'top': "  ___________________________________\n  '._______________________________.'"
        }

    def display(self, data):
        os.system('cls' if os.name == 'nt' else 'clear')
        print (self.art['top'])

        for x in range(data['top_floor'], -1, -1):
            if x == data['position'] and data['position'] == 0:
                print (self.art['floor_0'].format(self.people_in_el(data)))
            elif x == data['position']:
                print (self.art['elevator_floor'].format(self.people_in_el(data)))
            else:
                if data['position'] != 0 and x == 0:
                    print (self.art['floor_1'])
                else:
                    print (self.art['empty_floor'])

        print (self.art['ground'])

    def people_in_el(self, data):
        if data['el_people'] == 0:
            return '_'
        else:
            return 'X'

# draw_el = DisplayElevator()
