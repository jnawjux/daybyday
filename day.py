# Basic script for calculating the days from an input date, set with defaults for my purposes.

import sys
from datetime import datetime, timedelta

input_date = datetime.strptime(sys.argv[-1], "%m-%d-%y")


def days_from(input_day, days_to_remove):
    """Returns a formatted date of the days from the input.
    Args: input_day (as datetime object), days_to_remove (int)
    Returns: date minus specified days"""
    return (input_day - timedelta(days=days_to_remove)).strftime("%m-%d-%y")


print(f"""180 Days: {days_from(input_date, 180)}
    \n120 Days: {days_from(input_date, 120)}
    \n60 Days: {days_from(input_date, 60)}""")
