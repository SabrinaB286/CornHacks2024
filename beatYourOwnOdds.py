import time
#Get some infomation about the user to being with.
#What is the user's name and issue.
#Name will only be keep to use for making it feel personal.

# This function prints out the title screen to the program.
def intro():
    print("Welcome to", end="")
    for i in range (0,3):
        #time.sleep(0.3)
        print(".",end="")
    print()
    print(".-.       .                                   .   .  ") 
    print("|< .-,.-.-|-  . ..-.. ..-.  .-.. . ..-.  .-..-| .-| .-")
    print("'-'`'-`-`-'-  '-|`-''-''    `-' ` ` ' '  `-'`-'-`-'--'")
    print("              `-'                         ")         
    print("")

#Tells user what the program is about, what it can do, and how it does it.
#This user can come back to this to remind themselves of this information anytime.
def instructions():
    print("This is a program to help you work through tough decsions.")
    print("We use your answers to determine if you're making the right choice.")
    print("Note we are not therapy, we are also not responible for any choice you make. We are only here to give advice.")
    print("Right now we offer services for:")
    
def getNameAndProblem():
    print("To get ")
    return userName, userProblem

intro()
userName, userProblem = getNameAndProblem()
