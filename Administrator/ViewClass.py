def View_Class():
    
    while True:
        print(f"""
            {"=" * 40}
            View Class
          
          1. View Class
          2. Back to Administrator main menu
          {"=" * 40}
          """)
        choice = input("Enter Choice: ")
        if choice == "1":
            try:
                with open("txt/Class.txt", "r") as file:
                    lines = file.readlines()
                    if len(lines) == 0:
                        print("No Data in the file")
                        continue
                    print(f"{"ClassID":<15}{"Class Name":<35}{"Class Schedule":<20}{"Lecturer":<25}{"Class Capacity":<15}")
                    for line in lines:
                        data = line.strip().split(",")
                        if len(data) < 5:
                            print(f"Incomplete Data: {data}")
                        else:
                            print(f"{data[0]:<15}{data[1]:<35}{data[2]:<20}{data[3]:<25}{data[4]:<15}")
            except FileNotFoundError:
                print("file is not found")    
        elif choice == "2":
            return
        else:
            print("Wrong Choice")