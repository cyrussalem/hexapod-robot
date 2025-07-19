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
                self.gradual_move(self.legs[0], [65, -35, 74], [85, 0, 74], 0.2);
                self.gradual_move(self.legs[0], [85, 0, 74], [65, 35, 74], 0.2);
                self.gradual_move(self.legs[0], [65, 35, 74], [85, 0, 85], 0.2);
                self.gradual_move(self.legs[0], [85, 0, 85], [65, -35, 74], 0.2);
    
                
                self.gradual_move(self.legs[3], [65, 35, 74], [85, 0, 74], 0.2);
                self.gradual_move(self.legs[3], [85, 0, 74], [65, -35, 74], 0.2);
                self.gradual_move(self.legs[3], [65, -35, 74], [85, 0, 64], 0.2);
                self.gradual_move(self.legs[3], [85, 0, 64], [65, 35, 74], 0.2);


                # self.gradual_move(self.legs[3], [85, 0, 74], [65, 35, 74], 0.2);
                # self.gradual_move(self.legs[3], [65, 35, 74], [85, 0, 85], 0.2);
                # self.gradual_move(self.legs[3], [85, 0, 85], [65, -35, 85], 0.2);

                # self.gradual_move([85, 0, 85], [65, -35, 74], 0.5);
                # self.gradual_move([85, 0, 85], [65, -35, 85], 0.5);
                # self.gradual_move([60, -60, -74], [85, 0, -74], 1);
                # self.gradual_move([85, 0, -74], [60, 60, -74], 1);
                # self.gradual_move([60, 60, -74], [96.8, 96.8, 52], 1);
                # self.gradual_move([96.8, 96.8, 52], [137, 0, 52], 1);
                # self.gradual_move([137, 0, 52], [96.8, -96.8, 52], 1);
                # self.gradual_move([96.8, -96.8, 52], [60, -60, -74], 1);
                # self.legs[0].move_to_position([x, y, z])
                # time.sleep(1)
                # self.legs[0].move_to_position([85, 0, -74])
                # time.sleep(1)
                # self.legs[0].move_to_position([60, 60, -74])
                # time.sleep(1)
                # self.legs[0].move_to_position([60, 60, -74])
                # time.sleep(1)
                # # the lifting part was 52
                # self.legs[0].move_to_position([96.8, 96.8, 52])
                # time.sleep(1)
                # self.legs[0].move_to_position([137, 0, 52])
                # time.sleep(1)
                # self.legs[0].move_to_position([96.8, -96.8, 52])
                # time.sleep(1)


    def initialise_legs(self):
        for i in range(self.num_legs):
            leg = Leg(i, 'right' if i < self.num_legs/2 else 'left')
            self.legs.append(leg)

    def gradual_move(self, leg, start_position, end_position, time_to_move):
        # time_to_move is in seconds
        # start_position and end_position are lists of 3 values
        # we will move from start_position to end_position in time_to_move seconds
        # we will move in steps of 100ms
        steps = int(time_to_move / 0.05)
        if steps < 1:
            steps = 1
        delta = [
            (end_position[i] - start_position[i]) / steps for i in range(3)
        ]
        for step in range(steps + 1):
            current_position = [
                start_position[i] + delta[i] * step for i in range(3)
            ]
            # for leg in self.legs:
            leg.move_to_position(current_position)
            # self.legs[2].move_to_position(current_position)
            # self.legs[3].move_to_position(current_position)
            time.sleep(0.1)
        