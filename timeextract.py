import os
import datetime

# Specify the file path
file_path = input("Enter the file path: ")

# Retrieve file creation time in seconds with high precision
creation_time = os.stat(file_path).st_ctime

# Convert it to a datetime object with microsecond precision
creation_datetime = datetime.datetime.fromtimestamp(creation_time)

print(f"Creation time: {creation_datetime}")