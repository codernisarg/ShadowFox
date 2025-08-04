# 1. Create a list of your friends' names. The list should have at least 5 names. Create a list of tuples. Each tuple should contain a friend's name and the length of the name.
# For example, if someone’s name is Aditya, the tuple would be: ('Aditya', 6)

friends = ["Sudhir", "Dhiru", "Kratos", "David", "Baba" , "Bhidu"]
name_length = [(name, len(name)) for name in friends]

print("List of name-length tuples: ",name_length)

# 2. You and your partner are planning a trip, and you want to track expenses. Create two dictionaries, one for your expenses and one for your partner's expenses. Each dictionary should contain at least 5 expense categories and their corresponding amounts.
#For example:Your expenses
#        your_expenses = {
#           "Hotel": 1200,
#           "Food": 800,
#           "Transportation": 500,
#           "Attractions": 300,
#           "Miscellaneous": 200}
#Your partner's expenses
#partner_expenses = {
#   "Hotel": 1000,
#   "Food": 900,
#   "Transportation": 600,
#   "Attractions": 400,
#   "Miscellaneous": 150}
# Calculate the total expenses for each of you and print the results. Determine who spent more money overall and print the result. Find out the expense category where there is a significant difference in spending between you and your partner. Print the category and the difference.

your_expenses = {
    "Hotel": 4000,
    "Food": 1000,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 3000,
    "Food": 1500,
    "Transportation": 300,
    "Attractions": 400,
    "Miscellaneous": 300
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

if your_total > partner_total:
    print("You spent more overall.")
elif partner_total > your_total:
    print("Your partner spent more overall.")
else:
    print("Both of you spent the same amount.")

max_diff = 0
max_category = ""

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])# Calculate the absolute difference between your expenses and your partner's expenses
    if diff > max_diff:
        max_diff = diff
        max_category = category

print("The category with the biggest difference is",max_category,"with a difference of ₹" ,max_diff)
