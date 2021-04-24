import time

print("please insert your card")
time.sleep(5)
password = 1234
pin = int(input('enter your atm pin'))
balance = 5000

if pin == password:

    print("""
        1 == balance
        2 == withdraw balance
        3 == deposit balance
        4 == exit
        """
          )

    try:
        option = int(input("plz enter your choice"))
    except:
        print('plz enter valid option')

    if option == 1:
        print("your current balance is{balance}")

        print("===========================================")
        print("===========================================")
        print("===========================================")

    if option == 2:
        withdraw_amount = int(input("plz enter withdraw_amount"))
        balance = balance - withdraw_amount
        print(f"{withdraw_amount} is debited from your account")
        print(f"your updated balance is {balance}")

        print("===========================================")
        print("===========================================")

        if option == 3:
            deposit_amount = int(input("plz enter deposit amount"))
            balance = balance + deposit_amount

            print("===========================================")
            print("===========================================")


            print(f"{deposit_amount} is credited to your account")
            print(f"your updated balance is {balance} ")
else:
    print("wrong pin please try again")