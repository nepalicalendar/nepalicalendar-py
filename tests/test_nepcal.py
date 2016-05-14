# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest
from nepalicalendar import *
from datetime import date, timedelta
from random import randint


class NepCalTestCase(unittest.TestCase):
    """
    Tests for NepCal class
    """

    def test_iter_month(self):
        cal = NepCal.itermonthdates(2073, 8)
        self.assertEqual(len(list(cal)), 35)

        weeks = NepCal.monthdatescalendar(2073, 8)

    def test_functions(self):
        self.assertEqual(NepCal.weekday(2073, 1, 23), 4)
