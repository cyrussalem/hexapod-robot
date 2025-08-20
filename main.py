from hexapod import Hexapod
from servo_driver import PCA9685 



if __name__ == '__main__':
    hexapod = Hexapod()
    hexapod.move('forward')
