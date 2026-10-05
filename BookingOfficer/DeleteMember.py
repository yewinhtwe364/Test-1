# Delete member
from BookingOfficer import Function as F

def delete_member():
    while True:
        print(f"""
          {"=" * 40}
          Delete Member
          
          
          1. delete member
          2. Back to Booking Officer Menu
          {"=" * 40}
          """)
        choice = input("Enter Choice: ")
        if choice == "1":
            member_id = input("Enter member ID: ").strip()
            if not F.check_member(member_id):
                print("Invalid Member ID")
                return
            try:
                with open("txt/Member.txt", "r") as file:
                    lines = file.readlines()

                with open("txt/Member.txt", "w") as file:
                    for line in lines:
                        data = line.strip().split(",")
                        if data[0] == member_id:
                            continue
                        file.write(line)
                    print(f"MemberID {member_id} has been deleted")
            except FileNotFoundError:
                print("Member file not found.")
        elif choice == "2":
            return
        else:
            print("Wrong Choice")