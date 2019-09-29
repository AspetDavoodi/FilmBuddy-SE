import json as js

# Brand, Name, ISO, type, usage, is_highend, is_color, is_inProduction

class Rolls:

    RollData = {}

    PackedData = {}

    BrandtoAddto = ""

    def __init__(self):
        Rolls.getRollData()
        Rolls.ChooseMode()

    def AddRoll(self):
        pass

    def FindRoll(self):
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


    @classmethod

    def getRollData(cls):
        with open('RollData.json', 'r') as rolldata:
          Rolls.RollData = js.load(rolldata)

    @staticmethod

    def modelsInBrand(Brand, RollData):
        for key in RollData[Brand]:
            print(key['model'])

    def ChooseMode():
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

                        Rolls.AddRoll()

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

    def checkAgreement(argument):
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


class RollCreator(Rolls):

    def __init__(self, Brand, Name, ISO, type, usage, is_highend, is_color, is_inProduction):
        self.Brand = Brand
        self.Name = Name
        self.ISO = ISO
        self.type = type
        self.usage = usage
        self.is_highend = is_highend
        self.is_color = is_color
        self.is_inProduction = is_inProduction

        self.PackedData = {
            "model": self.Name,
            "ISO": self.ISO,
            "type": self.type,
            "Usage": self.usage,
            "is_HighEnd": self.is_highend,
            "is_Color": self.is_color,
            "is_inProduction": self.is_inProduction
        }

        self.BrandtoAddto = self.Brand
        super.PackedData = self.PackedData
        super.BrandtoAddto = self.BrandtoAddto



A = Rolls()

