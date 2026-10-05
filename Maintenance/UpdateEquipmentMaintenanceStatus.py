from Maintenance import Function as F
def update_equipment_maintenance_status():
    while True:
        print(f"""
              {"=" * 40}
              Update Equipment Maintenance status
              
              1. update equipment maintenance status
              2. back
              """)
        choice = input("Enter Choice: ")
        if choice == "1":
            equipmentID = input("Enter EquipmentID: ").strip()
            if not F.check_equipmentID(equipmentID):
                print("Invalid EquipmentID")
                return
            else:
                record = []
                
                try:
                    with open("txt/Equipment.txt", "r") as file:
                        for line in file:
                            data = line.strip().split(",")
                            if data[0] == equipmentID:
                                info = F.get_equipment(equipmentID)
                                if info != None:
                                    print(f"""
                                            Current Equipment info!
                                            EquipmentID = {info[0]}
                                            Name = {info[1]}
                                            Location = {info[2]}
                                            Status = {info[3]}
                                                            
                                            """)
                                    print("""
                                            Status
                                                              
                                            1. Repair
                                            2. Service
                                            """)
                                    while True:
                                        choice = input("Enter Status: ")
                                
                                        if choice == "1":
                                            data[3] = "Repair"
                                            break
                                        elif choice == "2":
                                            data[3] = "Service"
                                            break
                                        else:
                                            print("Wrong Choice, Try Again!")
                                else:
                                    print("Equipment Not found!")
                            record.append(",".join(data) + "\n")
                except FileNotFoundError:
                    print("file is not found!")
                try:
                    with open("txt/Equipment.txt", "w") as file:
                            file.writelines(record)
                            print("Equipment is updated successfully!")
                            
                except FileNotFoundError:
                    print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice")
                                
                                
                    