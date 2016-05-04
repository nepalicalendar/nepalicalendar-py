# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest
from nepcal import *
from datetime import date, timedelta
from random import randint


class NepdateTestCase(unittest.TestCase):
    """
    Tests for nepdate class
    """

    def test_from_ad_date(self):
        np_date = nepdate.from_ad_date(date.today())
        # self.assertEqual(np_date.year, date.today().year)

    def test_update(self):
        np_date = nepdate.from_bs_date(2073, 1, 10)
        self.assertEqual(np_date.weekday(), 5)
        self.assertEqual(np_date.en_weekday(), 4)

    def test_eq_operator(self):
        date1 = nepdate(2012, 12, 12)
        date2 = nepdate(2012, 12, 12)
        self.assertEqual(date1, date2)

    def test_lt_operator(self):
        self.assertLess(
            nepdate(2054, 1, 18),
            nepdate(2073, 12, 1)
        )

        self.assertLess(
            nepdate(2000, 1, 18),
            nepdate(2033, 2, 1)
        )

        self.assertLess(
            nepdate(2054, 1, 18),
            nepdate(2054, 1, 19)
        )

        self.assertFalse(
            nepdate(2054, 1, 18) <
            nepdate(2054, 1, 18)
        )

        self.assertTrue(
            nepdate(2054, 1, 18) <=
            nepdate(2054, 1, 18)
        )

        self.assertTrue(
            nepdate(2054, 1, 18) <=
            nepdate(2084, 3, 1)
        )

    def test_gt_operator(self):
        self.assertGreater(
            nepdate(2012, 12, 12),
            nepdate(2012, 12, 11)
        )

        self.assertGreater(
            nepdate(2013, 1, 10),
            nepdate(2012, 12, 11)
        )

        self.assertFalse(
            nepdate(2012, 1, 12) >
            nepdate(2012, 12, 11)
        )

        self.assertTrue(
            nepdate(2012, 12, 12) >=
            nepdate(2012, 12, 12)
        )

        self.assertTrue(
            nepdate(2012, 12, 12) >=
            nepdate(2012, 12, 11)
        )

        self.assertFalse(
            nepdate(2012, 12, 10) >=
            nepdate(2012, 12, 11)
        )

    def test_add_operator(self):
        """
        Test the addition operator with timedelta
        """
        self.assertEqual(
            nepdate(2000, 1, 1) + timedelta(days=1),
            nepdate(2000, 1, 2)
        )

        self.assertEqual(
            nepdate(2000, 1, 30) + timedelta(days=9),
            nepdate(2000, 2, 9)
        )

        self.assertEqual(
            nepdate(2036, 12, 15) + timedelta(days=30),
            nepdate(2037, 1, 15)
        )

        self.assertEqual(
            nepdate.from_ad_date(date(2016, 5, 2)),
            nepdate(2073, 1, 20)
        )

        self.assertEqual(
            nepdate.from_ad_date(END_EN_DATE),

            nepdate(
                END_NP_YEAR, 12,
                NEPALI_MONTH_DAY_DATA[END_NP_YEAR][12 - 1]
            )
        )

        self.assertEqual(
            nepdate(2036, 12, 15) + timedelta(days=-5),
            nepdate(2036, 12, 10)
        )

    def test_sub_operator(self):
        date = nepdate(2012, 2, 12) - nepdate(2012, 2, 13)
        self.assertEqual(date.days, 1)

        date = nepdate(2012, 2, 12) - nepdate(2012, 1, 1)
        self.assertEqual(date.days, 42)

        date = nepdate(2073, 1, 6) - nepdate(2073, 3, 18)
        self.assertEqual(date.days, -75)

        date = nepdate(2072, 11, 6) - nepdate(2074, 4, 5)
        self.assertEqual(date.days, -518)

        date = nepdate(2072, 11, 6) - timedelta(days=6)
        self.assertEqual(date, nepdate(2072, 10, 29))

        self.assertEqual(
            nepdate(2036, 12, 15) - timedelta(days=-5),
            nepdate(2036, 12, 20)
        )

    def test_multi_random(self):
        """
        Do multiple random tests by generating data
        """
        for i in range(1, 1000):
            year = randint(values.START_NP_YEAR, values.END_NP_YEAR)
            month = randint(1, 12)
            day = randint(1, 28)

            np_date = nepdate(year, month, day)
            # Check the update
            np_date.update()
            # Convert the english date back to bikram sambat
            np_date_sec = nepdate.from_ad_date(np_date.en_date)
            self.assertTrue((np_date, np_date_sec))

            # Limit year choices so there is enough space for addition
            year = randint(values.START_NP_YEAR, values.END_NP_YEAR - 33)
            np_date = nepdate(year, month, day)
            days = randint(34, 834)
            added_date = np_date + timedelta(days=days)

            calculated_days = added_date - np_date
            self.assertTrue(calculated_days, days)

            # Now, subtract the same number of days from the last date
            first_calc_date = added_date - timedelta(days=days)
            self.assertEqual(first_calc_date, np_date)

    def test_names(self):
        np_date = nepdate(2073, 12, 23).update()
        self.assertEqual(np_date.en_weekday_name(), u"Budhabar")
        self.assertEqual(np_date.weekday_name(), u"वुधवार")
        self.assertEqual(np_date.weekday_name_short(), u'वुध')
        self.assertEqual(np_date.en_month_name(), u'Chaitra')
        self.assertEqual(np_date.month_name(), u'चैत्र')

if __name__ == '__main__':
    unittest.main()
