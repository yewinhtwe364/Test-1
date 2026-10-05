from Accountant import Function as F
def membership():
    while True:
        print(f"""
              {"=" * 40}
              Membership Registration
              
              1. membership registration
              2. back
              """)
        choice = input("Enter Choice: ")
        if choice == "1":
            memberID = input("Enter Member ID: ").strip()
            if not F.check_member(memberID):
                print("Invalid Member ID")
            else:
                try:
                    with open("txt/Membershipplan.txt" , "r") as file:
                        print(f"\n{"Plan ID":<15}{"Plan Name":<25}{"Annual Fee":<15}")
                        for line in file:
                            data = line.strip().split(",")
                            print(f"{data[0]:<15}{data[1]:<25}{data[2]:<15}")
                except FileNotFoundError:
                    print("File is not found!")
                    continue
                
                while True:
                    planID = input("\nEnter PlanID: ").strip()
                    if not F.check_membershipplan(planID):
                        print("Invalid MembershipplanID")
                    else:
                        break
                while True:
                    
                    Date = input("Enter start date: ")
                    if not F.check_date(Date):                    
                        print("Invalid Date")
                    else:
                        break
                expiry_date = F.expiry_date(Date)
                membershipID = F.generate_membershipID()
                try:
                    with open("txt/Membership.txt", "a") as file:
                        file.write(f"{membershipID},{memberID},{planID},{Date},{expiry_date}\n")
                        print("Membership Plan registration has completed!")
                        print("membership ID = ", membershipID )
                except FileNotFoundError:
                    print("File is not found")
        elif choice == "2":
            return
        else:
            print("Wrong Choice!")
                    
                        
                        