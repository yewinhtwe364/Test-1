def generate_paymentID():
    try:
        with open("txt/Payment.txt", "r") as file:
            lines = file.readlines()
        if len(lines) == 0:
            return "P001"
        for line in reversed(lines):
            data = line.strip().split(",")
            if data[0].startswith("P"):
                number = int(data[0][1:]) + 1
                return "P" + str(number).zfill(3)
        return "P001"
    except FileNotFoundError:
        return "P001"
    
# check Member
def check_member(memberID):
    try:
        with open("txt/Member.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    if data[0] == memberID:
                        return True
    except FileNotFoundError:
        return False
    return False

def generate_membershipID():
    try:
        with open("txt/Membership.txt", "r") as file:
            lines = file.readlines()
        if len(lines) == 0:
            return "MS001"
        for line in reversed(lines):
            data = line.strip().split(",")
            if data[0].startswith("MS"):
                number = int(data[0][2:]) + 1
                return "MS" + str(number).zfill(3)
        return "MS001"
    except FileNotFoundError:
        return "MS001"
# expiry date
def expiry_date(Date):
    data = Date.strip().split("-")
    year = int(data[0]) + 1
    month = data[1]
    day = data[2]
    return str(year) +"-"+ month +"-"+ day

# Annual fee amount
def fee_amount(planID):
    try:
        with open("txt/Membershipplan.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == planID:
                    amount = data[2]
                    return amount
            return None
    except FileNotFoundError:
        return None
        
#check booking ID
def check_booking(bookingID):
    try:
        with open("txt/Booking.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == bookingID:
                    return True
            return False
    except FileNotFoundError:
        return False
    
def get_month(month):
    month_names = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    return month_names[int(month) - 1]

#check membershipplan
def check_membershipplan(planID):
    try:
        with open("txt/Membershipplan.txt","r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == planID:
                    return True
            return False
    except FileNotFoundError:
        return False

