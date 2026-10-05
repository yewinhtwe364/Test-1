def View_Booking():
    while True:
        print(f"""
            {"=" * 40}
            View Booking
          
            1. View Booking
            2. Back to Administrator Menu
            {"=" * 40}
          
          """)
        choice = input("Enter Choice: ")
        if choice == "1":
            try:
                with open("txt/Booking.txt", "r") as file:
                    lines = file.readlines()
                    if len(lines) == 0:
                        print("No Data in the file")
                        continue
                    print(f"{"BookingID":<10}{"MemberID":<10}{"ClassID":<10}{"Booking Date":<25}{"Class Time":<25}{"Lecturer":<25}{"Status":<10}")
                    for line in lines:
                        data = line.strip().split(",")
                        if len(data) < 7:
                            print(f"Incomplete Data: {data}")
                        else:
                            print(f"{data[0]:<10}{data[1]:<10}{data[2]:<10}{data[3]:<25}{data[4]:<25}{data[5]:<25}{data[6]:<10}")
            except FileNotFoundError:
                print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice")