from domain.service import StatisticService
from datetime import datetime, timedelta


start = datetime(2013, 9, 1)
end = datetime(2013, 12, 1)

while start < end:
    print "Loading stats for date %s" % start
    StatisticService().load_sem_stats(day=start.strftime('%Y%m%d'))
    start += timedelta(days=1)

