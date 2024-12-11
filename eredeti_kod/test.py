from tcs import myfunction
import unittest
from pathlib import Path
import sys
# current_file_path = Path(__file__).resolve()
# parent_directory = current_file_path.parent.parent
# sys.path.append(str(parent_directory))

class TestTimeChange(unittest.TestCase):
    def test_change(self):
        self.assertEqual("now", myfunction(0))
        self.assertEqual("1 second", myfunction(1))
        self.assertEqual("1 minute and 2 seconds", myfunction(62))
        self.assertEqual("2 minutes", myfunction(120))
        self.assertEqual("1 hour", myfunction(3600))
        self.assertEqual("1 hour, 1 minute and 2 seconds", myfunction(3662))
        self.assertEqual("182 days, 1 hour, 44 minutes and 40 seconds", myfunction(15731080))
        self.assertEqual("4 years, 68 days, 3 hours and 4 minutes", myfunction(132030240))
        self.assertEqual("6 years, 192 days, 13 hours, 3 minutes and 54 seconds", myfunction(205851834))
        self.assertEqual("8 years, 12 days, 13 hours, 41 minutes and 1 second", myfunction(253374061))
        self.assertEqual("7 years, 246 days, 15 hours, 32 minutes and 54 seconds", myfunction(242062374))
        self.assertEqual("3 years, 85 days, 1 hour, 9 minutes and 26 seconds", myfunction(101956166))
        self.assertEqual("1 year, 19 days, 18 hours, 19 minutes and 46 seconds", myfunction(33243586))
if __name__ == "__main__":
    unittest.main()

