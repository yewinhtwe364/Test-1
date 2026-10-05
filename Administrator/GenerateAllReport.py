def Generate_All_Report():
    
    while True:
        print(f"""
          {"=" * 40}
           Generate All Report
          
          1. generate all report
          2. back to Adminstrator Menu
          {"=" * 40}
          """)
        choice = input("Enter Choice: ")
        if choice == "1":
            try:
                with open("txt/Class.txt", "r") as file:
                    totalclass = sum(1 for line in file)
            except FileNotFoundError:
                print("File is not found!")
                totalclass = 0
                
            try:
                with open("txt/Member.txt", "r") as file:
                    totalmember = sum(1 for line in file)
            except FileNotFoundError:
                print("File is not found!")
                totalmember = 0
            
            try:
                with open("txt/Booking.txt" , "r") as file:
                    totalbooking = sum(1 for line in file)
            except FileNotFoundError:
                print("File is not found!")
                totalbooking = 0
            
            totalpayment = 0
            try:
                with open("txt/Payment.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        totalpayment += float(data[3])
            except FileNotFoundError:
                print("File is not found!")
                totalpayment = 0
            
            popular_class = "N/A"
            count = {}
            highestcount = 0
            className = "N/A"

            try:
                with open("txt/Booking.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        if len(data) == 7:
                            classID = data[2]
                            if classID in count:
                                count[classID] += 1
                            else:
                                count[classID] = 1
                    for classID, booking_count in count.items():
                        if booking_count > highestcount:
                            highestcount = booking_count
                            popular_class = classID
            except FileNotFoundError:
                print("file is not found!")          
                className = "N/A"
            
            try:
                with open("txt/Class.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(',')
                        if data[0] == popular_class:
                            className = data[1]
                            break
            except FileNotFoundError:
                print("File is not found!")
            print(f"""
              {"=" * 40}
              Over All Report
              Total Classs : {totalclass}
              Total Member : {totalmember}
              Total Booking : {totalbooking}
              Total Payment : {totalpayment}
              Popular Class : {className}
              {"=" * 40}
              """)
            
        elif choice == "2":
            return
        else:
            print("Wrong Choice")
            
