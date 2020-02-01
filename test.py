import sys
from datetime import datetime, timedelta

test = "12-1-19"

input_date = datetime.strptime(test, "%m-%d-%y")
print(f"180 Days: {(input_date - timedelta(days=180))}\n 120 Days: {(input_date - timedelta(days=120))}\n 60 Days: {(input_date - timedelta(days=60))}")
