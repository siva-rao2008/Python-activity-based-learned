# Attendance Eligibility.

classes = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

percentage = (attended / classes) * 100

print("Attendance Percentage:", percentage)

if percentage >= 75:
    print("Eligible for examination")
else:
    print("Not eligible for examination")
