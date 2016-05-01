# -*- coding: utf-8 -*-
"""
Defines the nepdate class
"""

import sys
from datetime import date


class nepdate(object):
    """
    Represents nepali date
    """

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_ad_date(cls, date):
        """
        Gets a nepdate object from gregorian calendar date
        """
        return nepdate(date.year, date.month, date.day)

    @classmethod
    def today():
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
