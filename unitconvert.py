import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def err(type):
    # Determine what error message to print:
    # opt = invalid option
    # num = string can't be converted to float
    if type == "opt":
        print('That is not a valid option. Exiting.')
        exit()
    elif type == "num":
        print('The length must be a number. Exiting.')
        exit()
    else:
        exit()

def isNumber(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def printOut(value, unit):
    print(str(value) + " " + unit)
    exit()

while True:
    # Define valid units and possible inputs
    validUnits = ['cm', 'centimeter', 'centimeters', 'm', 'meter', 'meters', 'in', 'inch', 'inches', 'ft', 'foot', 'feet']
    centimeters = ['cm', 'centimeter', 'centimeters']
    meters = ['m', 'meter', 'meters']
    inches = ['in', 'inch', 'inches']
    feet = ['ft', 'foot', 'feet']

    # Request conversion
    mode = input('Enter starting unit (cm, m, in, ft): ')
    if mode in validUnits:
        print("")
    else:
        err('opt')

    length = input('Enter the length you wish to convert: ')
    isNumber = isNumber(length)
    if isNumber:
        print("")
    else:
        err('num')

    outUnit = input('Enter your target unit (cm, m, in, ft): ')
    if mode in validUnits:
        print("")
    else:
        err('opt')

    # Convert all to cm
    if mode in meters:
        inputCm = float(length) * 100
    elif mode in inches:
        inputCm = float(length) * 2.54
    elif mode in centimeters:
        inputCm = float(length)
    elif mode in feet:
        inputCm = float(length) * 30.48
    else:
        err(opt)
    # Convert the desired unit
    if outUnit in meters:
        output = inputCm / 100
        printOut(output, "m")
    elif outUnit in centimeters:
        output = inputCm
        printOut(output, "cm")
    elif outUnit in inches:
        output = inputCm / 2.54
        printOut(output, "in")
    elif outUnit in feet:
        output = inputCm / 30.48
        printOut(output, "ft")
    else:
        err('opt')


































