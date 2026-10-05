# Update member
from BookingOfficer import Function as F
def update_member():

    
    while True:
        print(f"""
          {"=" * 40}
          Update Member Information
          
          1. update member information
          2. back to Booking Officer menu
          {"=" * 40}
          """)
        choice = input("Enter Choice: ")
        if choice == "1":
            member_id = input("Enter MemberID: ").strip()
            if not F.check_member(member_id):
                print("Invalid Member ID")
                return
            record = []

            try:
                with open("txt/Member.txt", "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        data = line.strip().split(",")
                        if len(data) == 4 and data[0] == member_id:
                            print("\nCurrent Information")
                            print("Name:", data[1])
                            print("Phone:", data[2])
                            print("Email:", data[3])

                            while True:
                                name = input("Enter new name: ").strip()

                                if not name.replace(" ","").isalpha():
                                    print("INVALID NAME - TRY AGAIN")
                                else:
                                    break

                            while True:
                                phone = input("Enter new phone: ").strip()

                                if phone.startswith("+") and phone[1:].isdigit():
                                    break
                                else:
                                    print("INVALID PHONE - TRY AGAIN")

                            while True:
                                email = input("Enter new email: ").strip()

                                if "@" in email and "." in email:
                                    break
                                else:
                                    print("INVALID EMAIL - TRY AGAIN")

                            data[1] = name
                            data[2] = phone
                            data[3] = email
                        record.append(",".join(data)+ "\n")
                        with open("txt/Member.txt", "w") as file:
                            file.writelines(record)
                    print("Member information updated successfully!")           

            except FileNotFoundError:
                print("Member file not found.")
        elif choice == "2":
            return
        else:
            print("Wrong Choice")