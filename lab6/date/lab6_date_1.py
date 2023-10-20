from datetime import date, timedelta
result = date.today() - timedelta(5)
dateFormat = "%d.%m.%y"
print(f'current date : {date.today().strftime(dateFormat)}')
print(f'date 5 days before : {result.strftime(dateFormat)}')
