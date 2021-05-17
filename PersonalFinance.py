from os import path

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
        self.program_state = ""
        self.lastSave = ""  # update when
        self.recentSaves = []  # when written to program_state file, add - to beginning of each item in list

        self.recurringIncomeDict = {} # each item is a list where 0 is
        self.recurringExpenseDict = {}

        self.budgetCategoryDict = {}  # budget categories and their balances
        self.budgetDict = {"default": {"balance": 0}, }  # type of budget and each category's percentage

        self.moneyTypeDict = {
            "Cash": 0,
            "Bank Account": 0
        }

        self.goalDict = {}

        self.date = [1, 1, 2000]

        if path.exists("program_state.txt"):
            program_state = open("program_state.txt", "r")
            for line in program_state:
                if "*lastSave:" in line:
                    self.lastSave = line[10:].rstrip()  # removes asterisk and newline
                if line[0] == "-":
                    self.recentSaves.append(line[1:].rstrip())
            program_state.close()
        else:
            # * used to avoid bug where user gives file same name as variable name,
            # since * can't be used in windows files
            program_state = open("program_state.txt", "x")
            program_state.write("*lastSave:\n")
            program_state.write("*recentSaves:\n")
            program_state.close()


        #if save file exists:
            #load most recent save file
        #else:
            #set initial values
        #self.lastSaveFile


    def singularIncome(self):
        pass

    def addRecurringIncome(self, id, moneyType, date, frequency):
        self.recurringIncomeDict[id] = Recurring_Income(moneyType, date, frequency)

    def removeRecurringIncome(self, id):
        self.recurringIncomeDict.pop(id)


    def singularExpense(self):
        pass

    def addRecurringExpense(self, id, moneyType, date, frequency):
        self.recurringExpenseDict[id] = Recurring_Income(moneyType, date, frequency)

    def removeRecurringExpense(self, id):
        self.recurringExpenseDict.pop(id)

    #ie. divide income into different categories
    def addBudgetCategory(self, id, balance):
        self.budgetCategoryDict[id] = {"balance": balance}

    def removeBudgetCategory(self, id):
        self.budgetCategoryDict.pop(id)

    def setPercentage(self, id, percentage):
        self.budgetCategoryDict[id]["percentage"] = percentage

    def addBudget(self, id, percentages):
        #percentages is a dictionary listing each budget category and a corresponding percentage
        self.budgetDict[id] = percentages

    def removeBudget(self, id):
        self.budgetDict.pop(id)

    def applyBudget(self, id):
        for category in self.budgetCategoryDict:
            self.budgetCategoryDict[category]["percentage"] = self.budgetDict[id["percentage"]]

    #ie. gift card, bank account, paper money, ect.
    #find better method name
    def addMoneyType(self, id, balance):
        #adds item to dict consisting of type and amount of that type
        #ex. gift cards
        self.moneyTypeDict[id] = {"total": balance}

    def addMoneySubType(self, parent, id, balance):
        # adds an instance of a money type, creating a subdictionary
        #ex. visa gift card exp. 6/24
        #ex.self.moneyTypeDict["Gift Cards"] = {vida gift card: 100}
        self.moneyTypeDict[parent][id] = balance
        self.moneyTypeDict[parent]["total"] += balance

    def addGoal(self, id, goal, dueDate, budget):
        #can call setBudget method
        self.goalDict[id] = {"goal": goal, "dueDate": dueDate, "budget": budget}

    def removeGoal(self, id):
        self.goalDict.pop(id)

    def checkProgress(self):
        pass


    def sendAlert(self, alertName):
        if alertName == "":
            pass
        if alertName == "":
            pass


    def saveProgramState(self):
        program_state = open("program_state.txt", "w")
        program_state.write("*lastSave:{}\n".format(self.lastSave))
        program_state.write("*recentSaves:\n")
        for save in self.recentSaves:
            program_state.write("-{}".format(save))
        program_state.close()

    def save(self):
        if not (self.recentSaves or self.lastSave):
            self.saveAs()

        save = open(self.lastSave)
        save.write("recurringIncomeDict\n")
        for i in self.recurringIncomeDict:
            save.write("-{}".format(i))
            save.write("--{}".format(self.recurringIncomeDict.get(i).moneyType))
            save.write("--{}".format(self.recurringIncomeDict.get(i).date))
            save.write("--{}".format(self.recurringIncomeDict.get(i).frequency))

        save.write("recurringExpenseDict\n")
        for i in self.recurringExpenseDict:
            save.write("-{}".format(i))
            save.write("--{}".format(self.recurringExpenseDict.get(i).moneyType))
            save.write("--{}".format(self.recurringExpenseDict.get(i).date))
            save.write("--{}".format(self.recurringExpenseDict.get(i).frequency))

        save.write("budgetCategoryDict\n")
        for i in self.budgetCategoryDict:
            save.write("-{}:{}".format(i, self.budgetCategoryDict.get(i)))

        save.write("budgetDict\n")
        for i in self.budgetDict:
            save.write("-{}:{}".format(i, self.budgetDict.get(i)))

        save.write("moneyTypeDict\n")
        for i in self.moneyTypeDict:
            save.write("-{}:{}".format(i, self.moneyTypeDict.get(i)))

        save.write("goalDict\n")
        for i in self.goalDict:
            save.write("-{}:{}".format(i, self.goalDict.get(i)))

        save.close()
        # when saving dictionary use - to indicate level of subdictionary
        # ex.
        # -trial1
        # --distance
        # --speed
        # trial2
        #when saving dictionary of objects use - to indicate attributes of object


    def saveAs(self, address, fileName):
        path = "{}\{}".format(address, fileName)
        save = open(path)
        self.lastSave = path
        self.recentSaves.append(path)
        self.save()



    def loadSave(self, address):
        save = open(address, "r")
        current = ""

        for line in save:
            if "recurringIncomeDict" in line:
                current = "recurringIncomeDict"
            if "recurringExpenseDict" in line:
                current = "recurringExpenseDict"
            if "budgetCategoryDict" in line:
                current = "budgetCategoryDict"
            if "budgetDict" in line:
                current = "budgetDict"
            if "moneyTypeDict" in line:
                current = "moneyTypeDict"
            if "goalDict" in line:
                current = "goalDict"
            # load recurring income

            #load recurring expense

            #load budget categories

            #load budgets

            #load money types

            #load goals
        save.close()


    @staticmethod
    def checkDate(self):
        pass