from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f" Current Date and Time: {formatted_date}")

def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print(f" Future Date after {days_to_add} days: {formatted_future}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def main():
    print("===  Date & Time Explorer ===")
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
