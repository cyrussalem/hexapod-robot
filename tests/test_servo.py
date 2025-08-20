import pytest
from unittest.mock import Mock, patch
from servo import Servo

@pytest.fixture
def mock_pca():
    with patch('servo.PCA9685') as mock:
        # Return a mock instance when PCA9685 is instantiated
        mock_instance = Mock()
        mock_instance.setPWMFreq = Mock()
        mock_instance.setServoAngle = Mock()
        mock.return_value = mock_instance
        yield mock_instance

def test_servo_initialization(mock_pca):
    """Test that a servo is properly initialized."""
    servo = Servo(1)
    assert servo.servo_channel == 1
    # Verify PCA9685 was initialized correctly
    mock_pca.setPWMFreq.assert_called_once_with(50)

def test_set_angle(mock_pca):
    """Test that set_angle properly delegates to the servo driver."""
    servo = Servo(1)
    test_angle = 90
    servo.set_angle(test_angle)
    # Verify the angle was set correctly
    mock_pca.setServoAngle.assert_called_once_with(1, test_angle) 