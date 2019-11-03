def addRoll(self):
    def brandChoice():

        while True:
            tempBrandChoice = (input("\nPlease input the name of the Brand you would like to add a roll to.\n"))

            brandValidation = Rolls.RollData.get(tempBrandChoice)

            if brandValidation is None:
                print("Invalid input, please input the name of the brand you want to select")
            else:
                break
        return tempBrandChoice

    def ISOWrite():
        ISORange = int(input("How many ISO's is the roll available in? (input an integer number)"))
        ISOValues = []
        for i in range(ISORange):
            ISO = input("Please write the ISO values of the roll, in increasing order")
            ISOValues.append(int(ISO))
        return ISOValues

    def typeWrite():

        while True:

            rollType = input("""
    Is the film Color?
    input:  """)
            rollType = Rolls.checkAgreement(rollType)

            if rollType.isnumeric() and int(rollType) == 0:
                is_Color = False
                break
            elif rollType.isnumeric() and int(rollType) == 1:
                is_Color = True
                break
            else:
                print("Invalid input! please refer to instructions above to select film type")
        return is_Color

    def usageWrite():
        usageValues = []
        while True:
            usage = input("""
    Please write applications for this film, for example:
    Portraits
    Street
    Landscape
    General
    Studio

    Afterwards input 0 to end this process

    input:  """)
            if usage.isnumeric() and int(usage) == 0:
                break
            else:
                usageValues.append(usage)

        return usageValues

    def highEndWrite():

        while True:
            highEndArgument = input("Does one roll of the film cost more than 7 USD?")

            highEndArgument = Rolls.checkAgreement(highEndArgument)

            if highEndArgument.isnumeric() and int(highEndArgument) == 1:
                is_HighEnd = True
                break
            elif highEndArgument.isnumeric() and int(highEndArgument) == 0:
                is_HighEnd = False
                break
            else:
                print("Invalid input, please refer to the instructions above")
        return is_HighEnd

    def productionWrite():

        while True:
            productionMode = input("Is this roll currently in production?")

            productionMode = Rolls.checkAgreement(productionMode)

            if productionMode.isnumeric() and int(productionMode) == 1:
                is_inProduction = True
                break
            elif productionMode.isnumeric() and int(productionMode) == 0:
                is_inProduction = False
                break
            else:
                print("Invalid input, please refer to the instructions above")
        return is_inProduction

    def negOrPos():
        while True:
            negorposArg = input("""is the roll negative?(write No if it's Slide)
    input:""")
            negorposArg = Rolls.checkAgreement(negorposArg)

            if negorposArg.isnumeric() and int(negorposArg) == 1:
                return "Negative"
            elif negorposArg.isnumeric() and int(negorposArg) == 0:
                return "Slide"
            else:
                print("Invalid input, please refer to the instructions above")

    print("""
    Hello! You are now in Admin mode.
    Here you can add new rolls of film that you found are missing from the database.
    Below are the list of Brands that already exist in the database. \n""")

    print(("   \n").join(Rolls.RollData.keys()))

    brandChoice = brandChoice()

    print("Here are the models that already exist for the selected brand:\n", )
    Rolls.modelsInBrand(brandChoice, Rolls.RollData)
    modelName = input("What is the name of the roll you'd like to add")

    ISOValues = ISOWrite()

    Color = typeWrite()

    usage = usageWrite()

    highend = highEndWrite()

    type = negOrPos()

    production = productionWrite()



    RollCreator(brandChoice,modelName,ISOValues,type,usage,highend,Color, production)

    Rolls.RollData[Rolls.BrandtoAddto].append(Rolls.PackedData)

    print ("Roll Added sucessfully!!\n \n")


def findRoll(self):
    print("""Hello! You are now in User Mode!

    This program will help you choose a roll of film based on:

    -Your budget.
    -The time of day during which you are going to shoot the most.
    -Choice of black and white or color.
    -developing Processes available to you.

    """)

    def getBudget():
        while True:

            userInput = input("Are you willing to pay more than 7 USD for a roll of film?")
            userInput = int(Rolls.checkAgreement(userInput))

            if userInput == 1:
                is_Highend = True
                break
            elif userInput == 0:
                is_Highend = False
                break
            else:
                print("Invalid input, please try again")

        return is_Highend

    def getTimeofDay():
        morningChoice = ("morning", "Morning")
        noonChoice = ("noon", "Noon")
        eveningChoice = ("evening", "Evening")
        nightChoice = ("night", "Night")

        while True:
            time = input("""at what time during the day are you going to shoot the most?
    Here's how to input:

    08 am to 12 pm - write morning
    12 pm to 15 pm - write noon
    15 pm to 18 pm - write evening
    after 18 pm - write night
    """)

            if time in morningChoice:
                timeofday = 1
                break
            elif time in noonChoice:
                timeofday = 2
                break
            elif time in eveningChoice:
                timeofday = 3
                break
            elif time in nightChoice:
                timeofday = 4
                break
            else:
                print("Invalid input, please try again")

        return timeofday

    def timeofDaytoISO(timeofday):

        ISOmin = 0
        ISOmax = 0

        if timeofday == 1:
            ISOmin = 0
            ISOmax = 200

        elif timeofday == 2:
            ISOmin = 200
            ISOmax = 400

        elif timeofday == 3:
            ISOmin = 400
            ISOmax = 800

        elif timeofday == 4:
            ISOmin = 800
            ISOmax = 6400

        ISO = range(ISOmin, ISOmax + 1)
        return ISO

    def getColor():
        while True:
            userInput = input("Do you want color film?")
            userInput = int(Rolls.checkAgreement(userInput))

            if userInput == 1:
                is_Color = True
                break
            elif userInput == 0:
                is_Color = False
                break
            else:
                print("Invalid input, please try again")
        return is_Color

    def getType():

        while True:
            userInput = input("Do you want negative film?")
            userInput = int(Rolls.checkAgreement(userInput))

            if userInput == 1:
                type = ["Negative"]
                break
            elif userInput == 0:
                type = ["Slide"]
                break
            else:
                print("Invalid input, please try again")
        return type

    def findRolls(RollData, ISO, Budget, Color, Type):

        brands = []
        ISOfilter = []
        BudgetFilter = []
        colorFilter = []
        processFilter = []

        for i in RollData:
            brands.append(i)

        for i in brands:
            for c in RollData[i]:
                for z in c["ISO"]:
                    if z in ISO:
                        ISOfilter.append(c["model"])

        for i in brands:
            for c in RollData[i]:
                if c["is_HighEnd"] == Budget:
                    BudgetFilter.append(c["model"])

        for i in brands:
            for c in RollData[i]:
                if c["is_Color"] == Color:
                    colorFilter.append(c["model"])

        for i in brands:
            for c in RollData[i]:
                if c["type"] in Type:
                    processFilter.append(c["model"])

        ISOfilter = set(ISOfilter)
        BudgetFilter = set(BudgetFilter)
        colorFilter = set(colorFilter)
        processFilter = set(processFilter)

        Filtered1 = ISOfilter.intersection(BudgetFilter)
        Filtered2 = colorFilter.intersection(processFilter)

        TotalFilter = Filtered1.intersection(Filtered2)

        return (TotalFilter)

    is_Highend = getBudget()
    is_Color = getColor()
    timeofday = getTimeofDay()
    ISO = timeofDaytoISO(timeofday)
    Type = getType()

    FoundRolls = findRolls(Rolls.RollData, ISO, is_Highend, is_Color, Type)

    print("Here are some rolls you can get for your next shoot!\n")

    for i in FoundRolls:
        print(i)

    print("\nHave fun!!!!")




def modelsInBrand(Brand, RollData):
    for key in RollData[Brand]:
        print(key['model'])

def ChooseMode(self):
    while True:
        modeChoice = input("""
Please choose operation mode\n
1- for Admin mode (to add new rolls to the database)\n
2- for User mode

input:  """)

        if modeChoice.isnumeric() and int(modeChoice) == 1:
            while True:
                modeContinue = input("Would you like to add a roll?")

                modeContinue = int(Rolls.checkAgreement(modeContinue))

                if modeContinue == 1:

                    Rolls.AddRoll(Rolls)

                    pass

                elif modeContinue == 0:
                    print("successfully ended admin mode. Bye Bye!")
                    exit()

                else:

                    print("Invalid input, please try again")
        elif modeChoice.isnumeric() and int(modeChoice) == 2:

            Rolls.FindRoll(Rolls)

            break
        else:
            print("invalid choice, please follow the instructions for choosing mode of operation")

def checkAgreement(self, argument):
    yesWords = ("Yes", "yes", "YES", "YeS", "yEs", "yus", "Yus", "Yup", "yup", "mhm")

    noWords = ("No", "no", "nO", "nope", "nein", "nou", "neh", "nah", "Nein", "Nou", "Neh", "Nah")

    while True:
        if argument in yesWords:
            output = "1"
            break
        elif argument in noWords:
            output = "0"
            break
        else:
            output = "2"
            break
    return output
