#time blindness estimator

from datetime import datetime 
import csv
import os


taskname = input("Task Name:")
taskname = taskname.strip().lower()

category = input("Category (optional): ")
category = category.strip().lower()

expectedtime = float(input("Expected Time (in minutes):"))
print("Expected Time:" + str(expectedtime) + " minutes")

actualtime = float(input("Actual Time (in minutes):"))
print("Actual Time:" + str(actualtime) + " minutes")

time_difference = actualtime - expectedtime
abs_time_diff = abs(time_difference)
print("You were off by " + str(abs_time_diff) + " minutes.")

if abs_time_diff < 3:
  print("⏱️ Nice! You're a time wizard.")
elif abs_time_diff < 10:
  print("🕰️ Not bad, you’re in the ballpark.")
else:
  print("🌀 Time blindness alert!")

notes = input("Notes (optional): ")
print("Notes: " + str(notes))
notes = notes.strip().lower()
timestamp = datetime.now()

file_exists = os.path.exists("timeblindnesslog.csv")

with open("timeblindnesslog.csv", "a", newline="") as log:
  writer = csv.writer(log)
  if not file_exists:
    writer.writerow(["Task Name", "Category", "Timestamp", "Expected Time", "Actual Time", "Time Difference", "Notes"])
  writer.writerow([taskname, category, timestamp, expectedtime, actualtime, time_difference, notes])
  
  