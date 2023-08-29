import datetime, bday_message

today = datetime.date.today()
my_next_birthday = datetime.date(2023, 8, 31)

days_away = my_next_birthday - today

if today == my_next_birthday:
    print(bday_message.random_message)
else:
    print(f'My next birthday is {days_away.days} days from today!')