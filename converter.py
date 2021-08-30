# Released under the GNU GPL-3.0-or-later
# Inches To Gallons Convertor v1.4
# Send bug reports to scochran2@protonmail.com

# Creates a list with the history of all results

history = []

# The while loop ensures the program keeps asking for conversions for as long as it's running.

while True:

    # This function is for use later on, to make sure the user enters a whole number.

    def inputNumber(message):
        while True:
            try:
                userInput = float(input(message))
            except ValueError:
                print("Please enter a whole number.")
                continue
            else:
                return userInput
                break

    # This function is for use later on, to make sure the user enters a correct unit.

    def inputUnits(message):
        while True:
            try:
                userInput = str(input(message))
            except ValueError:
                print("Please try again. Type g for gallons, q for quarts, or h for history.")
            else:
                return userInput
                break


    # This function handles printing based on the unit selection.

    def printResults():
        if units == "g":
            print("The barrel contains " + str(totalgallons) + " gallons")
            history.append(totalgallons)
        elif units == "q":
            print("The barrel contains " + str(totalquarts) + " quarts")
            history.append(totalquarts)
        return history

    # This part of the code asks the user which unit they want to convert to.

    units = inputUnits("Would you like to convert to (g)allons or (q)uarts, or see (h)istory?")

    # This loop makes sure the user input a valid selection.

    while units != "g" and units != "q" and units != "h":
        print("That is not a valid selection. Please type g for gallons, q for quarts, or h for history.")
        units = inputUnits("Would you like to convert to (g)allons or (q)uarts, or see (h)istory?")

    # This part asks the user how full the barrel is.

    if units == "g" or units == "q":
        inches = inputNumber("How full is the barrel, in inches?")
        while inches >= 34:
            print("55 gallon drums are only 33 inches tall. Please try again.")
            inches = inputNumber("How full is the barrel, in inches?")

        # This part does the actual calculation...

        totalgallons = 1.667 * inches

        # ...and multiplies by four in case quarts are needed.

        totalquarts = totalgallons * 4

        # Here we round the results to whole numbers

        totalgallons = round(totalgallons, 2)
        totalquarts = round(totalquarts, 2)

    elif units == "h":
        if not history:
            print("History is empty.")
        else:
            print(history)

    # The program calls a function to handle printing results

    printResults()
