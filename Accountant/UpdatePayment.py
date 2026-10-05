from Accountant import Function as F
def update_payment():
    while True:
        print(f"""
              {"=" * 40}
              Update Payment
              
              1. update payment
              2. back
              {"=" * 40}

              """)
        choice = input("Enter Choice: ")
        if choice == "1":
            updated_record = []
            found = False
            updated = False
            try:
                with open("txt/Payment.txt", "r") as file:
                    paymentID = input("Enter PaymentID: ")
                    for lines in file:
                        data = lines.strip().split(",")
                        if data[0] == paymentID:
                            found = True
                            
                            print(f"""
                                  {"=" * 40}
                                  Current Payment Information
                                  
                                  PaymentID = {paymentID}
                                  MemberID = {data[1]}
                                  BookingID = {data[2]}
                                  Amount = {data[3]}
                                  Payment Status = {data[4]}
                                  Payment Date = {data[5]}
                                  {"=" * 40}\n
                                  """)
                            print(f"""
                                Which One do you want to update!
                                                                
                                    1. Amount
                                    2. Payment Status
                                    3. Payment Date
                                    4. Quit
                                    """)                           
                            while True:
                               
                                choice = input("Enter Choice: ")
                                if choice == "1":
                                    while True:
                                        new_amount = input("Enter New Amount: ")
                                        try:
                                            if float(new_amount) > 0:
                                                data[3] = new_amount
                                                updated = True
                                                break
                                            else:
                                                print("Amount must be greater than 0")
                                        except ValueError:
                                            print("Invalid Amount")
                                elif choice == "2":
                                    new_payment_status = input("Enter New Payment Status:(Paid/Unpaid): ").strip().lower()
                                    if new_payment_status == "paid":
                                        
                                        data[4] = new_payment_status
                                        updated = True
                                        break
                                    elif new_payment_status == "unpaid":
                                        data[4] = new_payment_status
                                        updated = True
                                        break
                                    else:
                                        print("Invalid Payment Status")
                                elif choice == "3":
                                    while True:
                                        new_payment_date = input("Enter New Payment Date :")
                                        if not F.check_date(new_payment_date):
                                            print("Invalid Date, Try again")
                                        else:   
                                            data[5] = new_payment_date
                                            updated = True
                                            break
                                elif choice == "4":
                                    break
                                else:
                                    print("Wrong Choice!")
                        updated_record.append(",".join(data) + "\n")
            except FileNotFoundError:
                print("File is not found!")
                continue
            if found:
                if updated:
                    try:
                        with open("txt/Payment.txt", "w") as file:
                            file.writelines(updated_record)
                            print("Payment updated successfully")
                    except FileNotFoundError:
                        print("File is not found")
                else:
                    print("No changes were made")
            else:
                print("Invalid Payment ID")
        elif choice == "2":
            return
        else:
            print("Wrong Choice")
                                

                        
                        