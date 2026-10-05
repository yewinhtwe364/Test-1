def generate_outstanding_list():
    while True:
        print(f"""
            {"=" * 40}
            Generate Outstanding List
            
            1. generate outstanding list
            2. back
            {"=" * 40}
            """)
        choice = input("Enter Choice: ")
        if choice == "1":
            try:
                with open("txt/Payment.txt", "r") as file:
                    print(f"\n{"PaymentID":<15}{"MemberID":<15}{"FeeID":<15}{"Amount":<15}{"Status":<20}{"Date"}")
                    for line in file:
                        data = line.strip().split(",")
                        if len(data) >= 6:
                            if data[4].lower() == "unpaid":
                                print(f"{data[0]:<15}{data[1]:<15}{data[2]:<15}{data[3]:<15}{data[4]:<20}{data[5]}")
            except FileNotFoundError:
                print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice")