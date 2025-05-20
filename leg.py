from servo import Servo

class Leg:
    def __init__(self, leg_number):
        self.servos = []
        self.num_servos = 3
        self.leg_number = leg_number

    def initialise_servos(self):
        for i in range(self.num_servos):
            servo = Servo((self.leg_number*self.num_servos) + i)
            self.servos.append(servo)

    def move_to_position(self, position):
        self.servos[0].set_angle(position[0])
        self.servos[1].set_angle(position[1])
        self.servos[2].set_angle(position[2])
