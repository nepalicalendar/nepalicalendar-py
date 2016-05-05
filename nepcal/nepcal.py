# -*- coding: utf-8 -*-
"""
Defines the nepcal class
"""

import sys
from datetime import date, timedelta
from . import values, functions, nepdate


class nepcal(object):
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
        return nepdate.from_bs_date(year, month, day).weekday()

    @classmethod
    def monthrange(cls, year, month):
        """Returns the number of days in a month"""
        functions.check_valid_bs_range(year, month, 1)
        return values.NEPALI_MONTH_DAY_DATA[year][month - 1]

    @classmethod
    def itermonthdates(cls, year, month):
        """Returns the nepdate objects of any month as a list"""
        start = nepdate.from_bs_date(year, month, 1)

        for i in range(0, values.NEPALI_MONTH_DAY_DATA[year][month - 1]):
            if i > 0:
                start.day += 1
                start.en_date = start.en_date + timedelta(days=1)
            yield start
