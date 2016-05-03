# -*- coding: utf-8 -*-
"""
Defines the nepdate class
"""

import sys
from datetime import date, timedelta
from . import values, functions


class nepdate(object):
    """
    Represents nepali date
    """

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

        self.en_date = None

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

    def __sub__(self, other):
        """
        Subtraction operator.
        Returns a timedelta object
        """
        greater = self
        smaller = other
        multiplier = 1
        if self < other:
            greater = other
            smaller = self
            multiplier = -1

        # Delta in days
        num_days = 0
        if greater.year > smaller.year:
            # First of all, get the days remaining in the smaller year
            # till year end
            smaller_days_remain = nepdate(
                smaller.year, 12, values.NEPALI_MONTH_DAY_DATA[
                    smaller.year][12 - 1]
            ) - smaller

            year_remain = range(smaller.year + 1, greater.year)
            for year in year_remain:
                num_days += sum(values.NEPALI_MONTH_DAY_DATA[year])

            # Find the days past in the greater year since january
            greater_days_remain = greater - \
                nepdate(greater.year, 1, 1) + timedelta(1)

            total_days = timedelta(days=num_days) + \
                greater_days_remain + \
                smaller_days_remain

            return multiplier * total_days

        # Same year
        if greater.month > smaller.month:
            smaller_days_remain = nepdate(
                smaller.year,
                smaller.month,
                values.NEPALI_MONTH_DAY_DATA[smaller.year][smaller.month - 1]
            ) - smaller

            month_remain = range(smaller.month + 1, greater.month)
            for month in month_remain:
                num_days += values.NEPALI_MONTH_DAY_DATA[
                    smaller.year][month - 1]

            greater_days_remain = greater - nepdate(
                greater.year, greater.month, 1) + timedelta(days=1)
            # One is added to adjust for 1 gate. For example, if we're counting from
            # biasakh 12 to jestha 18, it will count from baisakh 12 to baisakh 30
            # Then again, from jeth 1 to jeth 18. In this process, jeth 1 is neglected
            # Hence, 1 is added here

            total_days = timedelta(days=num_days) + \
                greater_days_remain + \
                smaller_days_remain

            return multiplier * total_days

        # Same year and same month but different days
        total_days = timedelta(days=greater.day - smaller.day)
        return total_days

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
    def from_bs_date(cls, year, month, day):
        """
        Create and update an nepdate object for bikram sambat date
        """
        return nepdate(year, month, day).update()

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

    def weekday(self):
        """
        Returns weekday for the date.
        0 : Aaitabar
        6 : Sanibar
        """
        return (self.en_date.weekday() + 1) % 7

    def en_weekday(self):
        """
        Returns weekday with each week starting in monday
        monday = 0
        sunday = 7
        """
        return self.en_date.weekday()

    def update(self):
        """
        Updates information about the nepdate
        """
        # Here's a trick to find the gregorian date:
        # We find the number of days from earliest nepali date to the current
        # day. We then add the number of days to the earliest english date
        self.en_date = values.START_EN_DATE + \
            (
                self - nepdate(
                    values.START_NP_YEAR,
                    1,
                    1
                )
            )
        return self
