from Member import Function as F
def request_booking(memberID):
    while True:
        print(f"""
            {"=" * 40}
            Request Booking
            
            1. request booking
            2. back
            """)
        choice = input("Enter Choice: ")
        if choice == "1":
            classID = input("Enter Class ID to book: ").strip()
            if not F.check_classID(classID):
                print("Invalid Class ID")
                return
            class_data = F.get_class(classID)
            if class_data is None:
                print("No Data")
                return       
            classID = class_data[0]
            className = class_data[1]
            classTime = class_data[2]
            Lecturer = class_data[3]
            while True:
                dates = input("Enter Request date: ")
                date = dates.strip().split("-")
                if len(date) != 3:
                    print("Invalid Date")
                    continue
                try:
                    year = int(date[0])
                    month = int(date[1])
                    day = int(date[2])
                    if len(date[0]) != 4 or not (1 <= month <= 12) or not (1 <= day <= 31):
                        print("Invalid Date")
                    else:
                        break
                except ValueError:
                    print("Invalid Date")               
            requestID = F.generate_requestID()
            try:
                with open("txt/Request.txt", "a") as file:
                    file.write(f"{requestID},{memberID},{classID},{className},{classTime},{Lecturer},{dates}\n")
                    print("Booking request is successfully completed!")              
            except FileNotFoundError:
                print("File is not found!")
        elif choice == "2":
            return
        else:
            print("Wrong Choice: ")
