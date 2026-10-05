def view_available_classes():
    while True:
        print(f"""
              {"=" * 40}
              View Available Classes
              
              1. view available class
              2. back
              """)
        choice = input("Enter Choice: ")
        if choice == "1":        
            try:
                with open("txt/Class.txt", "r") as file:
                    lines = file.readlines()
                    if len(lines) == 0:
                        print("No data in the file")
                        continue
                    else:
                        print(f"{'Class ID':<10}{'Class Name':<32}{'Secheule':<20}{'Lecturer':<22}{"Capacity"}")
                        for line in lines:
                            data = line.strip().split(",")
                            if len(data) < 5:
                                print(f"Incomplete data: {data}")
                            else:
                                print(f"{data[0]:<10}{data[1]:<32}{data[2]:<20}{data[3]:<22}{data[4]}")
            except FileNotFoundError:
                print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice!")

if __name__ == "__main__":
    view_available_classes()
