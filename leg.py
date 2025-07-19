from servo import Servo
from inverse_kinematics import InverseKinematics

class Leg:
    def __init__(self, leg_number, leg_type):
        self.servos = []
        self.num_servos = 3
        self.leg_number = leg_number
        self.leg_type = leg_type
        self.inverse_kinematics = InverseKinematics()
        self.initialise_servos()  # Initialize servos when leg is created

    def initialise_servos(self):
        for i in range(self.num_servos):
            servo = Servo((self.leg_number*self.num_servos) + i)
            self.servos.append(servo)
        print(f"Initialized {len(self.servos)} servos for leg {self.leg_number}")

    def move_to_position(self, position):
        print(f"Moving leg {self.leg_number} with {len(self.servos)} servos")
        angles = self.inverse_kinematics.calculate_servo_angles(position[0], position[1], position[2])
        servo_angles = self.get_servo_angles(self.leg_type, angles)

        print('ANGLES: ', angles)
        print('SERVO ANGLES: ', servo_angles)
        if not self.servos:
            raise RuntimeError(f"No servos initialized for leg {self.leg_number}")
            
        angle1, angle2, angle3 = servo_angles  # tuple unpacking
        self.servos[0].set_angle(angle1)
        self.servos[1].set_angle(angle2)
        self.servos[2].set_angle(angle3)
    
    def get_servo_angles(self, leg_type, angles):
        if leg_type == 'right':
            return (angles[0]+ 90, angles[1] + 90, angles[2] + 90)
        else:
            return (angles[0]+ 90, angles[1] + 90, angles[2] - 90)
        
