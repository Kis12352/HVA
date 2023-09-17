from datetime import datetime, timedelta
import time

def calculate_time_until_birthday(birthday_date):
    today = datetime.today()
    next_birthday = birthday_date.replace(year=today.year)

    if today > next_birthday:
        next_birthday = next_birthday.replace(year=today.year + 1)

    time_until_birthday = next_birthday - today
    return time_until_birthday

def main():
    while True:
        birthday_str = input("Enter your birthday (YYYY-MM-DD): ")

        try:
            birthday_date = datetime.strptime(birthday_str, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
            continue

        if birthday_date > datetime.today():
            print("Your birthday should be in the past. Please enter a valid date.")
            continue

        time_until_birthday = calculate_time_until_birthday(birthday_date)

        days = time_until_birthday.days
        hours, remainder = divmod(time_until_birthday.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"You have {days} days")

        time.sleep(3)  # Pause for 3 seconds

        print(f"{hours} hours")

        time.sleep(3)  # Pause for 3 seconds

        print(f"{minutes} minutes and")

        time.sleep(3)  # Pause for 3 seconds

        print(f"{seconds} seconds until your birthday!")

        play_again = input("Calculate another birthday? (yes/no): ")
        if play_again.lower() != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
