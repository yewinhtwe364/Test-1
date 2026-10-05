def generate_classID():
    try:
        with open("txt/Class.txt", "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                return "C001"
            for line in reversed(lines):
                data = line.strip().split(",")
                if data[0].startswith("C"):
                    number = int(data[0][1:]) + 1
                    return "C" + str(number).zfill(3)
            return "C001"
    except FileNotFoundError:
        return "C001"
    
def check_classID(classID):
    try:
        with open("txt/Class.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == classID:
                    return True
            return False
    except FileNotFoundError:
        return False

def get_class(class_ID):
    try:
        with open("txt/Class.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == class_ID:
                    return data
            return None
    except FileNotFoundError:
        return None