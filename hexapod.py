from leg import Leg
import time


class Hexapod:
    def __init__(self):
        self.legs = []
        self.num_legs = 4
        self.initialise_legs()

    def move(self, direction):
        if direction == 'forward':
            self.move_forward()
        elif direction == 'backward':
            print('Moving backward')
    
    def move_forward(self):
        while True:
            # Initial position
            x, y, z = 60, -60, -74
            # Move for 3 seconds, incrementing every 100ms
            while True:
                self.legs[0].move_to_position([x, y, z])
                time.sleep(1)
                self.legs[0].move_to_position([85, 0, -74])
                time.sleep(1)
                self.legs[0].move_to_position([60, 60, -74])
                time.sleep(1)
                self.legs[0].move_to_position([60, 60, -74])
                time.sleep(1)
                # the lifting part was 52
                self.legs[0].move_to_position([96.8, 96.8, 52])
                time.sleep(1)
                self.legs[0].move_to_position([137, 0, 52])
                time.sleep(1)
                self.legs[0].move_to_position([96.8, -96.8, 52])
                time.sleep(1)


    def initialise_legs(self):
        for i in range(self.num_legs):
            leg = Leg(i)
            self.legs.append(leg)

        