# Assignment: US Federal Personal Income Tax Calculator for 2009
# Agboola Jesutofunmi Enoch
# Matric No: BU24SEN1006
# Department: Software Engineering

# This program calculates the federal income tax based on filing status and taxable income
# using the 2009 tax brackets

# this aspect is to ask user for filing status
print("US Federal Income Tax Calculator (2009)")
print("-------------------------------------")
print("Enter your filing status:")
print("0 - Single")
print("1 - Married Filing Jointly ")
print("2 - Married Filing Separately")
print("3 - Head of Household")
status = int(input("Enter number (0-3): "))

# Get taxable income
income = float(input("Enter your taxable income: "))

# Define the tax brackets and rates for each filing status
if status == 0:  # Single
    brackets = [8350, 33950, 82250, 171550, 372950]
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]
elif status == 1:  # Married Jointly
    brackets = [16700, 67900, 137050, 208850, 372950]
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]
elif status == 2:  # Married Separately
    brackets = [8350, 33950, 68525, 104425, 186475]
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]
elif status == 3:  # Head of Household
    brackets = [11950, 45500, 117450, 190200, 372950]
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]
else:
    print("Invalid filing status! Please enter 0, 1, 2, or 3.")
    exit()

# Calculate the tax
tax = 0.0
previous_bracket = 0

for i in range(len(brackets)):
    if income > brackets[i]:
        tax += (brackets[i] - previous_bracket) * rates[i]
        previous_bracket = brackets[i]
    else:
        tax += (income - previous_bracket) * rates[i]
        break
else:
    # If income is above the last bracket
    tax += (income - previous_bracket) * rates[-1]

# Print the result
print("\nYour federal income tax is: ${:.2f}".format(tax))

print("\nThank you for using my company tax calculator! 😊")