# Get class
def get_class(class_id):

    try:
        with open("txt/Class.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) == 5 and data[0] == class_id:
                    return data

    except FileNotFoundError:
        return None

    return None

# Generate booking id
def generate_booking_id():

    try:
        with open("txt/Booking.txt", "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            return "B001"

        for line in reversed(lines):

            data = line.strip().split(",")

            if data[0].startswith("B"):

                number = int(data[0][1:]) + 1

                return "B" + str(number).zfill(3)

        return "B001"

    except FileNotFoundError:
        return "B001"
    
# Generate member id
def generate_member_id():
    try:
        with open("txt/Member.txt", "r") as file:
            lines = file.readlines()
        if len(lines) == 0:
            return "M001"
        for line in reversed(lines):
            data = line.strip().split(",")
            if len(data) == 4 and data[0].startswith("M"):
                number = int(data[0][1:]) + 1
                return "M" + str(number).zfill(3)
        return "M001"

    except FileNotFoundError:
        return "M001"

# Count class bookings
def count_class_bookings(class_id):
    count = 0

    try:
        with open("txt/Booking.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) >= 7:
                    if data[2] == class_id and data[6] == "Booked":
                        count += 1
        return count

    except FileNotFoundError:
        return 0
    

   

# Checking member
def check_member(member_id):
    try:
        with open("txt/Member.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    if data[0] == member_id:
                        return True
    except FileNotFoundError:
        return False
    return False

# Check already booked
def already_booked(member_id, class_id):

    try:
        with open("txt/Booking.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) >= 7:

                    if data[1] == member_id and data[2] == class_id:
                        if data[6] == "Booked":
                            return True

    except FileNotFoundError:
        return False

    return False

def check_bookingID(bookingID):
    try:
        with open("txt/Booking.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == bookingID:
                    return True
            return False
    except FileNotFoundError:
        return False
    
# get booking
def get_booking(bookingID):
    try:
        with open("txt/Booking.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 7 and data[0] == bookingID:
                    return data
            return None
    except FileNotFoundError:
        return None

def check_date(Date):
    data = Date.strip().split("-")
    try:
        if len(data) == 3 and len(data[0]) == 4 and 0< int(data[1]) <= 12 and 0 < int(data[2]) <= 31:
            return True
        else:
            return False
    except ValueError:
        return False
