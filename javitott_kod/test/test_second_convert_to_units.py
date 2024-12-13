"""Description

This is the unittest for the seconds to time units converter
"""

import sys
import unittest
from pathlib import Path
from include import time_units_converter


class TestTimeChange(unittest.TestCase):

    """Time converter class for test

    Class for time converter for test
    """

    def test_for_zero(self):

        """Test method for zero value

        Expected output:
        'now'
        """

        test_unit = time_units_converter.TimeConverter(0)
        test_unit.convert_time()

        self.assertEqual(
            "now",
            test_unit.print_time())

    def test_for_one(self):

        """Test method for 1 value

        Expected output:
        '1 second'
        """

        test_unit = time_units_converter.TimeConverter(1)
        test_unit.convert_time()

        self.assertEqual(
            "1 second",
            test_unit.print_time())

    def test_for_62(self):

        """Test method for 62 value

        Expected output:
        '1 minute and 2 seconds'
        """

        test_unit = time_units_converter.TimeConverter(62)
        test_unit.convert_time()

        self.assertEqual(
            "1 minute and 2 seconds",
            test_unit.print_time())

    def test_for_3600(self):

        """Test method for 3600 value

        Expected output:
        '1 hour'
        """

        test_unit = time_units_converter.TimeConverter(3600)
        test_unit.convert_time()

        self.assertEqual(
            "1 hour",
            test_unit.print_time())

    def test_for_3662(self):

        """Test method for 3662 value

        Expected output:
        '1 hour, 1 minute and 2 seconds'
        """

        test_unit = time_units_converter.TimeConverter(3662)
        test_unit.convert_time()

        self.assertEqual(
            "1 hour, 1 minute and 2 seconds",
            test_unit.print_time())

    def test_for_15731080(self):

        """Test method for 15731080 value

        Expected output:
        '182 days, 1 hour, 44 minutes and 40 seconds'
        """

        test_unit = time_units_converter.TimeConverter(15731080)
        test_unit.convert_time()

        self.assertEqual(
            "182 days, 1 hour, 44 minutes and 40 seconds",
            test_unit.print_time())

    def test_for_132030240(self):

        """Test method for 132030240 value

        Expected output:
        '4 years, 68 days, 3 hours and 4 minutes'
        """

        test_unit = time_units_converter.TimeConverter(132030240)
        test_unit.convert_time()

        self.assertEqual(
            "4 years, 68 days, 3 hours and 4 minutes",
            test_unit.print_time())

    def test_for_205851834(self):

        """Test method for 205851834 value

        Expected output:
        '6 years, 192 days, 13 hours, 3 minutes and 54 seconds'
        """

        test_unit = time_units_converter.TimeConverter(205851834)
        test_unit.convert_time()

        self.assertEqual(
            "6 years, 192 days, 13 hours, 3 minutes and 54 seconds",
            test_unit.print_time())

    def test_for_253374061(self):

        """Test method for 205851834 value

        Expected output:
        '8 years, 12 days, 13 hours, 41 minutes and 1 second'
        """

        test_unit = time_units_converter.TimeConverter(253374061)
        test_unit.convert_time()

        self.assertEqual(
            "8 years, 12 days, 13 hours, 41 minutes and 1 second",
            test_unit.print_time())

    def test_for_242062374(self):

        """Test method for 205851834 value

        Expected output:
        '7 years, 246 days, 15 hours, 32 minutes and 54 seconds'
        """

        test_unit = time_units_converter.TimeConverter(242062374)
        test_unit.convert_time()

        self.assertEqual(
            "7 years, 246 days, 15 hours, 32 minutes and 54 seconds",
            test_unit.print_time())

    def test_for_101956166(self):

        """Test method for 101956166 value

        Expected output:
        '3 years, 85 days, 1 hour, 9 minutes and 26 seconds'
        """

        test_unit = time_units_converter.TimeConverter(101956166)
        test_unit.convert_time()

        self.assertEqual(
            "3 years, 85 days, 1 hour, 9 minutes and 26 seconds",
            test_unit.print_time())

    def test_for_33243586(self):

        """Test method for 33243586 value

        Expected output:
        '1 year, 19 days, 18 hours, 19 minutes and 46 seconds'
        """

        test_unit = time_units_converter.TimeConverter(33243586)
        test_unit.convert_time()

        self.assertEqual(
            "1 year, 19 days, 18 hours, 19 minutes and 46 seconds",
            test_unit.print_time())


def adjust_import_path():
    """
    Adjusting sys.path in the test script
    """
    current_file_path = Path(__file__).resolve()
    parent_directory = current_file_path.parent.parent
    sys.path.append(str(parent_directory))


if __name__ == "__main__":
    adjust_import_path()
    unittest.main()
