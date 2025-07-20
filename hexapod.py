from leg import Leg
import time


class Hexapod:
    def __init__(self):
        self.legs = []
        self.num_legs = 6
        self.initialise_legs()

    def move(self, direction):
        if direction == 'forward':
            self.move_forward()
        elif direction == 'backward':
            print('Moving backward')
    
    def move_forward(self):
        while True:
            # Move for 3 seconds, incrementing every 100ms
            while True:
                
                self.gradual_move([self.legs[0], self.legs[3]], [[65, -35, 74], [65, 35, 74]], [[85, 0, 74], [85, 0, 74]], 0.1);
                self.gradual_move([self.legs[0], self.legs[3]], [[85, 0, 74], [85, 0, 74]], [[65, 35, 74], [65, -35, 74]], 0.1);
                self.gradual_move([self.legs[0], self.legs[3]], [[65, 35, 74], [65, -35, 74]], [[85, 0, 85], [85, 0, 64]], 0.1);
                self.gradual_move([self.legs[0], self.legs[3]], [[85, 0, 85], [85, 0, 64]], [[65, -35, 74], [65, 35, 74]], 0.1);

    
                self.gradual_move([self.legs[1], self.legs[2]], [[65, -35, 74], [65, 35, 74]], [[85, 0, 74], [85, 0, 74]], 0.1);
                self.gradual_move([self.legs[1], self.legs[2]], [[85, 0, 74], [85, 0, 74]], [[65, 35, 74], [65, -35, 74]], 0.1);
                self.gradual_move([self.legs[1], self.legs[2]], [[65, 35, 74], [65, -35, 74]], [[85, 0, 85], [85, 0, 64]], 0.1);
                self.gradual_move([self.legs[1], self.legs[2]], [[85, 0, 85], [85, 0, 64]], [[65, -35, 74], [65, 35, 74]], 0.1);

                # self.gradual_move([self.legs[5]], [[65, -35, 74]], [[85, 0, 74]], 0.1);
                # self.gradual_move([self.legs[5]], [[85, 0, 74]], [[65, 35, 74]], 0.1);
                # self.gradual_move([self.legs[5]], [[65, 35, 74]], [[85, 0, 85]], 0.1);
                # self.gradual_move([self.legs[5]], [[85, 0, 85]], [[65, -35, 74]], 0.1);



    def initialise_legs(self):
        for i in range(self.num_legs):
            leg = Leg(i, 'right' if i < self.num_legs/2 else 'left')
            self.legs.append(leg)

    def gradual_move(self, legs, start_positions, end_positions, time_to_move):
        """
        Move multiple legs simultaneously from their respective start_positions to end_positions over time_to_move seconds.
        legs: list of Leg objects
        start_positions: list of [x, y, z] for each leg
        end_positions: list of [x, y, z] for each leg
        time_to_move: total time in seconds
        """
        import time

        num_legs = len(legs)
        assert len(start_positions) == num_legs and len(end_positions) == num_legs, \
            "legs, start_positions, and end_positions must have the same length"

        steps = int(time_to_move / 0.025)
        if steps < 1:
            steps = 1

        # Precompute deltas for each leg
        deltas = [
            [
                (end_positions[leg_idx][i] - start_positions[leg_idx][i]) / steps
                for i in range(3)
            ]
            for leg_idx in range(num_legs)
        ]

        for step in range(steps + 1):
            for leg_idx, leg in enumerate(legs):
                current_position = [
                    start_positions[leg_idx][i] + deltas[leg_idx][i] * step
                    for i in range(3)
                ]
                leg.move_to_position(current_position)
            time.sleep(0.05)