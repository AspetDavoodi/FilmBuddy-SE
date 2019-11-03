import json as js

# Brand, Name, ISO, type, usage, is_highend, is_color, is_inProduction

class RollManager:

    def __init__(self):
        self.RollData = {}
        self.rolls = []

    def loadRollDataFromJSON(self):
        with open('RollData.json', 'r') as rolldata:
          self.RollData = js.load(rolldata)

        for key in self.RollData:
            for rollData in self.RollData[key]:
                roll = Roll(key, rollData["model"], rollData["ISO"], rollData["type"], rollData["Usage"], rollData["is_HighEnd"], rollData["is_Color"], rollData["is_inProduction"])
                self.rolls.append(roll)

    def toJSON(self):
        saveData = {}
        for roll in self.rolls:
            if roll.getBrand() not in saveData.keys():
                saveData[roll.getBrand()] = []

            saveData[roll.getBrand()].append(roll.toJSON())

        return saveData

    def saveJSON(self):

        SaveFile = RollManager.toJSON(self)
        with open('RollData.json', 'W') as writedata:
            js.dump(SaveFile, writedata, indent=4, separators=(',', ': '))

class Roll:

    def __init__(self, Brand, Name, ISO, type, usage, is_highend, is_color, is_inProduction):
        self.Brand = Brand
        self.Name = Name
        self.ISO = ISO
        self.type = type
        self.usage = usage
        self.is_highend = is_highend
        self.is_color = is_color
        self.is_inProduction = is_inProduction

    def getBrand(self):
        return self.Brand

    def toJSON(self):
        json = {
            "model": self.Name,
            "ISO": self.ISO,
            "type": self.type,
            "Usage": self.usage,
            "is_HighEnd": self.is_highend,
            "is_Color": self.is_color,
            "is_inProduction": self.is_inProduction
        }

        return json


def main():
    rolls = RollManager()
    rolls.loadRollDataFromJSON()

    print(rolls)
    print(rolls.toJSON())

main()

