# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest
from nepcal import *
from datetime import date, timedelta
from random import randint


class NepCalTestCase(unittest.TestCase):
    """
    Tests for nepcal class
    """

    def test_iter_month(self):
        cal = nepcal.itermonthdates(2073, 8)
        self.assertEqual(len(list(cal)), 35)

        # print([str(x) for x in nepcal.itermonthdates(2073,8)])

        weeks = nepcal.monthdatescalendar(2073, 8)
        for week in weeks:
            print([str(x) for x in week])
            break


    def test_functions(self):
        self.assertEqual(nepcal.weekday(2073, 1, 23), 4)
