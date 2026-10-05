from Administrator import Function as F
def Remove_Class():
    
    while True:
        print("""
          ===================================
                Remove Class
          ===================================
          
          1. Remove Class
          2. Back to Adminstrative Menu
          """)
        choice = input("Enter Choice : ")
        if choice == "1":
            classID = input("Enter ClassID: ")
            if not F.check_classID(classID):
                print("Invalid ClassID")
                return
            else:
                updated_record = []
                try:
                    with open ("txt/Class.txt", "r") as file:
                        for line in file:
                            data = line.strip().split(",")
                            updated_record.append(",".join(data))
                except FileNotFoundError:
                    print("File is not found!")
                try:
                    with open("txt/Class.txt", "w") as file:
                        for record in updated_record:
                            file.write(record + "\n")
                            print(f"Class {data[1]} has successfully removed")

                except FileNotFoundError:
                    print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice")