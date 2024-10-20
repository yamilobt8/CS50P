months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

def numeric_date(date):
    try:
        month, day, year = map(int, date.split('/'))
        if 1 <= month <= 12 and 1 <= day <= 31:
            return f'{year:04d}-{month:02d}-{day:02d}'
    except ValueError:
        return None

def long_date(date):
    try:
        month_and_day, year = date.split(',')
        month, day = month_and_day.split()
        month = months.get(month)
        day = int(day.strip())
        if month and 1 <= day <= 31:
            return f'{year.strip():04d}-{month:02d}-{day:02d}'
    except:
        return None

while True:
    date = input('Date: ').strip()
    if '/' in date:
        result = numeric_date(date)
    else:
        result = long_date(date)
    
    if result:
        print(result)
        break