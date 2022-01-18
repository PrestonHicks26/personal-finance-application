# script that runs on user login
# checks current date against deadlines for goals
# sends desktop alert to user if a deadline is coming up
# says what the goal is, what the deadline is, and how close the user is to reaching their goal
# https://python101.pythonlibrary.org/chapter44_creating_an_installer.html
import time
import zmq

execute = True

# helper functions
def isRunning():
    # checks if the main software is running to determine if information can be passed back
    pass

def checkGoalExpiration(goalType):
    pass

def checkIncomeDate():
    pass

def checkExpenseDate():
    pass

# event handlers
def sendAppNotification():
    pass

def sendEmail():
    pass

def sendDesktopNotification():
    pass

def updateBalance():
    pass

def goalExpiration():
    pass

while execute:
    checkGoalExpiration('fund')
    checkGoalExpiration('moneyType')
    checkIncomeDate()
    checkExpenseDate()

    time.sleep(60)

