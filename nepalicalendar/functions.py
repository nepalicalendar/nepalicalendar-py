# -*- coding: utf-8 -*-
"""
Provides nepali calendar related functions
"""
from . import values


def check_valid_ad_range(date):
    """
    Checks if the english date is in valid range for conversion
    """
    if date < values.START_EN_DATE or date > values.END_EN_DATE:
        raise ValueError("Date out of range")
    return True


def check_valid_bs_range(date):
    """
    Checks if the nepali date is in valid range for conversion
    """
    ERR_MSG = "%s out of range" % str(date)

    if date.year < values.START_NP_YEAR or date.year > values.END_NP_YEAR:
        raise ValueError(ERR_MSG)
    if date.month < 1 or date.month > 12:
        raise ValueError(ERR_MSG)
    if date.day < 1 or date.day > values.NEPALI_MONTH_DAY_DATA[date.year][date.month - 1]:
        raise ValueError(ERR_MSG)
    return True

def nepali_number(number):
    """
    Convert a number to nepali
    """
    nepnum = ""
    for n in str(number):
        nepnum += values.NEPDIGITS[int(n)]
    return nepnum
