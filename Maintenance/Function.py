def generate_equipmentID():
    try:
        with open("txt/Equipment.txt", "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                return "E001"
            for line in reversed(lines):
                data = line.strip().split(",")
                if data[0].startswith("E"):
                    number = int(data[0][1:]) + 1
                    return "E" + str(number).zfill(3)
            return "E001"
    except FileNotFoundError:
        return "E001"
    
def check_equipmentID(equipmentID):
    try:
        with open("txt/Equipment.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == equipmentID:
                    return True
            return False
    except FileNotFoundError:
        return False
    
def get_equipment(equipmentID):
    try:
        with open("txt/Equipment.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == equipmentID:
                    return data
            return None
    except FileNotFoundError:
        return None

def generate_maintenance_recordID():
    try:
        with open("txt/MaintenanceRecord.txt", "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                return "MR001"
            for line in reversed(lines):
                data = line.strip().split(",")
                if data[0].startswith("MR"):
                    number = int(data[0][2:]) + 1
                    return "MR" + str(number).zfill(3)
            return "MR001"
    except FileNotFoundError:
        return "MR001"
        
def check_date(Date):
    data = Date.strip().split("-")
    try:
        if len(data) == 3 and len(data[0]) == 4 and 0< int(data[1]) <= 12 and 0 < int(data[2]) <= 31:
            return True
        else:
            return False
    except ValueError:
        return False
