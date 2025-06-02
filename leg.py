from servo import Servo
from inverse_kinematics import InverseKinematics

class Leg:
    def __init__(self, leg_number):
        self.servos = []
        self.num_servos = 3
        self.leg_number = leg_number
        self.inverse_kinematics = InverseKinematics()

    def initialise_servos(self):
        for i in range(self.num_servos):
            servo = Servo((self.leg_number*self.num_servos) + i)
            self.servos.append(servo)

    def move_to_position(self, position):
        angles = self.inverse_kinematics.calculate_servo_angles(position[0], position[1], position[2])
        self.servos[0].set_angle(angles[0])
        self.servos[1].set_angle(angles[1])
        self.servos[2].set_angle(angles[2])
        
