# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest
from nepcal import *
from datetime import date, timedelta


class NepdateTestCase(unittest.TestCase):
    """
    Tests for nepdate class
    """

    def test_from_ad_date(self):
        np_date = nepdate.from_ad_date(date.today())
        # self.assertEqual(np_date.year, date.today().year)

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


if __name__ == '__main__':
    unittest.main()
