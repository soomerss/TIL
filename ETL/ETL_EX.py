from datetime import timedelta, date,datetime
from pytz import timezone

datetime.now(timezone('utc'))
today = datetime.now(timezone('utc'))


print(today)