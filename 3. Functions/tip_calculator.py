# Tip Calculator

def tip_calculator(bill_amount, tip_percent):
    total = bill_amount * (1 + (tip_percent / 100))
    return total

# User input
bill_amount = float(input("Enter bill amount: "))
tip_percent = float(input("Enter tip percent: "))

# Output
total_amount = tip_calculator(bill_amount, tip_percent)
print(f"Total amount including tip: {total_amount:.2f}")
