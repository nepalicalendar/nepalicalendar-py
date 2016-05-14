# -*- coding: utf-8 -*-
"""
Defines the NepCal class
"""

from datetime import timedelta
from . import values, functions, NepDate


class NepCal(object):
    """ Nepali calendar class.
    """

    def __init__(self):
        pass

    def __unicode__(self):
        return u"Nepcal class"

    def __str__(self):
        return self.__unicode__()

    @classmethod
    def weekday(cls, year, month, day):
        """Returns the weekday of the date. 0 = aaitabar"""
        return NepDate.from_bs_date(year, month, day).weekday()

    @classmethod
    def monthrange(cls, year, month):
        """Returns the number of days in a month"""
        functions.check_valid_bs_range(year, month, 1)
        return values.NEPALI_MONTH_DAY_DATA[year][month - 1]

    @classmethod
    def itermonthdates(cls, year, month):
        """
        Returns an iterator for the month in a year
        This iterator will return all days (as NepDate objects) for the month
        and all days before the start of the month or after the end of the month
        that are required to get a complete week.
        """
        curday = NepDate.from_bs_date(year, month, 1)
        start_weekday = curday.weekday()
        # Start_weekday represents the number of days we have to pad
        for i in range(start_weekday, 0, -1):
            yield (curday - timedelta(days=i))

        for i in range(0, values.NEPALI_MONTH_DAY_DATA[year][month - 1]):
            if i > 0:
                curday.day += 1
                curday.en_date = curday.en_date + timedelta(days=1)
            # Create a new object and return it
            n_date = NepDate(curday.year, curday.month, curday.day)
            n_date.en_date = curday.en_date
            yield n_date
        # Now, curday points to the last day of the month. Check it's weekday
        # and return days from next month to complete the week
        last_weekday = curday.weekday()
        remain = 6 - last_weekday

        for i in range(1, remain + 1):
            yield (curday + timedelta(days=i))

    @classmethod
    def itermonthdays(cls, year, month):
        """Similar to itermonthdates but returns day number instead of NepDate object
        """
        for day in NepCal.itermonthdates(year, month):
            if day.month == month:
                yield day.day
            else:
                yield 0

    @classmethod
    def itermonthdays2(cls, year, month):
        """Similar to itermonthdays2 but returns tuples of day and weekday.
        """
        for day in NepCal.itermonthdates(year, month):
            if day.month == month:
                yield (day.day, day.weekday())
            else:
                yield (0, day.weekday())

    @classmethod
    def monthdatescalendar(cls, year, month):
        """ Returns a list of week in a month. A week is a list of NepDate objects """
        weeks = []
        week = []
        for day in NepCal.itermonthdates(year, month):
            week.append(day)
            if len(week) == 7:
                weeks.append(week)
                week = []
        if len(week) > 0:
            weeks.append(week)
        return weeks

    @classmethod
    def monthdayscalendar(cls, year, month):
        """Return a list of the weeks in the month month of the year as full weeks.
        Weeks are lists of seven day numbers."""
        weeks = []
        week = []
        for day in NepCal.itermonthdays(year, month):
            week.append(day)
            if len(week) == 7:
                weeks.append(week)
                week = []
        if len(week) > 0:
            weeks.append(week)
        return weeks

    @classmethod
    def monthdays2calendar(cls, year, month):
        """ Return a list of the weeks in the month month of the year as full weeks.
        Weeks are lists of seven tuples of day numbers and weekday numbers. """
        weeks = []
        week = []
        for day in NepCal.itermonthdays2(year, month):
            week.append(day)
            if len(week) == 7:
                weeks.append(week)
                week = []
        if len(week) > 0:
            weeks.append(week)
        return weeks
