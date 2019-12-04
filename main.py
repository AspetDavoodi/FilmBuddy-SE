import json as js

# Brand, Model, ISO, type, usage, is_highend, is_color, is_inProduction

class LL:

    def __init__(self):
        self.head = None

    def append(self,roll):
        newRoll = roll
        newRoll.set_next(self.head)
        self.head = newRoll
        #LIFO linked list append

    def searchmodels(self,ISO, Highend, Color, list):

        current = self.head

        while current is not None:
            if current.is_equal(ISO, Highend, Color):
                list.append(current.Model)
                current = current.next
            else:
                current = current.next

class RollManager:

    def __init__(self):
        self.RollData = {}
        self.MaxNumberofBrands = 100
        self.Hashtable = [LL()] * self.MaxNumberofBrands
        self.brandlist = []

    def HashFunction(self, key):
        hashedkey = 0
        for i in key:
            hashedkey = hashedkey + ord(i)
        hashedkey = hashedkey % self.MaxNumberofBrands
        return hashedkey

    def InsertBrand(self,key,value):
        hash_key = self.HashFunction(key)
        self.Hashtable[hash_key] = value

    def loadRollDataFromJSON(self):
        with open('RollData.json', 'r') as rolldata:
          self.RollData = js.load(rolldata)

        for key in self.RollData:
            self.brandlist.append(key)

            for rollData in self.RollData[key]:
                roll = Roll(key, rollData["model"], rollData["ISO"], rollData["type"], rollData["Usage"], rollData["is_HighEnd"], rollData["is_Color"], rollData["is_inProduction"])

                self.addRolltoBrand(key,roll)

    def addRolltoBrand(self,brand,roll):
        brand = self.HashFunction(brand)
        self.Hashtable[brand].append(roll)

    def deleteRoll(self,brand,model):
        brand = self.HashFunction(brand)
        TMP = self.Hashtable[brand]
        current = TMP.head
        previous = None
        found = False
        while current and found is False:
            if current.Model == model:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            print ("Error")
        if previous is None:
            current.head = current.next
        else:
            previous.next = current.next #actual deletion happens here

    def findRoll(self,ISO, Highend, Color):
        selectedRolls = []
        for brand in self.brandlist:
            tmp = []
            brand = self.HashFunction(brand)
            self.Hashtable[brand].searchmodels(ISO, Highend, Color,tmp)
            selectedRolls.extend(tmp)

        return (selectedRolls)
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


    def set_next(self,Node):
        self.next = Node

    def get_next(self):
        return self.next

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

        return

    def is_equal(self,ISO, Highend,Color):

        if ISO in self.ISO:
            if self.is_highend == Highend:
                if self.is_color == Color:
                    return True
                else:
                    return False
            else:
                return False
        else: return False

def main():
    rolls = RollManager()
    rolls.loadRollDataFromJSON()
   # rolls.deleteRoll("Kodak","52145")
   # print(rolls.findRoll(800,True,True))
    brand = rolls.HashFunction('FujiColor')
    print(rolls.Hashtable[brand].head.next.Model)

main()

