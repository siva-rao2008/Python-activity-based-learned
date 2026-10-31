# Student Marks and Result.

a = int(input("Enter marks in subject 1: "))
b = int(input("Enter marks in subject 2: "))
c = int(input("Enter marks in subject 3: "))

total = a+b+c
average = total / 3

print("Total Marks:", total)
print("Average Marks:", average)

if a >= 35 and b >= 35 and c >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")
