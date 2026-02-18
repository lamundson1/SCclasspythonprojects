#import date configurations
from datetime import date, timedelta


#create the budget log
budgetlog = []

def helpcommand(time_left, budget_remain):
    #print command list
    print("here is a list of commands.")
    print("'withdraw', this command allows you to list an expense and withdraw money from your budget")
    print("'showlog', this command shows the editing history of the budget.")
    print("'deposit', this command allows you to add to the budget.")
    print("'status', this command shows you the current budget")
    #call main
    main(time_left, budget_remain)


def status(time_left, budget_remain):
    #show status
    print(time_left, "days left, and $", f"{budget_remain:.2f}", "left")
    #call main
    main(time_left, budget_remain)
    
def showlog(time_left, budget_remain):
    #show log history
    for i in range(len(budgetlog)):
        print(budgetlog[i])
        i += 1
    #call main
    main(time_left, budget_remain)

def depositcommand(time_left, budget_remain):
    print("type how much you deposited and why, type '0' to cancel this process.")
    #checking for correct inputs
    while True:
        try:
            logaddamount_input = input("How much do you want to add? : $")
            logaddamount = float(logaddamount_input)
            if logaddamount < 0:
                print("Please enter a non-negative amount.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    #cancel
    if logaddamount == 0:
        main(time_left, budget_remain)
    #ask for reason
    logreason = input("why? :")
    #add to budget
    budget_remain += logaddamount
    #add to log
    today = date.today()
    logaddition = f"${logaddamount} was deposited, reason: {logreason} - {today}"
    budgetlog.append(logaddition)
    #call main
    main(time_left, budget_remain)

    
def withdrawcommand(time_left, budget_remain):
    print("type how much you spent and what you spent it on, type '0' to cancel this process.")
    #checking for correct inputs
    while True:
        try:
            logremamount_input = input("How much do you want to remove? : $")
            logremamount = float(logremamount_input)
            #cancel
            if logremamount == 0:
                main(time_left, budget_remain)
            if logremamount < 0:
                print("Please enter a non-negative amount.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    #ask for reason
    logreason = input("why? :")
    #estimate if it goes over budget
    estimate = budget_remain - logremamount
    #withdraw from budget
    budget_remain -= logremamount
    #add to log
    today = date.today()
    logaddition = f"${logremamount} was withdrawn, reason: {logreason} - {today}"
    budgetlog.append(logaddition)
    #warning if it goes over
    if estimate <= 0:
        print("Warning, you have depleted your budget")
    #call main
    main(time_left, budget_remain)

    

def main(time_left, budget_remain):
    #main function that calls other functions
    usercmnd = input("what do you want to do? :")
    if usercmnd == "helpme" :
        helpcommand(time_left, budget_remain)
    elif usercmnd == "withdraw":
        withdrawcommand(time_left, budget_remain)
    elif usercmnd == "showlog":
        showlog(time_left, budget_remain)
    elif usercmnd == "deposit":
        depositcommand(time_left, budget_remain)
    elif usercmnd == "status":
        status(time_left, budget_remain)
    else:
        print("please type the correct commands.")
        main(time_left, budget_remain)
        return usercmnd
    #the below print statement should not be executed, if it is executed then something went wrong
    print(" there is ", time_left, "days left, and $", f"{budget_remain:.2f}", " budget left.", "something went wrong")
    
   

#set todays date
todayextend = date.today()
today = todayextend.day


print("This is your personal budget tracker, all you have to do to set it up is provide the budget amount and time.")
#ensuring an acceptable time frame
acceptabletime = False
while True :
    try:
        time_set = int(input("Please provide the number of days as a frame for the budget up to 31 days, (1 - 31):  "))
        if time_set <= 31 and time_set >= 1:
            break
    except ValueError:
        print("please provide a time frame in range.")
    
    
#getting date
today = date.today()
time_deadline = today + timedelta(days=time_set)
time_left = (time_deadline - today).days

#setting initial budget
while True:
    try:
        budget_set = float(input("Please set the budget amount: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number")
budget_remain = budget_set
print(" there is ", time_left, "days left, and $", f"{budget_remain:.2f}", " budget left.")

#call methods and user input

print("if you need help, type the 'helpme' command")
main(time_set, budget_remain)
print(budget_remain)

