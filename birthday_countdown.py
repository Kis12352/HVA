from datetime import datetime, timedelta

def calculate_time_until_birthday(birthday_date):
    today = datetime.today()
    next_birthday = birthday_date.replace(year=today.year)

    if today > next_birthday:
        next_birthday = next_birthday.replace(year=today.year + 1)

    time_until_birthday = next_birthday - today
    return time_until_birthday

def main():
    birthday_str = input("Enter your birthday (YYYY-MM-DD): ")
    birthday_date = datetime.strptime(birthday_str, '%Y-%m-%d')
    time_until_birthday = calculate_time_until_birthday(birthday_date)

    days = time_until_birthday.days
    hours, remainder = divmod(time_until_birthday.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Time until your birthday:")
    print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

if __name__ == "__main__":
    main()






