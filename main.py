import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()
name = ""
account_number = ""
balance = 0 

while True:
    print("\n===== BANKING MANAGEMENT SYSTEM =====")
    print("1.  Create Account")
    print("2.  Check Account")
    print("3.  Deposit Money")
    print("4.  Withdraw Money")
    print("5.  Exit")

    choice = input("Enter Choice: ")
     
    if choice == "1":
        name = input("Enter Name: ")
        account_number = input("Enter Account Number: ")
        balance = float(input("Enter Initial Deposit: "))

        cursor.execute(
            "INSERT INTO accounts VALUES (?, ?, ?)",
            (account_number, name, balance))

        conn.commit()

        print("Account Saved Successfully") 

    elif choice == "2":
        acc_no = input("Enter Account Number: ")

        cursor.execute(
            "SELECT * FROM accounts WHERE account_number=?",
            (acc_no,)
        )

        account = cursor.fetchone()

        if account:

            print("\n----- ACCOUNT DETAILS -----")
            print("Account Number:", account[0])
            print("Name:", account[1])
            print("Balance:", account[2])

        else:

            print("Account Not Found")

    elif choice == "3":
        
        acc_no = (input("Enter Account Number: ")) 

        amount = float(input("Enter Deposit Amount: "))
        
        cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE account_number = ?",
            (amount, acc_no)
        )

        conn.commit()

        print("Money Deposited Successfully")


    elif choice == "4":
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Withdrawal Amount: "))

        cursor.execute(
            "SELECT balance FROM accounts WHERE account_number=?",
            (acc_no,)
        )

        result = cursor.fetchone()

        if result: 

            current_balance = result[0]

            if amount <= current_balance:

                cursor.execute(
                    "UPDATE accounts SET balance = balance - ? WHERE account_number=?",
                    (amount, acc_no)
                )

                conn.commit()

                print("Withdrawal Successful")

            else: 
                print("Insufficient Balance")

        else: 
            print("Account Not Found")

        if amount <= balance:
            balance = balance - amount 
            print("Withdrawal Successful")
            print("Remaining Balance:", balance)

        else:
            print("Insufficient Balance")
    elif choice == "5":

        print("Goodbye")
        break
        