
def show_menu():
    print("===== Personal Finance Tracker =====")
    print("1.Add Income")
    print("2.Add Expence")
    print("3.View Transaction")
    print("4.Exit")

def add_income():
    print("Show income message")

def add_expence():
    print("Show expense message")

def show_transaction():
    print("Show transactions message")



show_menu()
choice=int(input("Enter a choice: "))

if(choice ==1):
    add_income()
elif(choice==2):
    add_expence()
elif(choice==3):
    show_transaction()
elif(choice==4):
    print("ThankYou, see you again")
else:
    print("Invalid choice")