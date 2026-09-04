# 01_transactions.py

transactions = [1200, 450, 800, 1500, 2300, 700, 100]

total = 0

for transaction in transactions:
    total += transaction

print("Total Transaction Value:", total)

highest = transactions[0]
lowest = transactions[0]

for transaction in transactions:
    if transaction > highest:
        highest = transaction

    if transaction < lowest:
        lowest = transaction

print("Highest Transaction:", highest)
print("Lowest Transaction:", lowest)