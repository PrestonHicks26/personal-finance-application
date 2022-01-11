from os import path
import json
import datetime

class Recurring_Income:
    def __init__(self, moneyType, date, frequency):
        self.moneyType = moneyType
        self.date = date  # starting date for recurring income
        self.frequency = frequency  # how often income recurs

class Recurring_Expense:
    def __init__(self, moneyType, date, frequency):
        self.moneyType = moneyType
        self.date = date
        self.frequency = frequency

class Finance:
    def __init__(self):
        self.lastSave = ''
        self.saves = []
        self.recentSaves = [] # when save is saved, remove it from list, and then append back to the end, if list gets too long, remove oldest save
        self.openSave = ''
        if path.exists("program_state.json"):
            with open("program_state.json", "r") as f:
                jsonList = json.load(f)
            self.lastSave = jsonList[0]
            self.saves = jsonList[1]
            self.recentSaves = jsonList[2]
            self.openSave = self.lastSave

        if not self.saves:
            self.recurringIncomeDict = {} # each item is a list where 0 is
            self.recurringExpenseDict = {}
            self.fundDict = {}  # funds (ie. college fund, personal spending, savings, ect.) and their balances
            self.budgetDict = {"default": {"balance": 0}, }  # type of budget and each category's percentage
            self.moneyTypeDict = {
                "Cash": 0,
                "Bank Account": 0
            }
            self.goalDict = {}
            self.forcedBudget = False
        else:
            self.loadSave()


    def singularIncome(self, value, fund, moneyType):
        self.fundDict[fund] += value
        self.moneyTypeDict[moneyType] += value

    def addRecurringIncome(self, id, moneyType, date, frequency):
        self.recurringIncomeDict[id] = Recurring_Income(moneyType, date, frequency)

    def removeRecurringIncome(self, id):
        self.recurringIncomeDict.pop(id)


    def singularExpense(self,value, fund, moneyType):
        self.fundDict[fund] -= value
        self.moneyTypeDict[moneyType] -= value

    def addRecurringExpense(self, id, moneyType, date, frequency):
        self.recurringExpenseDict[id] = Recurring_Income(moneyType, date, frequency)

    def removeRecurringExpense(self, id):
        self.recurringExpenseDict.pop(id)

    #ie. divide income into different categories
    def addFund(self, id, balance):
        self.fundDict[id] = {"balance": balance}

    def removeFund(self, id):
        self.fundDict.pop(id)

    def setPercentage(self, id, percentage):
        self.fundDict[id]["percentage"] = percentage

    def addBudget(self, id, percentages):
        #percentages is a dictionary listing each budget category and a corresponding percentage
        self.budgetDict[id] = percentages

    def removeBudget(self, id):
        self.budgetDict.pop(id)

    def applyBudget(self, id):
        if self.forcedBudget:
            print("One of your goals has you on a forced budget, are you sure you want to change it?")
            # spawn pop up box with yes and no buttons
            # temp code:
            if input() == 'y':
                for category in self.fundDict:
                    self.fundDict[category]["percentage"] = self.budgetDict[id["percentage"]]
        else:
            for category in self.fundDict:
                self.fundDict[category]["percentage"] = self.budgetDict[id["percentage"]]


    #ie. gift card, bank account, paper money, ect.
    #find better method name
    def addMoneyType(self, id, balance):
        #adds item to dict consisting of type and amount of that type
        #ex. gift cards
        self.moneyTypeDict[id] = {"total": balance}

    def addMoneySubType(self, parent, id, balance):
        # adds an instance of a money type, creating a subdictionary
        #ex. visa gift card exp. 6/24
        #ex.self.moneyTypeDict["Gift Cards"] = {visa gift card: 100}
        self.moneyTypeDict[parent][id] = balance
        self.moneyTypeDict[parent]["total"] += balance

    def addGoal(self, goal, value, dueDate, budget=None):
        #can call setBudget method
        self.goalDict[goal] = {"value": value, "dueDate": dueDate, "budget": budget}
        if budget is not None:
            self.applyBudget(budget)
            self.forcedBudget = True
        for goal in self.goalDict:
            if self.goalDict[goal]['budget'] != budget and self.goalDict[goal]['budget'] is not None:
                print("This goal's budget conflicts with another goal's budget. Which would you like to keep?")
                # open pop up window and display 'old' on one button and 'new' on the other
                # if new pressed:
                    # applyBudget(budget)

    def removeGoal(self, id):
        self.goalDict.pop(id)
        self.forcedBudget = False
        for goal in self.goalDict:
            if self.goalDict[goal]['budget'] is not None:
                self.forcedBudget = True

    def checkProgress(self):
        date = datetime.datetime.now()
        for goal in self.goalDict:
            if date.year

    def notification(self, notification):
        if notification == "":
            pass
        if notification == "":
            pass


    def saveProgramState(self):
        jsonList = [self.lastSave, self.saves, self.recentSaves]
        with open('program_state.json', 'w') as f:
            json.dump(jsonList, f)

    def save(self):
        self.lastSave = self.openSave
        if not (self.saves or self.lastSave):
            print("Address: ")
            address = input()
            print("File Name: ")
            fileName = input()
            self.saveAs(address, fileName)

        jsonDict = {'recurringIncomeDict': self.recurringIncomeDict,
                    'recurringExpenseDict': self.recurringExpenseDict,
                    'fundDict': self.fundDict,
                    'budgetDict': self.budgetDict,
                    'moneyTypeDict': self.moneyTypeDict,
                    'goalDict': self.goalDict,
                    'forcedBudget': self.forcedBudget}
        with open(self.lastSave, 'w') as f:
            json.dump(jsonDict, f)

    def saveAs(self, address, fileName):
        path = "{}\\{}.json".format(address, fileName)
        save = open(path, 'w')
        save.close()
        self.lastSave = path
        self.saves.append(path)
        self.recentSaves.remove(path)
        self.recentSaves.append(path) # makes sure most recent save is at end of list
        if len(self.recentSaves) > 3:
            self.recentSaves.pop(0)

    def loadSave(self, address): # rewrite to use .json format
        self.openSave = address
        self.recentSaves.remove(address)
        self.recentSaves.append(address)  # makes sure most recent save is at end of list
        if len(self.recentSaves) > 3:
            self.recentSaves.pop(0)
        with open(address, "r") as f:
            jsonDict = json.load()
            self.recurringIncomeDict = jsonDict['recurringIncomeDict']
            self.recurringExpenseDict = jsonDict['recurringExpenseDict']
            self.fundDict = jsonDict['fundDict']
            self.budgetDict = jsonDict['budgetDict']
            self.moneyTypeDict = jsonDict['moneyTypeDict']
            self.goalDict = jsonDict['goalDict']
            self.forcedBudget = jsonDict['forcedBudget']

    #def update(self):

    def close(self):
        self.saveProgramState()
        #if changes made w/o save, spawn confirmation box
        #terminate window


    @staticmethod
    def checkDate(self):
        pass