from Accountant import Function as F
def record_payment():
    while True:
        print(f"""
              {"=" * 40}
              Record Payment
              
              1. record payment
              2. back
              {"=" * 40}
              """)
        choice = input("Enter Choice: ")
        if choice  == "1":
            paymentID = F.generate_paymentID()
            memberID = input("Enter MemberID: ")
            if not F.check_member(memberID):
                print("Invalid Memberid")
                return
            else:
                while True:
                    feetype = input("Enter FeeType(Booking Fee (or) Annual Fee): ").strip().lower()
                    if feetype == "booking fee":
                        bookingID = input("Enter Booking ID: ")
                        if not F.check_booking(bookingID):
                            print("Invalid BookingID!")
                            return
                        else:
                            planID= bookingID
                            amount = input("Enter Amount: ")
                            break
                    elif feetype == "annual fee":
                        while True:
                            planID = input("Enter Membership Plan ID: ")
                            if not F.check_membershipplan(planID):
                                print("Invalid Membershipplan")
                            else:
                                break
                        amount = F.fee_amount(planID)
                        found = False
                        try:
                            with open("txt/Membership.txt", "r") as file:
                                for line in file:
                                    data = line.strip().split(",")
                                    if data[1] == memberID and data[2] == planID:
                                        found = True
                                        break
                        except FileNotFoundError:
                            print("File is not found!")
                        if found:
                            break
                        else:
                            print("This member does not register this plan")
                            return
                    else:
                        print("Wrong Choice")
                payment_status = input("Enter Payment Status (Paid/Unpaid): ")
                while True:
                    Date = input("Enter Payment Date: ")
                    if not F.check_date(Date):
                        print("Invalid Date. Try Again")
                    else:
                        break
                try:
                    with open("txt/Payment.txt", "a") as file:
                        file.write(f"{paymentID},{memberID},{planID},{amount},{payment_status},{Date}\n")
                        print("Payment recorded successfully!")
                        print("Payment ID = ", paymentID)
                except FileNotFoundError:
                    print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice")