# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest
from nepalicalendar import *
from datetime import date, timedelta
from random import randint


class NepDateTestCase(unittest.TestCase):
    """
    Tests for NepDate class
    """

    def test_properties(self):
        np_date = NepDate(2071,12,23)
        self.assertEqual(np_date.ne_day, "२३")
        self.assertEqual(np_date.ne_month, "१२")
        self.assertEqual(np_date.ne_year, "२०७१")

    def test_from_ad_date(self):
        np_date = NepDate.from_ad_date(date.today())
        self.assertEqual(np_date, NepDate.today())
        self.assertEqual(np_date.en_date, date.today())

    def test_update(self):
        np_date = NepDate.from_bs_date(2073, 1, 10)
        self.assertEqual(np_date.weekday(), 5)
        self.assertEqual(np_date.en_weekday(), 4)

    def test_eq_operator(self):
        date1 = NepDate(2012, 12, 12)
        date2 = NepDate(2012, 12, 12)
        self.assertEqual(date1, date2)

    def test_lt_operator(self):
        self.assertLess(
            NepDate(2054, 1, 18),
            NepDate(2073, 12, 1)
        )

        self.assertLess(
            NepDate(2000, 1, 18),
            NepDate(2033, 2, 1)
        )

        self.assertLess(
            NepDate(2054, 1, 18),
            NepDate(2054, 1, 19)
        )

        self.assertFalse(
            NepDate(2054, 1, 18) <
            NepDate(2054, 1, 18)
        )

        self.assertTrue(
            NepDate(2054, 1, 18) <=
            NepDate(2054, 1, 18)
        )

        self.assertTrue(
            NepDate(2054, 1, 18) <=
            NepDate(2084, 3, 1)
        )

    def test_gt_operator(self):
        self.assertGreater(
            NepDate(2012, 12, 12),
            NepDate(2012, 12, 11)
        )

        self.assertGreater(
            NepDate(2013, 1, 10),
            NepDate(2012, 12, 11)
        )

        self.assertFalse(
            NepDate(2012, 1, 12) >
            NepDate(2012, 12, 11)
        )

        self.assertTrue(
            NepDate(2012, 12, 12) >=
            NepDate(2012, 12, 12)
        )

        self.assertTrue(
            NepDate(2012, 12, 12) >=
            NepDate(2012, 12, 11)
        )

        self.assertFalse(
            NepDate(2012, 12, 10) >=
            NepDate(2012, 12, 11)
        )

    def test_add_operator(self):
        """
        Test the addition operator with timedelta
        """
        self.assertEqual(
            NepDate(2000, 1, 1) + timedelta(days=1),
            NepDate(2000, 1, 2)
        )

        self.assertEqual(
            NepDate(2000, 1, 30) + timedelta(days=9),
            NepDate(2000, 2, 9)
        )

        self.assertEqual(
            NepDate(2036, 12, 15) + timedelta(days=30),
            NepDate(2037, 1, 15)
        )

        self.assertEqual(
            NepDate.from_ad_date(date(2016, 5, 2)),
            NepDate(2073, 1, 20)
        )

        self.assertEqual(
            NepDate.from_ad_date(END_EN_DATE),

            NepDate(
                END_NP_YEAR, 12,
                NEPALI_MONTH_DAY_DATA[END_NP_YEAR][12 - 1]
            )
        )

        self.assertEqual(
            NepDate(2036, 12, 15) + timedelta(days=-5),
            NepDate(2036, 12, 10)
        )

    def test_sub_operator(self):
        date = NepDate(2012, 2, 12) - NepDate(2012, 2, 13)
        self.assertEqual(date.days, 1)

        date = NepDate(2012, 2, 12) - NepDate(2012, 1, 1)
        self.assertEqual(date.days, 42)

        date = NepDate(2073, 1, 6) - NepDate(2073, 3, 18)
        self.assertEqual(date.days, -75)

        date = NepDate(2072, 11, 6) - NepDate(2074, 4, 5)
        self.assertEqual(date.days, -518)

        date = NepDate(2072, 11, 6) - timedelta(days=6)
        self.assertEqual(date, NepDate(2072, 10, 29))

        self.assertEqual(
            NepDate(2036, 12, 15) - timedelta(days=-5),
            NepDate(2036, 12, 20)
        )

    def test_multi_random(self):
        """
        Do multiple random tests by generating data
        """
        for i in range(1, 1000):
            year = randint(values.START_NP_YEAR, values.END_NP_YEAR)
            month = randint(1, 12)
            day = randint(1, 28)

            np_date = NepDate(year, month, day)
            # Check the update
            np_date.update()
            # Convert the english date back to bikram sambat
            np_date_sec = NepDate.from_ad_date(np_date.en_date)
            self.assertTrue((np_date, np_date_sec))

            # Limit year choices so there is enough space for addition
            year = randint(values.START_NP_YEAR, values.END_NP_YEAR - 33)
            np_date = NepDate(year, month, day)
            days = randint(34, 834)
            added_date = np_date + timedelta(days=days)

            calculated_days = added_date - np_date
            self.assertTrue(calculated_days, days)

            # Now, subtract the same number of days from the last date
            first_calc_date = added_date - timedelta(days=days)
            self.assertEqual(first_calc_date, np_date)

    def test_names(self):
        np_date = NepDate(2073, 12, 23).update()
        self.assertEqual(np_date.en_weekday_name(), u"Budhabar")
        self.assertEqual(np_date.weekday_name(), u"वुधवार")
        self.assertEqual(np_date.weekday_name_short(), u'वुध')
        self.assertEqual(np_date.en_month_name(), u'Chaitra')
        self.assertEqual(np_date.month_name(), u'चैत')

if __name__ == '__main__':
    unittest.main()
