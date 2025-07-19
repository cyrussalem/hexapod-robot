import math
import numpy as np

class InverseKinematics:
    def __init__(self, coxa_length=45, femur_length=40, tibia_length=74):
        """
        Initialize the inverse kinematics calculator with leg segment lengths.
        
        Args:
            coxa_length (float): Length of the coxa (hip) segment in mm
            femur_length (float): Length of the femur (thigh) segment in mm
            tibia_length (float): Length of the tibia (shin) segment in mm
        """
        self.a1 = coxa_length
        self.a2 = femur_length
        self.a3 = tibia_length

    def r1(self, x, y):
        return math.sqrt(x ** 2 + y ** 2) - self.a1

    def r2(self, z):
        return z

    def phi_2(self, x, y, z):
        return math.degrees(math.atan(self.r2(z) / self.r1(x, y)))

    def r3(self, x, y, z):
        return math.sqrt(self.r1(x, y) ** 2 + self.r2(z) ** 2)

    def phi_1(self, x, y, z):
        return math.degrees(math.acos((self.a3 ** 2 - self.a2 ** 2 - self.r3(x, y, z) ** 2) / (-2 * self.a2 * self.r3(x, y, z))))

    def phi_3(self, x, y, z):
        return math.degrees(math.acos((self.r3(x, y, z) ** 2 - self.a2 ** 2 - self.a3 ** 2) / (-2 * self.a2 * self.a3)))

    def calculate_servo_angles(self, x, y, z):

        # print('POSTIIONS IN SPACE:', x, y, z)

        servo_angle_1 = math.degrees(math.atan(y / x))
        servo_angle_2 = self.phi_2(x, y, z) - self.phi_1(x, y, z)
        servo_angle_3 = 180 - self.phi_3(x, y, z)

        return (servo_angle_1, servo_angle_2, servo_angle_3)