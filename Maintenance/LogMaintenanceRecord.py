from Maintenance import Function as F
def log_maintenance_record():
    while True:
        print(f"""
              {"=" * 40}
              1. Log Maintenance Record
              2 back
              """)
        choice = input("Enter Choice: ")
        if choice == "1":
            maintenance_recordID = F.generate_maintenance_recordID()
            equipmentID = input("Enter EquipmentID: ").strip()
            if not F.check_equipmentID(equipmentID):
                print("Invalid EquipmentID!")
                return
            else:
                info = F.get_equipment(equipmentID)
                print("Equipment Name = ", info[1])
                maintenance_type = info[3]
                print("Maintenance Type = ", maintenance_type)
                while True:
                    date = input("Enter date: ")
                    if F.check_date(date):
                        break
                    else:
                        print("Invalid Date!")
                while True:

                    status = input("Enter Maintenance Status(Completed/Pending): ").strip() 
                    if status == "completed" or status == "pending":
                        status = status.capitalize()
                        break
                    else:
                        print("Wrong choice:")         
            try:
                with open("txt/MaintenanceRecord.txt" , "a") as file:
                    file.write(f"{maintenance_recordID},{equipmentID},{maintenance_type},{date},{status}\n")
                    print(f"Maintenance Record {maintenance_recordID} is added successfully!")
            except FileNotFoundError:
                print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong choice")
            