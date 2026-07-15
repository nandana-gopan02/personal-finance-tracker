transaction=[]
def show_menu():
    print("\n===== Personal Finance Tracker =====")
    print("1.Add Income")
    print("2.Add Expense")
    print("3.View Transaction")
    print("4.Exit")

def add_income():
   income=int(input("Enter Income Amount:"))
   income_store= f"Income : {income}"
   transaction.append(income_store)

def add_expence():
    expense=int(input("Enter Expense Amount: "))
    expense_store = f"Expense: {expense}"
    transaction.append(expense_store)

def view_transaction():
    if len(transaction)==0:
        print("No transaction found")
    else:
        print("\nTransaction")
        print("============")
    
    for i in transaction:
        print(i)



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