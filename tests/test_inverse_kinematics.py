import pytest
import math
import numpy as np
from inverse_kinematics import InverseKinematics

@pytest.fixture
def ik():
    """Create an InverseKinematics instance with default values."""
    return InverseKinematics()

def test_initialization():
    """Test that the InverseKinematics class initializes with correct default values."""
    ik = InverseKinematics()
    assert ik.a1 == 45
    assert ik.a2 == 40
    assert ik.a3 == 74

    # Test custom initialization
    ik = InverseKinematics(40, 80, 120)
    assert ik.a1 == 40
    assert ik.a2 == 80
    assert ik.a3 == 120

def test_completely_straight_leg(ik):
    """Test calculating angles for a position straight down."""
    ik = InverseKinematics()
    angles = ik.calculate_servo_angles(159, 0, 0)
    coxa, femur, tibia = angles
    print('ANGLES: ', coxa, femur, tibia)
    
    assert coxa == 0 
    assert femur == 0
    assert tibia == 0
    # assert -180 <= femur <= 180  # Femur angle should be reasonable
    # assert -180 <= tibia <= 180  # Tibia angle should be reasonable

def test_leg_on_the_ground(ik):
    """Test calculating angles for a position straight down."""
    ik = InverseKinematics()
    angles = ik.calculate_servo_angles(85, 0, 74)
    coxa, femur, tibia = angles
    print('ANGLES: ', coxa, femur, tibia)
    
    assert coxa == 0  
    assert femur == 0
    assert tibia == 90

    # assert -180 <= femur <= 180  # Femur angle should be reasonable
    # assert -180 <= tibia <= 180  # Tibia angle should be reasonable