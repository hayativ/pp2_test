from datetime import date, timedelta
today = date.today()
yesterday = today - timedelta(1)
tomorrow = today + timedelta(1) 
dateFormat = "%d.%m.%y"
print(f'yesterday : {yesterday.strftime(dateFormat)}')
print(f'today : {today.strftime(dateFormat)}')
print(f'tomorrow : {tomorrow.strftime(dateFormat)}')