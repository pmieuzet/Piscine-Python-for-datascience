import time

current_time = time.time()

print("Seconds since January 1, 1970 :", current_time, "or", "{:.2e}".format(current_time), "in scientific notation")
print(time.strptime(time.ctime(current_time), "%m %d %y"))