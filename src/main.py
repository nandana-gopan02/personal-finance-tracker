print("===== Personal Finance Tracker =====")
print("1.Add Income")
print("2.Add Expence")
print("3.View Transaction")
print("4.Exit")

choice=int(input("Enter a choice: "))

if(choice ==1):
    print("Show income message")
elif(choice==2):
    print("Show expense message")
elif(choice==3):
    print("Show transactions message")
elif(choice==4):
    print("ThankYou, see you again")
else:
    print("Invalid choice")