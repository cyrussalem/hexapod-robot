import sys
from unittest.mock import MagicMock

class MockSMBus:
    def __init__(self, bus=None):
        self.write_byte_data = MagicMock()
        self.read_byte_data = MagicMock()
        self.read_word_data = MagicMock()
        self.write_word_data = MagicMock()

# Create a mock for the smbus module
mock_smbus = MagicMock()
mock_smbus.SMBus = MockSMBus

# Add the mock to sys.modules
sys.modules['smbus'] = mock_smbus 