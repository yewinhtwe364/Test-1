def view_equipment():
    while True:
        print(f"""
              {"=" * 40}
              View Equipment
              
              1. view equipment
              2. back
              """)
        choice = input("Enter Choice: ")
        if choice == "1":
            try:
                with open("txt/Equipment.txt", "r") as file:
                    lines = file.readlines()
                    if len(lines) == 0:
                        print("No Data in the file")
                        continue
                    print(f"{"EquipmentID":<15}{"Name":<30}{"Location":<30}{"Status"}")

                    for line in lines:
                        data = line.strip().split(",")
                        if len(data) < 4:
                            print(f"Incomplete Data: {data}")
                        else:
                            print(f"{data[0]:<15}{data[1]:<30}{data[2]:<30}{data[3]}")
            except FileNotFoundError:
                print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice ")
                        