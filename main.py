import json as js

# Brand, Name, ISO, type, usage, is_highend, is_color, is_inProduction

class RollManager:

    def __init__(self):
        self.RollData = {}
        self.MaxNumberofBrands = 100
        self.Hashtable = [None] * self.MaxNumberofBrands
        self.head = None


    def HashFunction(self, key):
        hashedkey = 0
        for i in key:
            hashedkey = hashedkey + ord(i)
        return hashedkey


    def InsertBrand(self,key,value):
        hash_key = self.HashFunction(key)
        self.Hashtable[hash_key] = value

    def loadRollDataFromJSON(self):
        with open('RollData.json', 'r') as rolldata:
          self.RollData = js.load(rolldata)

        for key in self.RollData:

            for rollData in self.RollData[key]:
                roll = Roll(key, rollData["model"], rollData["ISO"], rollData["type"], rollData["Usage"], rollData["is_HighEnd"], rollData["is_Color"], rollData["is_inProduction"])
                if self.head is None:
                    self.head = roll
                else:
                    last = self.head
                    while last is not None:
                        last = roll.next
                    last.next = roll

                self.addRolltoBrand(key,roll)

    def addRolltoBrand(self,brand,roll):
        brand = self.HashFunction(brand)
        self.Hashtable[brand] = roll


    def deleteRoll(self,brand,model):
        pass



    def saveJSON(self):
        pass


class Roll:

    def __init__(self, Brand, Model, ISO, type, usage, is_highend, is_color, is_inProduction):
        self.Brand = Brand
        self.Model = Model
        self.ISO = ISO
        self.type = type
        self.usage = usage
        self.is_highend = is_highend
        self.is_color = is_color
        self.is_inProduction = is_inProduction

        self.next = None #Linked List implementation made more sense than tree or BST as most rolls have values that coincide



    def getBrand(self):
        return self.Brand

    def toJSON(self):
        json = {
            "model": self.Model,
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

main()

