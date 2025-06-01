import pytest
from leg import Leg
from servo import Servo

def test_leg_initialization():
    """Test that a leg is properly initialized with the correct number of servos."""
    leg = Leg(1)
    assert leg.leg_number == 1
    assert leg.num_servos == 3
    assert len(leg.servos) == 0

def test_servo_initialization():
    """Test that servos are properly initialized for a leg."""
    leg = Leg(1)
    leg.initialise_servos()
    assert len(leg.servos) == 3
    assert all(isinstance(servo, Servo) for servo in leg.servos)
    # Check servo numbers are assigned correctly (leg 1 should have servos 3,4,5)
    assert [servo.servo_number for servo in leg.servos] == [3, 4, 5]

def test_move_to_position():
    """Test that move_to_position correctly sets servo angles."""
    leg = Leg(0)
    leg.initialise_servos()
    test_position = [45, 90, 135]
    leg.move_to_position(test_position)
    
    # Verify each servo was set to the correct angle
    for servo, expected_angle in zip(leg.servos, test_position):
        assert servo.current_angle == expected_angle 