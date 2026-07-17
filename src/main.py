transactions=[]
def show_menu():
    print("\n===== Personal Finance Tracker =====")
    print("1.Add Income")
    print("2.Add Expense")
    print("3.View Transaction")
    print("4.Exit")

def add_income():
    income=int(input("Enter Income Amount:"))

    if(income<0):
       print("Amount cannot be negative.")
    else:
        transaction={
            "Type":"Income",
            "Amount":income
        }
        transactions.append(transaction)
#    income_store= f"Type: Income ,Income : {income}"
#    transaction.append(income_store)

def add_expence():
    expence=int(input("Enter Expense Amount: "))
    if(expence<0):
        print("Amount cannot be negative.")
    else:
        transaction={
            "Type":"Expence",
            "Amount":expence
        }
        transactions.append(transaction)
    # expense_store = f"Expense: {expense}"
    # transaction.append(expense_store)

def view_transaction():
    if len(transactions)==0:
        print("No transaction found")
    else:
        print("\nTransaction")
       
    
    for transaction in transactions:
        print("-------------------")
        print("\nType: ",transaction["Type"])
        print("\nAmount: ",transaction["Amount"])
    print("-----------------")
      



while True:
    show_menu()
    choice=int(input("Enter a choice: "))
    if(choice ==1):
     add_income()
    elif(choice==2):
         add_expence()
    elif(choice==3):
        view_transaction()
    elif(choice==4):
        print("ThankYou, see you again")
        break
    else:
        print("Invalid choice")