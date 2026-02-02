# test_evmrelay.py
"""
Tests for EvmRelay module.
"""

import unittest
from evmrelay import EvmRelay

class TestEvmRelay(unittest.TestCase):
    """Test cases for EvmRelay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EvmRelay()
        self.assertIsInstance(instance, EvmRelay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EvmRelay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
