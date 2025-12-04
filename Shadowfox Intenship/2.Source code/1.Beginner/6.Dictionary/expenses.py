my_expenses = {"Hotel":1200, "Food":800, "Transportation":500, "Attractions":300, "Miscellaneous":200}
partner_expenses = {"Hotel":1000, "Food":900, "Transportation":600, "Attractions":400, "Miscellaneous":150}

my_total_expenses = sum(my_expenses.values())
partner_total_expenses = sum(partner_expenses.values())

print(my_total_expenses)
print(partner_total_expenses)

if my_total_expenses > partner_total_expenses:
    print("My Expenses is greater")
elif partner_total_expenses > my_total_expenses:
    print("My Partner's Expenses is Greater")
else:
    print("Both Spend Equally")

max_diff = 0
max_category = ""

for category in my_expenses:
    difference = abs(my_expenses[category] - partner_expenses[category])
    
    if difference > max_diff:
        max_diff = difference
        max_category = category

print("Category with highest difference:", max_category)
print("Difference amount:", max_diff)
