from Administrator import Function as F
def Update_Class_Schedule():
    while True:
        print(f"""
            {"=" * 40}
            UPDATE CLASS SCHEDULE
        
            1. Update Class Schedule
            2. Back to Administrator Menu
            {"=" * 40}
            """)
        choice = input("Enter Choice: ")
        if choice == "1":
            classID = input("Enter Class ID to update schedule: ").strip()
            if not F.check_classID(classID):
                print("Invalid ClassID")
                return
            else:
                updated_record = []
                try:
                    with open("txt/Class.txt", "r") as file:
                        for line in file:
                            data = line.strip().split(",")
                            if classID == data[0]:
                                print("Current Schedule:", data[2])
                                new_schedule = input("Enter New Schedule: ")
                                data[2] = new_schedule
                            updated_record.append(",".join(data))
                except FileNotFoundError:
                    print("File is not Found!")
                    continue
                try:
                    with open("txt/Class.txt", "w") as file:
                        for record in updated_record:
                                file.write(record + "\n")
                                print("Schedule updated successfully!")

                except FileNotFoundError:
                        print("File is not found!")
               
        elif choice == "2":
            return
        else:
            print("Choice wrong, try again.")