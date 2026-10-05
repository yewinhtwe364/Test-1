def view_booking_request():
    while True:
        print(f"""
              {"=" * 40}
              View Booking Request
              
              1. view booking request
              2. back
              """)
        choice = input("Enter Choice: ")
        if choice == "1":
            try:
                with open("txt/Request.txt", "r") as file:
                    lines = file.readlines()
                    if len(lines) == 0:
                        print("No Data in the file")
                    else:
                        print(f"{"RequestID":<10}{"MemberID":<10}{"ClassID":<10}{"Class Name":<30}{"Class Time":<20}{"Lecturer":<25}{"Date":<20}")
                                            
                    for line in lines:
                        data = line.strip().split(",")
                        if len(data) < 7:
                            print(f"Incomplete Data: {data}")
                        else:
                            print(f"{data[0]:<10}{data[1]:<10}{data[2]:<10}:{data[3]:<30}{data[4]:<20}{data[5]:<25}{data[6]:<20}")
            except FileNotFoundError:
                print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice!")
                        