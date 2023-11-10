#######################################################
# LDate
#
# A simple date class for *L*earning to write classes
#
# Name: zzNAMEzz (replace with your name)
# Section: XX
#
# Fall 2023
#########################################################

class LDate:

    # **class** method
    @classmethod
    def is_leap_year(cls,year: int) -> bool:
        """Return True if year is a leap year, False otherwise
           This should be a **class** method"""
        returnVal = False
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            returnVal = True
            return returnVal
        else:
            return returnVal
        #

    # **class** method
    @classmethod
    def days_in_month(cls,year, month):
        """ Return the number of days in the requested month"""
        day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # in leap year (February has 29 days)
        if cls.is_leap_year(year):
            day_in_month[1] = 29

        return day_in_month[month-1]
        #

    # **class** method
    @classmethod
    def is_valid_date(cls,year, month, day):
        """ Return whether year-month-day represents a valid date.
            This should be a **class** method """
        if not (isinstance(year, int) and 1 <= month <= 12 and 1 <= day <= LDate.days_in_month(year, month)):
            return False
        return True
        #

    #

    def __init__(self, year: int, month: int, day: int):
        """ Constructor
            Raise a ValueError if year-month-day is not a valid date (e.g., 2022-15-27)
        """
        if not self.is_valid_date(year, month, day):
            raise ValueError("Invalid date: {}-{}-{}".format(year, month, day))

        self.year = year
        self.month = month
        self.day = day
        #

    def ordinal_date(self) -> int:
        """ Return the number of days elapsed since the beginning of the year, including any partial days.
            For example, the ordinal date for 1 January is 1."""
        ordinal = self.day
        for month in range(1, self.month):
            ordinal += LDate.days_in_month(self.year, month)
        return ordinal

        #

    def __eq__(self, other) -> bool:
        """Return whether the two objects represent the same date.
        Return False if other is not an LDate."""
        if not isinstance(other, LDate):
            return False
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __lt__(self, other) -> bool:
        """Return whether self < other.
        Raise a ValueError if other is not an LDate."""
        if not isinstance(other, LDate):
            raise ValueError("Comparison with non-LDate object")
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __le__(self, other) -> bool:
        """Return whether self <= other.
        Raise a ValueError if other is not an LDate.
        Use the methods above. Don't re-implement the < algorithm!"""
        if not isinstance(other, LDate):
            raise ValueError("Comparison with non-LDate object")
        return self == other or self < other

    def days_since(self, other) -> bool:
        """ Return the number of days that have elapsed since other.
            (In other words, when other < self, the result should be positive.)
        """

        if not isinstance(other, LDate):
            raise ValueError("Comparison with non-LDate object")

        return self.ordinal_date() - other.ordinal_date()
        #

    _DAYS_OF_WEEK = ('Saturday', 'Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

    def day_of_week(self) -> str:
        """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
            Hint 1: 1 January 1753 was a Monday.
            Hint 2: Use the methods you've already written."""
        day=self.day
        month=self.month
        year=self.year
        if month < 3:
            month += 12
            year -= 1

        yearper100, yeardev100 = year % 100, year // 100

        val = (day + 13 * (month + 1) // 5 + yearper100 + yearper100 // 4 + yeardev100 // 4 - 2 * yeardev100) % 7
        nameDay = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        return nameDay[val]
        #

    def __str__(self) -> str:
        """Return this date as a string of the form "Wednesday, 07 March 1833"."""
        day_of_week_str = LDate._DAYS_OF_WEEK[self.ordinal_date() % 7]
        # print(self.ordinal_date()%7,day_of_week_str)
        month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return f"{day_of_week_str}, {self.day:02d} {month_names[self.month - 1]} {self.year}"

    def __add__(self, days):
        """Return a new LDate object that is the requested number of days after self."""
        if not isinstance(days, int):
            raise ValueError("Days must be an integer")

        new_ordinal_date = self.ordinal_date() + days
        new_year = self.year
        new_month = 1
        while new_ordinal_date > LDate.days_in_month(new_year, new_month):
            new_ordinal_date -= LDate.days_in_month(new_year, new_month)
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1

        return LDate(new_year, new_month, new_ordinal_date)
        #


if __name__ == '__main__':
    d1 = LDate(1941, 12, 7)
    d2 = LDate(2023, 11, 1)
    print(d1)
    print(d2)
    print(d2.days_since(d1))