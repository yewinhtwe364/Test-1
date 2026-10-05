from Maintenance import Function as F
def add_new_equipment():
    while True:
        print(f"""
              {"=" * 40}
              Add New Equipment
              
              1. add new equipment
              2. back
              """)
        choice = input("Enter Choice: ")
        if choice == "1":
            equipmentID = F.generate_equipmentID()
            name = input("Enter Equipment Name: ").strip()
            location = input("Enter Location: ").strip()
            while True:
                status = input("Enter Status(Repair/Service): ").strip().lower()
                if status == "repair" or status == "service":
                    status = status.capitalize()
                    break
                else:
                    print("Wrong choice:")
            try:
                with open("txt/Equipment.txt", "a") as file:
                    file.write(f"{equipmentID},{name},{location},{status}\n")
                    print("New Equipment is added successfully!")
            except FileNotFoundError:
                print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong choice")
        
                               
                    