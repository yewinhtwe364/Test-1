from Administrator import Function as F
def Add_New_Class():
    
    while True:
        print(f"""
        {"=" * 40}
        ADD NEW CLASS
        
        1. Add New Class
        2. Back to Administrator Menu
        {"=" * 40}
          """)
        choice = input("Enter Choice: ")
        if choice == "1":
            classID = F.generate_classID()
            class_name = input("Enter Class Name: ")
            day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            while True:
                class_schedule = input("Enter Class Schedule:(eg. Monday-10:00 AM) ")
                inx = class_schedule.strip().split("-")
                if len(inx) != 2:
                    print("Invalid Schedule Format")
                elif inx[0] not in day:
                    print("Invalid Day")
                else:
                    break
            while True:
                lecturer = input("Enter Lecturer Name: ")
                if lecturer.replace(" ","").isalpha():
                    break
                else:
                    print("Invalid Lecturer Name: Please enter letters only!")
            
            try:
                while True:
                    class_capacity = int(input("Enter Class Capacity: "))
                    if class_capacity > 0:
                        break
                    else:
                        print("Capacity must be positive!:")
            except ValueError:
                print("Invalid input. Class capacity must be a positive integer.")
            try: 
                with open("txt/Class.txt", "a") as file:
                    file.write(f"{classID},{class_name},{class_schedule},{lecturer},{class_capacity}\n")
                    print("New class added successfully!\n")
                    print("Class ID= ", classID)
            except FileNotFoundError:
                print("file is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice, Try again")