# Generate Request ID
def generate_requestID():
    try:
        with open("txt/Request.txt" , "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                return "R001"
            for line in reversed(lines):
                data = line.strip().split(",")
                if data[0].startswith("R"):
                    number = int(data[0][1:]) + 1
                    return "R" + str(number).zfill(3)
            return "R001"
    except FileNotFoundError:
        return "R001"
    
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
    
        