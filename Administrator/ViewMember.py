def View_Member():
    
    while True:
        print(f"""
          {"=" * 40}
          View Member
            
          1. View Member
          2. Back to administrator Menu
          {"=" * 40}
          """)
        choice = input("Enter Choice: ")
        if choice == "1":
          try:
              with open("txt/Member.txt", "r") as file:
                lines = file.readlines()
                if len(lines) == 0:
                  print("No data in the file")
                  continue
                print(f"{"MemberID":<10}{"Name":<25}{"Phone Number":<15}{"Email":<30}")
                for line in lines:
                  data = line.strip().split(",")
                  if len(data) < 4:
                    print(f"Incomplete Data: {data}")
                  else:
                    print(f"{data[0]:<10}{data[1]:<25}{data[2]:<15}{data[3]:<30}")
          except FileNotFoundError:
            print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice: ")    
            