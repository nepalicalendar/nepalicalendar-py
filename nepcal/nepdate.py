# -*- coding: utf-8 -*-
"""
Defines the nepdate class
"""

import sys
from datetime import date
from . import values, functions


class nepdate(object):
    """
    Represents nepali date
    """

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __eq__(self, other):
        return self.year == other.year and \
            self.month == other.month and \
            self.day == other.day

    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False
        else:
            if self.month > other.month:
                return True
            elif self.month < other.month:
                return False
            else:
                if self.day > other.day:
                    return True
                return False

    def __ge__(self, other):
        return self == other or self > other

    def __lt__(self, other):
        return (not self == other) and (not self > other)

    def __le__(self, other):
        return not self > other

    def __add__(self, other):
        """
        Add operator for timedelta
        """
        year = self.year
        month = self.month
        day = self.day

        days_remain = other.days

        while True:
            # Make sure we're still in range
            if year > values.END_NP_YEAR:
                raise ValueError("Out of range")
            # The current day + days in timedelta fits in within the current
            # month
            if days_remain + day <= values.NEPALI_MONTH_DAY_DATA[year][month - 1]:
                day = day + days_remain
                return nepdate(year, month, day)
            else:
                days_remain -= values.NEPALI_MONTH_DAY_DATA[
                    year][month - 1] - day + 1
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    year += 1

    @classmethod
    def from_ad_date(cls, date):
        """
        Gets a nepdate object from gregorian calendar date
        """
        functions.check_valid_ad_range(date)
        days = values.START_EN_DATE - date

        # Add the required number of days to the start nepali date
        start_date = nepdate(values.START_NP_YEAR, 1, 1)
        return start_date + (date - values.START_EN_DATE)

    @classmethod
    def today(today):
        """
        Returns today's date in nepali calendar
        """
        return nepdate.from_ad_date(date.today())

    @classmethod
    def fromtimestamp(cls, timestamp):
        """
        Returns a nepdate object created from timestamp
        """
        return nepdate.from_ad_date(date.fromtimestamp(timestamp))

    def __unicode__(self):
        return u"Bikram Sambat Date (%d:%d:%d)" % (self.year, self.month, self.day)

    def __str__(self):
        return self.__unicode__()
