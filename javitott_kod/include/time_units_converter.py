"""Description

This is the main function for converting
seconds to human readable time format.
"""


class TimeConverter:

    """Converter Class

    This is the main class for convert seconds to human readable time format.
    """

    def __init__(self, seconds):
        self.seconds = seconds
        self.time_units = []

    def calculate_units(self, units_left, unit):

        """Calculate units

        Method for calculate units and append them to the list
        """

        if units_left == 1:
            unit = str(units_left) + " " + unit
            self.time_units.append(unit)
        elif units_left > 1:
            unit = str(units_left) + " " + unit + "s"
            self.time_units.append(unit)

    def convert_time(self):

        """Converter method

        Main converter method
        """

        if self.seconds != 0:

            # Seconds
            seconds_left = self.seconds % 60
            self.calculate_units(seconds_left, "second")

            # Minutes
            minutes = self.seconds // 60
            minutes_left = minutes % 60
            self.calculate_units(minutes_left, "minute")

            # Hours
            hours = minutes // 60
            hours_left = hours % 24
            self.calculate_units(hours_left, "hour")

            # Days
            days = hours // 24
            days_left = days % 365
            self.calculate_units(days_left, "day")

            # Years
            years = days // 365
            years_left = years % 365
            self.calculate_units(years_left, "year")

        else:
            self.time_units.append("now")

    def print_time(self):

        """WriteOut method

        Write out the time
        """
        temporary_units = []
        self.time_units = self.time_units[::-1]

        for i, time_unit in enumerate(self.time_units):
            if i == len(self.time_units) - 2:
                temporary_units.append(time_unit + " and ")
            elif i == len(self.time_units) - 1:
                temporary_units.append(time_unit)
            else:
                temporary_units.append(time_unit + ", ")

        text = "".join(temporary_units)
        print(text)
        return text
