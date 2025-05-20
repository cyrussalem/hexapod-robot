from hexapod import Hexapod
from servo_driver import PCA9685 



if __name__ == '__main__':
    # sv_driver = PCA9685()
    # sv_driver.setPWMFreq(50)

    # sv_driver.setServoAngle(0, 90)

    hexapod = Hexapod()
    hexapod.move()
