import sys
from datetime import datetime, timedelta

input_date = datetime.strptime(sys.argv[-1], "%m-%d-%y")

print(f"""180 Days: {(input_date - timedelta(days=180)).strftime("%m-%d-%y")}
    \n120 Days: {(input_date - timedelta(days=120)).strftime("%m-%d-%y")}
    \n60 Days: {(input_date - timedelta(days=60)).strftime("%m-%d-%y")}""")
