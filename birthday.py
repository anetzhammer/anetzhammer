import random

input = int(input("Number of students: "))

def divide():
    division = checklist()
    print("Percent chance two or more birthday's are shared: ", division)


def getlist():
    randomlist = []
    for i in range(input):
        n = random.randint(1, 365)
        randomlist.append(n)
    return randomlist


def checklist():
        count = 0
        x = 0
        y = 0
        while count < 100000:
            numbers = getlist()
            duplicates = [number for number in numbers if numbers.count(number) > 1]
            unique_duplicates = (list(set(duplicates)))
            if len(unique_duplicates) >= 1:
                x = x + 1
                count = count + 1
            elif len(unique_duplicates) == 0:
                y = y + 1
                count = count + 1
        return (x/(x+y))





getlist()
checklist()
divide()