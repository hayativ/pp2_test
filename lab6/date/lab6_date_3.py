from datetime import datetime
dateFormat = '%H:%M:%S %d.%m.%y'
dt = datetime.today().replace(microsecond=0).strftime(dateFormat)
print(dt)