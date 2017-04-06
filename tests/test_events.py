# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest
from nepalicalendar import NepDate


class EventsTestCase(unittest.TestCase):
    """
    Test case for the Events
    """

    def test_events(self):
        """
        Test the events
        """
        # TODO: Add more tests
        nep_date = NepDate(2033, 1, 1)
        nep_date.update()
        self.assertEqual(nep_date.events_list(), [(u"नेपाली नयाँ वर्ष", 1)])
        self.assertEqual(NepDate(2073, 9, 17).update().events_list(), [(u"अंग्रेजी नयाँ वर्ष", 0)])
        self.assertEqual(NepDate(2073, 9, 17).update().events_name(), [u"अंग्रेजी नयाँ वर्ष"])
        self.assertTrue(NepDate(2053, 1, 11).update().is_event_holiday())
        self.assertTrue(NepDate(2054, 1, 11).update().is_holiday())
