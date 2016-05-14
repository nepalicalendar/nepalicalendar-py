# -*- coding: utf-8 -*-
"""
Defines the NepDate class
"""

from datetime import date, timedelta
from . import values, functions


class NepDate(object):
    """ Nepali Date class that implements a single nepali date
    """

    def __init__(self, year, month, day):
        """ Initializer for NepDate
        Params:
            year : Year of the date
            month : Month of the date
            day : Day of the date
        English date is not updated in constructor. 'update' should
        be called explicitly"""
        self.year = year
        self.month = month
        self.day = day

        self.en_date = None

    def __unicode__(self):
        return u"Bikram Sambat Date (%d:%d:%d)" % (self.year, self.month, self.day)

    def __str__(self):
        return self.__unicode__()

    def __eq__(self, other):
        return self.year == other.year and \
            self.month == other.month and \
            self.day == other.day

    def __gt__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                return self.day > other.day
            return self.month > other.month
        return self.year > other.year

    def __lt__(self, other):
        return (not self == other) and (not self > other)

    def __ge__(self, other):
        return not self < other

    def __le__(self, other):
        return not self > other

    def __add__(self, other):
        """Adds NepDate with timedelta object"""
        year = self.year
        month = self.month
        day = self.day

        days_remain = other.days

        if days_remain == 0:
            return NepDate(self.year, self.month, self.day).update()
        elif days_remain < 0:
            return self - (other * -1)

        while True:
            # Make sure we're still in range
            if year > values.END_NP_YEAR:
                raise ValueError("Out of range")
            # The current day + days in timedelta fits in within the current
            # month
            if days_remain + day <= values.NEPALI_MONTH_DAY_DATA[year][month - 1]:
                day = day + days_remain
                return NepDate(year, month, day).update()
            else:
                days_remain -= values.NEPALI_MONTH_DAY_DATA[
                    year][month - 1] - day + 1
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    year += 1

    def __sub__(self, other):
        """Subtraction for NepDate. Subtraction can be done with either
        timedelta object to obtain NepDate object or with NepDate object
        to find timedelta object (number of days between the two dates)
        """
        if isinstance(other, timedelta):
            # Subtract number of days from the date
            days_remain = other.days
            if days_remain == 0:
                return self
            elif days_remain < 0:
                return self + (-1 * other)
            # Subtract the number of days
            year = self.year
            month = self.month
            day = self.day
            while True:
                if year < values.START_NP_YEAR:
                    raise ValueError("Out of range")
                if days_remain < day:
                    day = day - days_remain
                    return NepDate(year, month, day).update()
                days_remain -= day
                month = month - 1
                if month < 1:
                    month = 12
                    year = year - 1
                day = values.NEPALI_MONTH_DAY_DATA[year][month - 1]

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
            smaller_days_remain = NepDate(
                smaller.year, 12, values.NEPALI_MONTH_DAY_DATA[
                    smaller.year][12 - 1]
            ) - smaller

            year_remain = range(smaller.year + 1, greater.year)
            for year in year_remain:
                num_days += sum(values.NEPALI_MONTH_DAY_DATA[year])

            # Find the days past in the greater year since january
            greater_days_remain = greater - \
                NepDate(greater.year, 1, 1) + timedelta(1)

            total_days = timedelta(days=num_days) + \
                greater_days_remain + \
                smaller_days_remain

            return multiplier * total_days

        # Same year
        if greater.month > smaller.month:
            smaller_days_remain = NepDate(
                smaller.year,
                smaller.month,
                values.NEPALI_MONTH_DAY_DATA[smaller.year][smaller.month - 1]
            ) - smaller

            month_remain = range(smaller.month + 1, greater.month)
            for month in month_remain:
                num_days += values.NEPALI_MONTH_DAY_DATA[
                    smaller.year][month - 1]

            greater_days_remain = greater - NepDate(
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
        """ Gets a NepDate object from gregorian calendar date """
        functions.check_valid_ad_range(date)
        days = values.START_EN_DATE - date

        # Add the required number of days to the start nepali date
        start_date = NepDate(values.START_NP_YEAR, 1, 1)
        # No need to update as addition already calls update
        return start_date + (date - values.START_EN_DATE)

    @classmethod
    def from_bs_date(cls, year, month, day):
        """ Create and update an NepDate object for bikram sambat date """
        return NepDate(year, month, day).update()

    @classmethod
    def today(today):
        """ Returns today's date in nepali calendar """
        return NepDate.from_ad_date(date.today())

    @classmethod
    def fromtimestamp(cls, timestamp):
        """ Returns a NepDate object created from timestamp """
        return NepDate.from_ad_date(date.fromtimestamp(timestamp))

    def weekday(self):
        """ Returns weekday for the date.
        0 : Aaitabar
        6 : Sanibar """
        return (self.en_date.weekday() + 1) % 7

    def en_weekday(self):
        """ Returns weekday with each week starting in monday
        monday = 0
        sunday = 7 """
        return self.en_date.weekday()

    def en_weekday_name(self):
        """ Gets the weekday name in English language. For eg. Aaitabar"""
        return values.NEPALI_WEEKDAY_NAMES_EN[self.weekday()]

    def weekday_name(self):
        """ Gets the weekday name in Nepali language. For eg. आइतवार"""
        return values.NEPALI_WEEKDAY_NAMES_NE[self.weekday()]

    def weekday_name_short(self):
        """ Gets the short weekday name in nepali language. For eg. आइत for आइतवार"""
        return values.NEPALI_WEEKDAY_NAMES_SHORT_NE[self.weekday()]

    def en_month_name(self):
        """Gets the name of month in english language. For eg. Baisakh"""
        return values.NEPALI_MONTH_NAMES_EN[self.month]

    def month_name(self):
        """Gets the name of month in nepali language. For eg. बैशाख"""
        return values.NEPALI_MONTH_NAMES_NE[self.month]

    def update(self):
        """ Updates information about the NepDate """
        functions.check_valid_bs_range(self)
        # Here's a trick to find the gregorian date:
        # We find the number of days from earliest nepali date to the current
        # day. We then add the number of days to the earliest english date
        self.en_date = values.START_EN_DATE + \
            (
                self - NepDate(
                    values.START_NP_YEAR,
                    1,
                    1
                )
            )
        return self
