balance=input("Input Balance:")
withdrawal=input("Input Withdrawal:")
deposit=input("Input Deposit:")

balance=int(balance)
withdrawal=int(withdrawal)
deposit=int(deposit)

balance=balance-withdrawal+deposit
tax=0.01*(withdrawal+deposit)
balance=balance-tax

print("New Balance:",balance)