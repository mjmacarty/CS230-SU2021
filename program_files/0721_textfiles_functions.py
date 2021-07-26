"""
Author:  Mark Frydenberg
Description: text file examples
"""

REGFILE = "registration.txt"

def linebyline():
    print("Line By Line")

    # print all the records in the file within range specified

    lowAge = int(input("Enter the lower age :"))
    highAge = int(input("Enter the upper age: "))

    # find all the people in the file whose ages are in the range above

    f = open(REGFILE, 'r')  # open file for read
    done = False
    while not done:
        line = f.readline()
        if line == "":  # end of file
            done = True
            continue

        record = line.split("|")
        name = record[0]
        addr = record[1]
        city = record[2]
        state = record[3]
        zip = record[4]
        age = int(record[5])

        if lowAge <= age <= highAge:
            print(f"{name:20s}\t{age:3d}")

    f.close()  # input files don't need to be closed explicitly


def filetolist():
    print("Read File to List of Strings")

    lowAge = int(input("Enter the lower age :"))
    highAge = int(input("Enter the upper age: "))

    f = open(REGFILE, 'r')  # open file for read
    ftext = f.read()  # read the entire file into a string
    print(ftext)
    f.close()

    lines = ftext.split("\n")  # split the file at new line characters

    first = True  # skip the header row in the file

    for line in lines:
        if first:
            first = False   #skip the first line
            continue
        if line == "":  # end of file
            break
        else:
            record = line.split("|")
            name = record[0]
            addr = record[1]
            city = record[2]
            state = record[3]
            zip = record[4]
            age = int(record[5])

            if lowAge <= age <= highAge:
                print(f"{name:20s}\t{age:3d}")


def modifyfile():
    print("Modify File")

    years = int(input("Enter years to add to each age: "))

    f = open(REGFILE, 'r')  # open file for read
    ftext = f.read()  # read the entire file into a string
    f.close()

    lines = ftext.split("\n")  # split the file at new line characters

    f = open(REGFILE, "w")

    for line in lines:
        if line == "":  # end of file
            break
        else:
            record = line.split("|")
            name = record[0]
            addr = record[1]
            city = record[2]
            state = record[3]
            zip = record[4]
            age = int(record[5])

            age += years

            # you could do it this way
            # newLine = name + "|" + addr + "|" + city + "|" + \
            #          state + "|" + zip + "|" + str(age) + "\n"

            # but this is a good use of the join method with a list

            listItems = [name, addr, city, state, zip, str(age)]
            newLine = "|".join(listItems) + "\n"  # create the new line to write

            f.write(newLine)
    f.close()


done = False
while not done:
    choice = input("""
    1 Read File Line By Line
    2 Read File to String
    3 Modify File
    4 Print File with Line Numbers (to be filled in by you)
    5 Write Matching Records to a New File (to be filled in by you)
    Q Quit
    Enter choice:""")

    if choice == "1":
        linebyline()
    elif choice == "2":
        filetolist()
    elif choice == "3":
        modifyfile()
    elif choice == "Q":
        print("Quit. Thank you.")
        done = True
    else:
        print("Enter a valid choice.")
