"""Sample test file to ensure tests directory exists"""
import unittest


class TestBasic(unittest.TestCase):
    """Basic test class"""

    def test_import(self):
        """Test basic import"""
        self.assertTrue(True)

    def test_placeholder(self):
        """Placeholder test"""
        assert 1 + 1 == 2


if __name__ == '__main__':
    unittest.main()
