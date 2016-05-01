# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest
from nepcal import nepdate
from datetime import date

class NepdateTestCase(unittest.TestCase):
    """
    Tests for nepdate class
    """
    def test_from_ad_date(self):
        np_date = nepdate.from_ad_date(date.today())
        self.assertEqual(np_date.year, date.today().year)



if __name__ == '__main__':
    unittest.main()
