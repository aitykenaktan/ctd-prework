# This program calculates earnings for a work day.

name = input("What is your name? ")
hours = float(input("How many hours did you work today? "))
hourly_rate = 20

total_pay = hours * hourly_rate

print(name, "earned $", total_pay)

if hours >= 8:
    print("You worked a full day.")
else:
    print("You worked less than a full day.")
