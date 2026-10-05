def generate_ID(x):
    with open("ID.txt","r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            return "ID001"
        for line in reversed(lines):
            data = line.strip().split(",")
            if data[0].startswith("ID"):
                number = int(data[0][2:]) + 1
                return "ID" + str(number).zfill(3)
        else:
            return ("ID001")