def generate_income_summary():
    while True:
        print(f"""
            {"=" * 40}
            Generate Income Summary
            
            1. generate income summary
            2. back
            {"=" * 40}
            """)
        choice = input("Enter Choice: ")
        if choice == "1":
            total = 0
            try:
                with open("txt/Payment.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        if len(data) >= 5:
                            if data[4] == "Paid":
                                total += float(data[3])
                    print("Total Payment Summary: ", total)
            except FileNotFoundError:
                print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong choice")