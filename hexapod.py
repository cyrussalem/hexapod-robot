from leg import Leg


class Hexapod:
    def __init__(self):
        self.legs = []
        self.num_legs = 4
        self.initialise_legs()

    def move(self, direction=None):
        self.legs[0].move_to_position([159, 0, 0])

    def initialise_legs(self):
        for i in range(self.num_legs):
            leg = Leg(i)
            self.legs.append(leg)

        