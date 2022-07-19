plate = input("Plate: ")


def main():
    if is_valid(input):
        if is_valid_ii():
            if is_valid_iii():
                if is_valid_iv():
                    get_start()
                    print("Valid")
                    return
    print("Invalid")


def is_valid(s):
    s = len(plate)
    if s >= 2 and s <= 6:
        return True


def is_valid_ii():
    for i in plate:
        n = plate[0:2]
    if n.isalpha:
        return True


def is_valid_iii():
    for i in range(len(plate)):
        o = plate[i]
        if o == "0":
            return False
        if o.isnumeric():
            finstring = (plate[i:])
            if finstring.isnumeric():
                    return True
            return False
    return True


def get_start():
    new_str = []
    for i in plate:
        if i.isnumeric():
            new_str.append(i)
            if i.isalpha():
                new_str.append(i)

def is_valid_iv():
    if plate.isalnum():
        return True
    else:
        return False


main()
