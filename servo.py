from servo_driver import PCA9685


class Servo:
    def __init__(self, servo_number):
        self.servo_number = servo_number
        self.current_angle = 0
        
        if self.servo_number > 15:
            self.servo_channel = self.servo_number - 16
            self.servo_driver_address = 0x41
        else:
            self.servo_channel = self.servo_number
            self.servo_driver_address = 0x40

        print(f"Servo Driver Address: {self.servo_driver_address}, Servo channel: {self.servo_channel}, Servo numvber: {self.servo_number}")
        self.servo_driver = PCA9685(self.servo_driver_address, debug=False)
        self.servo_driver.setPWMFreq(50)

    def set_angle(self, angle):
        print(f"Servo Driver Address: {self.servo_driver_address}, Servo channel: {self.servo_channel}, Servo angle: {angle}")
        self.current_angle = angle
        self.servo_driver.setServoAngle(self.servo_channel, angle)
