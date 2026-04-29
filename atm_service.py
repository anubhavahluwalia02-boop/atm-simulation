balance = 1000
transactions = []

def get_balance():
    return balance

def deposit(amount):
    global balance
    if amount <= 0:
        return "Invalid amount"
    balance += amount
    transactions.append(f"Deposited: ₹{amount}")
    return "Deposit successful"

def withdraw(amount):
    global balance
    if amount <= 0:
        return "Invalid amount"
    if amount > balance:
        return "Insufficient balance"
    balance -= amount
    transactions.append(f"Withdrawn: ₹{amount}")
    return "Withdrawal successful"

def get_statement():
    if not transactions:
        return ["No transactions yet"]
    return transactions