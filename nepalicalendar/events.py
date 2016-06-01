# -*- coding: utf-8 -*-

"""
Defines different constant events in nepali and english calendar
"""

from collections import defaultdict


NEPALI_EVENTS = defaultdict(lambda: [])


# The events are represented as below
# NEPALI_EVENTS[(month, day)] = (Event name, holiday)
# Holiday represents if there is a holiday in that day

NEPALI_EVENTS[(1, 1)] = [(u"नेपाली नयाँ वर्ष", 1)]
NEPALI_EVENTS[(1, 8)] = [(u"छन्द दिवस", 0)]
NEPALI_EVENTS[(1, 24)] = [(u"किरात समाजसुधार दिवस", 0)]
NEPALI_EVENTS[(1, 11)] = [(u"लोकतन्त्र दिवस", 1)]
NEPALI_EVENTS[(2, 15)] = [(u"गणतन्त्र दिवस", 1)]
NEPALI_EVENTS[(3, 15)] = [(u"दहि-चिउरा खाने दिन", 0)]
NEPALI_EVENTS[(4, 15)] = [(u"खिर खाने दिन", 0)]
NEPALI_EVENTS[(5, 1)] = [(u"भाद्र सङ्क्रान्ति", 0)]
NEPALI_EVENTS[(5, 29)] = [(u"राष्ट्रिय बाल दिवस", 0)]
NEPALI_EVENTS[(9, 27)] = [(u"पृथ्वी जयन्ती", 0)]
NEPALI_EVENTS[(10, 1)] = [(u"माघे सङ्क्रान्ति", 0)]
NEPALI_EVENTS[(10, 16)] = [(u"शहीद दिवस", 1)]
NEPALI_EVENTS[(11, 7)] = [(u"प्रजातन्त्र दिवस", 1)]

ENGLISH_EVENTS = defaultdict(lambda: [])

ENGLISH_EVENTS[(1, 1)] = [(u"अंग्रेजी नयाँ वर्ष", 0)]
ENGLISH_EVENTS[(2, 14)] = [(u"भ्यालेन्टाईन डे", 0)]
ENGLISH_EVENTS[(3, 22)] = [(u"विश्व पानी दिवस", 0)]
ENGLISH_EVENTS[(3, 24)] = [(u"विश्व क्षयरोग बिरुद्ध दिवस", 0)]
ENGLISH_EVENTS[(4, 1)] = [(u"विश्व मूर्ख दिवस", 0)]
ENGLISH_EVENTS[(4, 7)] = [(u"विश्व स्वास्थ्य दिवस", 0)]
ENGLISH_EVENTS[(5, 1)] = [(u"मजदुर दिवस", 0)]
ENGLISH_EVENTS[(5, 3)] = [(u"प्रेस स्वतन्त्रता दिवस", 0)]
ENGLISH_EVENTS[(5, 1)] = [(u"विश्व दुरसंचार दिवस", 0)]
ENGLISH_EVENTS[(5, 31)] = [(u"विश्व धुम्रपानरहित दिवस", 0)]
ENGLISH_EVENTS[(6, 5)] = [(u"विश्व वातावरण दिवस", 0)]
ENGLISH_EVENTS[(6, 20)] = [(u"विश्व शरणार्थी दिवस", 0)]
ENGLISH_EVENTS[(7, 11)] = [(u"अन्तराष्टिय जनसङ्ख्या दिवस", 0)]
ENGLISH_EVENTS[(8, 12)] = [(u"विश्व युवा दिवस", 0)]
ENGLISH_EVENTS[(9, 8)] = [(u"शिक्षा तथा साक्षरता दिवस", 0)]
ENGLISH_EVENTS[(9, 27)] = [(u"विश्व पर्यटन दिवस", 0)]
ENGLISH_EVENTS[(10, 1)] = [(u"अन्तराष्टिय जेष्ठ नागरिक दिवस", 0)]
ENGLISH_EVENTS[(10, 9)] = [(u"विश्व हुलाक दिवस", 0)]
ENGLISH_EVENTS[(10, 13)] = [(u"प्राकृतिक विपत्ति न्यूनिकरण दिवस", 0)]
ENGLISH_EVENTS[(10, 14)] = [(u"विश्व गुणस्तर दिवस", 0)]
ENGLISH_EVENTS[(10, 16)] = [(u"विश्व खाद्य दिवस", 0)]
ENGLISH_EVENTS[(10, 16)] = [(u"विश्व गरिबी निवारण दिवस", 0)]
ENGLISH_EVENTS[(10, 24)] = [(u"संयुक्त राष्ट्रसंघ दिवस", 0)]
ENGLISH_EVENTS[(11, 14)] = [(u"विश्व मधुमेह दिवस", 0)]
ENGLISH_EVENTS[(11, 17)] = [(u"अन्तराष्टिय विद्यार्थी दिवस", 0)]
ENGLISH_EVENTS[(11, 20)] = [(u"विश्व बाल अधिकार दिवस", 0)]
ENGLISH_EVENTS[(11, 21)] = [(u"विश्व टेलिभिजन दिवस", 0)]
ENGLISH_EVENTS[(12, 1)] = [(u"विश्व एड्स दिवस", 0)]
ENGLISH_EVENTS[(12, 7)] = [(u"अन्तर्राष्ट्रीय नागरिक उड्डयन दिवस", 0)]
ENGLISH_EVENTS[(12, 9)] = [(u"विश्व भ्रष्टाचारविरुद्द दिवस", 0)]
ENGLISH_EVENTS[(12, 10)] = [(u"विश्व मानव अधिकार दिवस", 0)]
