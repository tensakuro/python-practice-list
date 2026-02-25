spend = int(input("Enter the spend amount: "))
creditlimit = int(input("Enter credit limit: "))

due = 0

todo = input("Do you want to spend or pay? ").lower()

if todo == "spend":
    if spend <= creditlimit:
        creditlimit -= spend
        due += spend
        print("Spend successful")
    else:
        print("Insufficient credit limit")

elif todo == "pay":
    pay = int(input("Enter amount to pay: "))
    if pay <= due:
        due -= pay
        creditlimit += pay
        print("Payment successful")
    else:
        print("You cannot pay more than due")

else:
    print("Invalid option")

print("Remaining credit limit:", creditlimit)
print("Total due:", due)
