amount =5000
pin = 7248
user_pin = int(input("Enter the pin number:"))
if user_pin == pin:
    print("A/c no :1110703879 \n  Name : Kl Rahul")
    print("1.Deposit")
    print("2.Withdrawl")
    print("Blanace")
    choice = int(input("Enter your choice:"))
    # if user_pin1 == pin1:
    #     print("A/c no :11283746 \n  Name : Vimal")
    #     print("1.Deposit")
    #     print("2.Withdrawl")
    #     print("Blanace")
    #     choice1 = int(input("Enter your choice:"))

    if choice == 1:
        damount=int(input("Enater the deposit amount:"))
        amount = amount + damount
        print("your currently balance is :",amount)
    # if choice1== 1:
    #     damount1=int(input("Enater the deposit amount:"))
    #     amount1 = amount1 + damount1
    #     print("your currently balance is :",amount)
    elif choice==2:
        wamount=int(input("Enter the withdrawl amount :"))
        amount = amount - wamount
        print("your currently balance is :",amount)
    # elif choice1==2:
    #     wamount1=int(input("Enter the withdrawl amount :"))
    #     amount1 = amount1 - wamount1
    #     print("your currently balance is :",amount)

    elif choice == 3:
         print("your currently balance is :",amount)
    # elif choice1==3:
    #      print("your currently balance is :",amount)
    else:
        print("Invalid input")
else:
    print("Invalid user pin")
