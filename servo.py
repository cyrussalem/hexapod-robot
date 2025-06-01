from servo_driver import PCA9685


class Servo:
    def __init__(self, servo_channel):
        self.servo_channel = servo_channel
        self.servo_number = servo_channel
        self.current_angle = 0
        self.servo_driver = PCA9685(0x40, debug=False)
        self.servo_driver.setPWMFreq(50)

    def set_angle(self, angle):
        print(f"Servo channel: {self.servo_channel}, Servo angle: {angle}")
        self.current_angle = angle
        self.servo_driver.setServoAngle(self.servo_channel, angle)
