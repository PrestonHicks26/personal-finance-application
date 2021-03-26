from os import path

class Finance:
    def __init__(self):
        self.program_state = ""
        self.lastSave = ""  # update when
        self.recentSaves = []  # when written to program_state file, add - to beginning of each item in list

        self.recurringIncomeDict = {}
        self.recurringExpenseDict = {}

        self.budgetCategoryDict = {}  # budget categories and their budgets
        self.budgetDict = {"default": {}}  # type of budget and each category's percentage

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

    def addRecurringIncome(self):
        pass

    def removeRecurringIncome(self):
        pass


    def singularExpense(self):
        pass

    def addRecurringExpense(self):
        pass

    def removeRecurringExpense(self):
        pass

    #ie. divide income into different categories
    def setBudget(self):
        pass

    def addBudgetCategory(self):
        pass

    def removeBudgetCategory(self):
        pass


    #ie. gift card, bank account, paper money, ect.
    #find better method name
    def addMoneyType(self):
        #adds item to dict consisting of type and amount of that type
        #ex. gift cards
        pass

    def addMoneySubType(self):
        # adds an instance of a money type, creating a subdictionary
        #ex. visa gift card exp. 6/24
        #ex.self.moneyTypeDict["Gift Cards"] = {vida gift card: 100}
        pass

    def addGoal(self):
        #can call setBudget and addBudgetCategory methods
        pass

    def removeGoal(self):
        pass

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


    def saveAs(self, address, fileName):
        save = open("{}/{}".format(address, fileName))
        save.close()
        #when saving dictionary use - to indicate level
        #ex.
        #-trial1
        #--distance
        #--speed
        #trial2



    def loadSave(self):
        pass


    @staticmethod
    def checkDate(self):
        pass