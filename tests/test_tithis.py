# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest
from nepalicalendar import TITHIS, NepDate, NepCal
from datetime import date, timedelta
from random import randint


class TithisTestCase(unittest.TestCase):
    """
    Test case for the tithis
    """

    def test_tithi_month_count(self):
        """
        Make sure that the tithi data is in match with the month data
        """
        for i in range(2040, 2071):
            self.assertEqual(len(TITHIS[i]), 12)
            for j in range(1,13):
                try:
                    self.assertEqual(len(TITHIS[i][j-1]), NepCal.monthrange(i,j))
                except:
                    print("Error in year %d month %d" % (i, j))
                    raise

    def test_nepdate_tithi(self):
        d = NepDate(2069,2,3)
        self.assertEqual(d.tithi, 11)
        #TODO: Add more tithi tests

    def test_nepdate_tithi_name(self):
        self.assertEqual(NepDate(2069,4,15).ne_tithi_name(),"द्वादशी")
        pass


