"""Description

This script reads a time duration in seconds from user input,
uses the `time_units_converter.TimeConverter` class methods to convert it into
a human-readable format, and prints the result.
"""

from include import time_units_converter


def start_convert():

    """Main function

    Usage:
        - Run the script.
        - Enter a numerical value (in seconds) when prompted.
        - The script outputs the formatted time duration.

    Dependencies:
        - `time_units_converter`:   A module with the convert_time()
                                    that performs the time conversion.

    Example:
        Input: 3600
        Output: "1 hour"
    """

    users_seconds = input("Please enter the seconds")
    converted_time = time_units_converter.TimeConverter(int(users_seconds))
    converted_time.convert_time()
    converted_time.print_time()


if __name__ == "__main__":
    start_convert()
