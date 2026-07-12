
def show_menu():
    print("\n===== Personal Finance Tracker =====")
    print("1.Add Income")
    print("2.Add Expense")
    print("3.View Transaction")
    print("4.Exit")

def add_income():
    print("Income feature coming soon...")

def add_expence():
    print("Expense feature coming soon...")

def view_transaction():
    print("Show transactions message")


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