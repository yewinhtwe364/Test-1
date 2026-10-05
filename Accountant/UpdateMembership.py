def update_membershipplan():
    while True:
        print(f"""
              {"=" * 40}
              Update Membership Plan
              
              1. update membership plan
              2. back
              """)
        choice = input("Enter Choice: ")
        if choice == "1":
            planid = input("Enter Membership Plan ID: ")
            found = False
            updated = False
            record = []
            try:
                with open("txt/Membershipplan.txt" , "r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        if data[0] == planid:
                            found = True
                            print(f"""
                                  Current Membership Plan info!
                                  PlanID = {data[0]}
                                  Plan Name = {data[1]}
                                  Annual Fee = {data[2]}
                                  """)
                            print(f"""
                                  Which one do you want to update?
                                  
                                  1. Plan Name
                                  2. Annual Fee
                                  3. Quit
                                  """)
                            while True:
                                choice = input("Enter Choice: ")
                                if choice == "1":
                                    new_plan_name = input("Enter New Plan Name: ")
                                    data[1] = new_plan_name
                                elif choice == "2":
                                    new_annual_fee = input("Enter New Annual Fee: ")
                                    data[2] = new_annual_fee
                                    updated = True
                                elif choice == "3":
                                    break
                                else:
                                    print("Wrong Choice!")
                        record.append(",".join(data) + "\n")
            except FileNotFoundError:
                print("File is not found!")
                continue
            if found:
                if updated:
                    try:
                        with open("txt/Membershipplan.txt", "w") as file:
                            file.writelines(record)
                            print("Membership Plan is  updated! successfully")
                    except FileNotFoundError:
                        print("File is not found!")
                else:
                    print("No changes were made")
            else:
                print("Invalid Plan ID")
        elif choice == "2":
            return
        else:
            print("Wrong choice!")                            
                                
                    