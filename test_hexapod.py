from hexapod import Hexapod
from servo_driver import PCA9685

# front:  x = 60, y = -60, z = 74 back: x = 85, y = 0, z = 74 

# leg, start_pos, end_pos
def main():
    hexapod = Hexapod()
    while True:
        values_str = input("Leg Number, X, Y, Z: ")
    
        values = values_str.strip().split(",")  # Fixed: should use values_str, not values
    
        hexapod.test_leg(int(values[0].strip()), int(values[1].strip()), int(values[2].strip()), int(values[3].strip()))  # Fixed: missing closing parentheses and commas

if __name__ == '__main__':  # Fixed: should be __name__ not **name**
    main() 



# legs 0 and 2
# 1, 60, -60, 74
# 2, 85, 0, 74
# 4, 73, 0, 90


# leg 1

# 1, 60, 60, 74
# 2, 73, 0, 90
# 2, 85, 0, 74


