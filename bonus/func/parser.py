def parse(length):
    length = length.split("'")
    feet, inches = float(length[0]), float(length[1])
    return feet, inches
