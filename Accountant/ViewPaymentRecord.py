def view_payment_record():
    while True:
        print(f"""
              {"=" * 40}
              View Payment Record
              
              1. view payment record
              2. back
              """)
        choice = input("Enter choice: ")
        if choice == "1":
            try:
                with open("txt/Payment.txt", "r") as file:
                     lines = file.readlines()
                     if len(lines) == 0:
                         print("No Data in the file")
                         continue
                     else:
                         print(f"{"PaymentID":<15}{"MemberID":<15}{"FeeID":<15}{"Amount":<15}{"Status":<15}{"Date"}")
                     for line in lines:
                         data = line.strip().split(",")
                         if len(data) < 6:
                             print(f"Incomplete Data: {data}")
                         else:
                            print(f"{data[0]:<15}{data[1]:<15}{data[2]:<15}{data[3]:<15}{data[4]:<15}{data[5]}")
            except FileNotFoundError:
                print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice!")
            