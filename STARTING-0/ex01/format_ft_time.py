import datetime

current_time = datetime.datetime.now()
current_time_seconds = current_time.timestamp()

print("Seconds since January 1, 1970 :", current_time_seconds, "or", "{:.2e}".format(current_time_seconds), "in scientific notation")
print(current_time.strftime("%b %d %Y"))