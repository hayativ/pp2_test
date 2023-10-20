from datetime import datetime

date1 = datetime.strptime('2023-09-26 00:00:01', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
difference = date2 - date1
result = difference.days * 24 * 3600 + difference.seconds
print(result)