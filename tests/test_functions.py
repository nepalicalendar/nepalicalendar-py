# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest
from datetime import date

from nepalicalendar.functions import check_valid_bs_range, check_valid_ad_range
from nepalicalendar import nepdate


class FunctionsTestCase(unittest.TestCase):
    """
    Tests for functions
    """

    def test_values_ad_range(self):
        self.assertTrue(
            check_valid_ad_range(
                date(2000, 1, 1)
            )
        )

        self.assertTrue(
            check_valid_ad_range(
                date(2034, 4, 13)
            )
        )

        # Invalid dates
        with self.assertRaises(ValueError):
            check_valid_ad_range(
                date(1942, 12, 2)
            )

        with self.assertRaises(ValueError):
            check_valid_ad_range(
                date(2035, 1, 1)
            )

        with self.assertRaises(ValueError):
            check_valid_ad_range(
                date(2034, 4, 14)
            )

    def test_values_bs_range(self):
        self.assertTrue(
            check_valid_bs_range(
                nepdate(2000, 1, 1)
            )
        )

        # Year less than min year
        with self.assertRaises(ValueError):
            check_valid_bs_range(
                nepdate(1999, 12, 30)
            )

        # Year greater than max year
        with self.assertRaises(ValueError):
            check_valid_bs_range(
                nepdate(2100, 1, 1)
            )

        # Month not in range
        with self.assertRaises(ValueError):
            check_valid_bs_range(
                nepdate(2050, 13, 1)
            )

        # Day not in range
        with self.assertRaises(ValueError):
            check_valid_bs_range(
                nepdate(2000, 1, 31)
            )

        with self.assertRaises(ValueError):
            check_valid_bs_range(
                nepdate(2078, 8, 30)
            )

        self.assertTrue(
            check_valid_bs_range(
                nepdate(2000, 1, 30)
            )
        )

        self.assertTrue(
            check_valid_bs_range(
                nepdate(2064, 3, 32)
            )
        )


if __name__ == '__main__':
    unittest.main()
