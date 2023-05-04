import datetime
# Get the current date and time
current_datetime = datetime.datetime.now()
timestamp = current_datetime.strftime(f"%d-%b-%Y (%H:%M:%S.%f)")

# For more directives like %d or %b visit
# https://www.w3schools.com/python/python_datetime.asp

print(timestamp)
