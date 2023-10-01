from datetime import datetime, timedelta

# Getting current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# Formatting date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_datetime)

# Calculating time difference
past_datetime = datetime(2023, 1, 1)
time_difference = current_datetime - past_datetime
print("Time Difference:", time_difference)

# Adding a time delta
new_datetime = current_datetime + timedelta(days=5)
print("Date 5 Days from Now:", new_datetime)
