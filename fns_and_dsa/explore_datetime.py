from datetime import datetime
def display_current_datetime():
	current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print(current_date)


def calculate_future_date():
	d = int(input("Enter the number of days to add to the current date:"))
	future_date = datetime.now - datetime.timedelta(days=d)
	print(future_date.strftime("%Y-%m-%d"))
