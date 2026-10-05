# Register member
from BookingOfficer import Function as F
def member_registration():
    

    
    while True:
        print(f"""
          {"=" * 40}
          Member Registration
          
          1. member registration
          2. Back to Booking Officer Menu
          {"=" * 40}
          
          """)
        choice = input("Enter choice: ")
        if choice == "1":
            member_id = F.generate_member_id()
            while True:

                name = input("Enter member name: ").strip()
                if name.replace(" ","").isalpha():
                    break
                else:
                    print("Invalid Name - try again!")
            

            while True:
                phone = input("Enter phone number: ")

                if phone.startswith("+") and phone[1:].isdigit():
                    break
                else:
                    print("INVALID PHONE - TRY AGAIN")

            while True:
                email = input("Enter email: ")

                if "@" in email and "." in email:
                    
                    break
                else:
                    print("INVALID EMAIL - TRY AGAIN")

            with open("txt/Member.txt", "a") as file:
                file.write(member_id + "," + name + "," + phone + "," + email + "\n")

            print("Member registered successfully.")
            print("Member ID:", member_id)
        elif choice == "2":
            return
        else:
            print("Wrong Choice")
