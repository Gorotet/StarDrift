# test_stardrift.py
"""
Tests for StarDrift module.
"""

import unittest
from stardrift import StarDrift

class TestStarDrift(unittest.TestCase):
    """Test cases for StarDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StarDrift()
        self.assertIsInstance(instance, StarDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StarDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
