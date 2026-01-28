number_hour = float(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))
standard_hours = 44
standard_exceed_hours = max(0, number_hour - standard_hours)
readjusted_hours = standard_hours * hourly_rate + standard_exceed_hours * hourly_rate * 1.5
print("The total pay is:", readjusted_hours)

