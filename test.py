import sys
from datetime import datetime, timedelta

input_date = datetime.strptime(sys.argv[-1], "%m-%d-%y")

print(f"""180 Days: {(input_date - timedelta(days=180))}
    \n120 Days: {(input_date - timedelta(days=120))}
    \n60 Days: {(input_date - timedelta(days=60))}""")
