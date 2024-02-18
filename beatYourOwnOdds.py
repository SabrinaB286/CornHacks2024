import time
import random
#Made by Sabrina Benford 02/18/2024

#Lists of all different accepting spellings for all variables.
spellingOfInformation = ["Information", "information", "info", "Info", "Informations", "informations"]
spellingOfRelationships = ["Relationships","Relationship", "relationships","relationship","relation", "relations","1"]
spellingOfNo = ["No","no","n", "N", "1"]
spellingOfUnlikely = ['Unlikely', "unlikely", "not really","Not Really","Not really", "not Really", "2"]
spellingOfUnsure = ["Unsure","unsure", "possibly", "Possibly", "Don't know", "don't know", "Do Not Know", "do not know", "3"]
spellingOfMoreLikely = ["More Likely", "more Likely", "more likely", "most likely", "Most Likely", "Most likely","likely", "Likely", "4"]
spellingOfYes = ["Yes", "yes", "Sure", "sure", "absolutely", "Absolutely", "y", "Y", "5"]
spellingOfEvent = ["Events", "events", "Event", "event", "An event", "An Event", "an event", "the event", "The event", "The Event","3"]
spellingOfPurchases = ["Purchases", "purchases","2", "Purchase", "purchase", "buying", "Buying"]


# This function prints out the title screen to the program.
def intro():
    print("Welcome to...", end="")
    time.sleep(0.5)
    print()
    print(",---.          |        ,   .                   ,---.              ,---.    |    |     ")
    print("|---.,---.,---.|---     |   |,---..   .,---.    |   |. . .,---.    |   |,---|,---|,---.")
    print("|   ||---',---||        `---'|   ||   ||        |   || | ||   |    |   ||   ||   |`---.")
    print("`---'`---'`---^`---'      |  `---'`---'`        `---'`-'-'`   '    `---'`---'`---'`---'")
    time.sleep(0.5)


#Checks to see if the user wants to keep the program running.
#Return 1 for keep the program going or 0 for end the program.
def replay():
    print()
    print("Would you like to take another quiz?")
    stay = input("Please input yes or no:")
    if (stay in spellingOfYes):
        stay = 1
    else:
        stay = 0
    return stay

#This function tells the user that the program is ended.
#This will only run after at least 1 quiz has been done fully.
def exit():
    print()
    print("Thank you for using our services.")
    print("We hope we can help you solve out another problem soon!")
    print(",---.              ||              |")
    print("|  _.,---.,---.,---||---.,   .,---.|")
    print("|   ||   ||   ||   ||   ||   ||---' ")
    print("`---'`---'`---'`---'`---'`---|`---'o")
    print("                         `---'")

#If user inputs 'Ask' any time they are allowed to give user input then they will be taken here (unless in the middle of a quiz).
#User can ask about the problem options and instructions.
def Ask():
    print()
    print(",---.     |    ")
    print("|---|,---.|__/ ")
    print("|   |`---.|  \ ")
    print("`   '`---'`   `")
    print()
    print("What do you want to know more about?")
    print("You can ask about:")
    time.sleep(0.5)
    print("\033[0;35mInformation")
    time.sleep(0.5)
    print("\033[0;31mRelationships")
    time.sleep(0.5)
    print("\033[0;32mPurchases")
    time.sleep(0.5)
    print("\033[0;34mEvents",end="\033[0;0m")
    print()
    check = True
    print()
    while (check):
        the_Ask = input("Please input what you want more information about here:")
        if (the_Ask in spellingOfInformation):
            instructions()
            print("If you need any more info on anything please just retype 'Ask' again.")
            check = False
        elif (the_Ask in spellingOfRelationships):
            relationshipInfo()
            print("If you need any more info on anything please just retype 'Ask' again.")
            check = False
        elif (the_Ask in spellingOfEvent):
            eventInfo()
            print("If you need any more info on anything please just retype 'Ask' again.")
            check = False
        elif (the_Ask in spellingOfPurchases):
            purchaseInfo()
            print("If you need any more info on anything please just retype 'Ask' again.")
            check = False
        else:
            print("This is something we cannot provide information on. Please try again.")

#This function calculates the percent of all the ratings 5-1 star and shows it to user.
#ratings - The list of integers from 1-5 for the relationship quiz.
def calculateRelationshipRating(ratings,comment):
    fiveStar = 0
    fourStar = 0
    threeStar = 0
    twoStar = 0
    oneStar = 0
    total = len(ratings)
    for rate in ratings:
        if (rate == 5):
            fiveStar += 1
        elif (rate == 4):
            fourStar += 1
        elif (rate == 3):
            threeStar +=1
        elif (rate == 2):
            twoStar += 1
        elif (rate == 1):
            oneStar += 1
    print()
    print("For the Relationship quiz",int((fiveStar/total)*100),"percent of people gave it a five star rating.")
    print("For the Relationship quiz",int((fourStar/total)*100),"percent of people gave it a four star rating.")
    print("For the Relationship quiz",int((threeStar/total)*100),"percent of people gave it a three star rating.")
    print("For the Relationship quiz",int((twoStar/total)*100),"percent of people gave it a two star rating.")
    print("For the Relationship quiz",int((oneStar/total)*100),"percent of people gave it a one star rating.")
    print()
    print("Here are also some comments about the quiz from people that have taken the quiz before:")
    print()
    randomCheck = []
    for i in range (0,random.randint(2,3)):
        j = random.randint(0,len(comment)-1)
        if comment[j] not in randomCheck:
            print(comment[j])
            randomCheck.append(comment[j])

#This function calculates the percent of all the ratings 5-1 star and shows it to user.
#ratings - The list of integers from 1-5 for the purchase quiz.
def calculatePurchasesRating(ratings,comment):
    fiveStar = 0
    fourStar = 0
    threeStar = 0
    twoStar = 0
    oneStar = 0
    total = len(ratings)
    for rate in ratings:
        if (rate == 5):
            fiveStar += 1
        elif (rate == 4):
            fourStar += 1
        elif (rate == 3):
            threeStar +=1
        elif (rate == 2):
            twoStar += 1
        elif (rate == 1):
            oneStar += 1
    print()
    print("For the Purchase quiz",int((fiveStar/total)*100),"percent of people gave it a five star rating.")
    print("For the Purchase quiz",int((fourStar/total)*100),"percent of people gave it a four star rating.")
    print("For the Purchase quiz",int((threeStar/total)*100),"percent of people gave it a three star rating.")
    print("For the Purchase quiz",int((twoStar/total)*100),"percent of people gave it a two star rating.")
    print("For the Purchase quiz",int((oneStar/total)*100),"percent of people gave it a one star rating.")
    print()
    print("Here are also some comments about the quiz from people that have taken the quiz before:")
    print()
    randomCheck = []
    for i in range (0,random.randint(2,3)):
        j = random.randint(0,len(comment)-1)
        if comment[j] not in randomCheck:
            print(comment[j])
            randomCheck.append(comment[j])

#This function calculates the percent of all the ratings 5-1 star and shows it to user.
#ratings - The list of integers from 1-5 for the event quiz.
def calculateEventRating(ratings,comment):
    fiveStar = 0
    fourStar = 0
    threeStar = 0
    twoStar = 0
    oneStar = 0
    total = len(ratings)
    for rate in ratings:
        if (rate == 5):
            fiveStar += 1
        elif (rate == 4):
            fourStar += 1
        elif (rate == 3):
            threeStar +=1
        elif (rate == 2):
            twoStar += 1
        elif (rate == 1):
            oneStar += 1
    print()
    print("For the Event quiz",int((fiveStar/total)*100),"percent of people gave it a five star rating.")
    print("For the Event quiz",int((fourStar/total)*100),"percent of people gave it a four star rating.")
    print("For the Event quiz",int((threeStar/total)*100),"percent of people gave it a three star rating.")
    print("For the Event quiz",int((twoStar/total)*100),"percent of people gave it a two star rating.")
    print("For the Event quiz",int((oneStar/total)*100),"percent of people gave it a one star rating.")
    print()
    print("Here are also some comments about the quiz from people that have taken the quiz before:")
    print()
    randomCheck = []
    for i in range (0,random.randint(2,3)):
        j = random.randint(0,len(comment)-1)
        if comment[j] not in randomCheck:
            print(comment[j])
            randomCheck.append(comment[j])

#Reads in the rating file and gets the rates (5-1 stars) for the respective quiz.
def getRatings(askedForQuizRating):
    relationshipRating = []
    relationshipComments = []
    purchaseRating = []
    purchaseComments = []
    eventRating = []
    eventComments = []
    file = open("ratings.txt")
    for line in file:
        comment = -1
        typeOfQuiz, ratingNumber = [str(i) for i in line.split(' ',1)]
        if ' ' in ratingNumber:
            ratingNumber,comment = [str(i) for i in ratingNumber.split(' ',1)]
        if (typeOfQuiz == "Relationships"):
            relationshipRating.append(int(ratingNumber))
            if comment != -1:
                comment = comment.replace("\n","")
                relationshipComments.append(comment)
        if (typeOfQuiz == "Purchases"):
            purchaseRating.append(int(ratingNumber))
            if comment != -1:
                comment = comment.replace("\n","")
                purchaseComments.append(comment)
        if (typeOfQuiz == "Events"):
            eventRating.append(int(ratingNumber))
            if comment != -1:
                comment = comment.replace("\n","")
                eventComments.append(comment)
    print(relationshipComments)
    if (askedForQuizRating == "Relationships"):
        calculateRelationshipRating(relationshipRating,relationshipComments)
    if (askedForQuizRating == "Events"):
        calculateEventRating(eventRating,eventComments)
    if (askedForQuizRating == "Purchases"):
        calculateEventRating(purchaseRating,purchaseComments)

#Gets a number from user (1-5) then inputs it into the rating quiz.
def rateMyQuiz(quizName):    
    checkNumber = True
    print()
    while (checkNumber):
        rate = input("Please input a number from 1 to 5:")  
        if ((rate == "5") or (rate == "4") or (rate == "3") or (rate == "2") or (rate == "1")):
            file = open("ratings.txt", "a")
            file.write("\n"+quizName + " "+str(rate))
            checkNumber = False
        else:
            print("This is number a from 1-5. Please try again.")
    print("You may also leave a comment if you would like.")
    comment = input("Input your comment or 'No' if you want no comment.")
    if (comment not in spellingOfNo):
        file.write(" "+comment)
    file.close()

#Tells user what the program is about, what it can do, and how it does it.
#This user can come back to this to remind themselves of this information anytime.
def instructions():   
    print("|          |                   |    o               ")
    print("|,---.,---.|--- ,---..   .,---.|--- .,---.,---.,---.")
    print("||   |`---.|    |    |   ||    |    ||   ||   |`---.")
    print("``   '`---'`---'`    `---'`---'`---'``---'`   '`---'")  
    print()                     
    print("This is a program to help you work through tough decisions.")
    print("Everyone regrets something, relationships, missing out on things, money issues.")
    print("We use your answers to help you make the right decision.")
    print("Note we are not therapy, we are also not responible for any choice you make. We are only here to give advice.")
    print()
    print("Right now we offer services for:")
    time.sleep(0.5)
    print("\033[0;31mRelationships")
    time.sleep(0.5)
    print("\033[0;32mPurchases")
    time.sleep(0.5)
    print("\033[0;34mEvents")
    print()
    print("\033[0;0mIf you are unsure of what we mean by these catagories feel free to input 'Ask'.")
    print("Ask allows you to get more info about these choices or to see this page again.")

#This functions gets the name from the user.
#User can input whatever they want for their name. We want them to feel comfortable so any name is fine.
#Returns the userName
def getName():
    print(". . .|         |     |         ,   .                   ,   .               ,---.")
    print("| | ||---.,---.|--- ' ,---.    |   |,---..   .,---.    |\  |,---.,-.-.,---.  ,-'")
    print("| | ||   |,---||      `---.    `---'|   ||   ||        | \ |,---|| | ||---'  |  ")
    print("`-'-'`   '`---^`---'  `---'      |  `---'`---'`        `  `'`---^` ' '`---'  o ")
    #Checks to see if 'Ask' was input into the userName. If so they will be taken to the Ask page.
    print()
    checkAskName = True
    while (checkAskName):
        userName = input("Please enter your name here:")
        if (userName == 'Ask'):
            Ask()
            print("Now that you know more about your options let's get that name.")
        else:
            checkAskName = False
    return userName

#This function gets the problem from the user.
#If user picks 'Ask' they will be sent to the Ask function then give their problem.
#If the user does not give a valid problem the user will be promoted again until it's a valid input.
#Returns the problem
def getProblem():
    print(". . .|         |     |         ,   .                   ,---.          |    |              ,---.")
    print("| | ||---.,---.|--- ' ,---.    |   |,---..   .,---.    |---',---.,---.|---.|    ,---.,-.-.  ,-'")
    print("| | ||   |,---||      `---.    `---'|   ||   ||        |    |    |   ||   ||    |---'| | |  |  ")
    print("`-'-'`   '`---^`---'  `---'      |  `---'`---'`        `    `    `---'`---'`---'`---'` ' '  o ")
    print()
    checkProblem = True
    while (checkProblem):
        print("What seems to be your problem today?")
        print("Right now we help with these problems:")
        time.sleep(0.5)
        print("\033[0;31mRelationships (or 1)")
        time.sleep(0.5)
        print("\033[0;32mPurchases (or 2)")
        time.sleep(0.5)
        print("\033[0;34mEvents (or 3)")
        print("\033[0;0m")
        print()
        userProblem = input("Please enter in your problem that we can help with today:")
        if(userProblem == 'Ask'):
            Ask()
            print("Now that you know more about your options let's get that problem.")
        if (userProblem in spellingOfRelationships):
            userProblem = "relationships"
            print("We are happy to we are able to help with your", userProblem, "problem.")
            checkProblem = False
        if (userProblem in spellingOfEvent):
            userProblem = "events"
            print("We are happy to we are able to help with your", userProblem, "problem.")
            checkProblem = False
        if (userProblem in spellingOfPurchases):
            userProblem = "purchases"
            print("We are happy to we are able to help with your", userProblem, "problem.")
            checkProblem = False
        else:
            print("This is not an issue we currently help with here at beat your own odds.")
    return userProblem

#Since all the questions have the same answer output this is a reuseable answer input for all questions.
#Returns a number between 1-5
def answerQuestion():
    check = True
    while (check):
        print("Please answer the question with:")
        print("\033[0;31m1 (or No)")
        print("\033[0;35m2 (or Unlikely)")
        print("\033[0;33m3 (or Unsure)")
        print("\033[0;32m4 (or Likely)")
        print("\033[0;36m5 (or Yes)")
        print("\033[0;0m")
        answer = input("Please answer the question here:")
        if (answer in spellingOfNo):
            points = 1
            return points
        elif (answer in spellingOfUnlikely):
            points = 2
            return points
        elif (answer in spellingOfUnsure):
            points = 3
            return points
        elif (answer in spellingOfMoreLikely):
            points = 4
            return points
        elif (answer in spellingOfYes):
            points = 5
            return points
        else:
            print("This is not an answer we accept. Please try again.")
    return points

#Info about relationship quiz
def relationshipInfo():
    print(",---.     |         |    o               |    o         |     ,---.                    |    o          ")
    print("|---',---.|    ,---.|--- .,---.,---.,---.|---..,---.    |,---.|__. ,---.,---.,-.-.,---.|--- .,---.,---.")
    print("|  \ |---'|    ,---||    ||   ||   |`---.|   |||   |    ||   ||    |   ||    | | |,---||    ||   ||   |")
    print("`   ``---'`---'`---^`---'``---'`   '`---'`   '`|---'    ``   '`    `---'`    ` ' '`---^`---'``---'`   '")
    print("                                               |   ") 
    print("Relationships can be hard and we don't just mean romantically.")
    print("This quiz deals with everything from breaking up to the start of a relationship.")
    print("Once again note every relationship is different and not all need to take the same steps in the same situation.")
    print("These results are based on a lot of different sources.")
    print("Here is a list of our sources for our relatioship quiz:")
    print("Our teams own experience.")
    print("Friend's of the experiences.")
    print("https://www.everydayhealth.com/sexual-health/signs-youre-healthy-relationship/ (everday health)")
    print("https://www.psychologytoday.com/us/blog/the-psychology-relationships/202110/how-tell-if-relationship-is-actually-working (psychology today)")
    print("As always we aren't match makers, just people giving advise from experience.")
    print("To prove this quiz is up to your standards here some ratings from others that have taken this quiz.")
    print()
    getRatings("Relationships")


#The relationship quiz itself.
#Calls the function answerQuestion since all questions will have the same answer types.
def relationshipQuiz(userName):
    totalPoints = 0
    print(",---.     |         |    o               |    o         ,---.     o     ")
    print("|---',---.|    ,---.|--- .,---.,---.,---.|---..,---.    |   |.   ..,---,")
    print("|  \ |---'|    ,---||    ||   ||   |`---.|   |||   |    |   ||   || .-' ")
    print("`   ``---'`---'`---^`---'``---'`   '`---'`   '`|---'    `---\`---'`'---'")
    print("                                               | ")
    print("Now that we have idenfity your problem",userName,"let's begin with the quiz.")
    print("\033[0m")
    print(",---.               |    o               '|")
    print("|--- ,---..   .,---.|--- .,---.,---.      |")
    print("|    |   ||   |,---||    ||   ||   |      |")
    print("`---'`---|`---'`---^`---'``---'`   '      `")
    print("         |                                 ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mWould you loan this person money without a second thought?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.    ,--'")
    print("|    |   ||   |,---||    ||   ||   |    |   ")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |  ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mHas the person hit you or likely to hit you? (Don't lie please, this is a safe space, we won't tell anyone since this code is not program to do that.)")
    print("\033[0m")
    totalPoints -= answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.      -|")
    print("|    |   ||   |,---||    ||   ||   |       |")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |                                  ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mWould your friends(or people you know) likely say good things about the relationship? (It's okay if you don't know, just guess.)")
    print("\033[0m")
    question3 = answerQuestion()
    if (question3 == 5):
        totalPoints -= question3
    else:
        totalPoints += question3
    print(",---.               |    o              |  |")
    print("|--- ,---..   .,---.|--- .,---.,---.    `--|")
    print("|    |   ||   |,---||    ||   ||   |       |")
    print("`---'`---|`---'`---^`---'``---'`   '       `")
    print("         |           ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mDo you know eachothers love languages?(If not select 3) If so, is just something healthy, like gift giving.")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ---.")
    print("|--- ,---..   .,---.|--- .,---.,---.    `--.")
    print("|    |   ||   |,---||    ||   ||   |       |")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |                                 ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mDo you guys argue a lot?")
    print("\033[0m")
    totalPoints -= answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.    |--.")
    print("|    |   ||   |,---||    ||   ||   |    |  |")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |   ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mHave you hung out with your friends a lot less this the relatioship started?")
    print("\033[0m")
    totalPoints -= answerQuestion()
    print(",---.               |    o              ---.")
    print("|--- ,---..   .,---.|--- .,---.,---.       /")
    print("|    |   ||   |,---||    ||   ||   |      | ")
    print("`---'`---|`---'`---^`---'``---'`   '      | ")
    print("         |                            ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mIf you don't consent to being touch do they not touch you? Do you regret being touched afterwards?")
    print("\033[0m")
    totalPoints -= answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.    ,--.")
    print("|    |   ||   |,---||    ||   ||   |    |  |")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |                        ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mDo you both do your own things seperatly?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.    `__|")
    print("|    |   ||   |,---||    ||   ||   |       |")
    print("`---'`---|`---'`---^`---'``---'`   '       '")
    print("         |     ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mDo they make you feel bad?")
    print("\033[0m")
    totalPoints -= answerQuestion()
    print(",---.               |    o               '|,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.      ||  |")
    print("|    |   ||   |,---||    ||   ||   |      ||  |")
    print("`---'`---|`---'`---^`---'``---'`   '      ``--'")
    print("         |                             ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mDo you feel your relation has good communication?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print()
    #results 
    if (totalPoints < 0):
        print(userName, "this relationship seems pretty toxic. We think it's in your best interest to get out of the relationship.")
    elif (totalPoints == 0):
        print(userName, "you seem very unsure of this realtionship. We could called this relationship the possible start of a friendship.")
        print("If this is a romantic relationship it might be a good idea to end it. If it's a friendship it might just need more time to form.")
    elif (totalPoints < 5):
        print(userName, "this seems like a strong friendship or a week romantic relationship. Either way you should keep it going.")
        print("Unless things start changing this is a great person for you to be around.")
    elif (totalPoints < 8):
        print(userName, "this is a golden friendship or romantic relationship. Keep this relationship close to your heart.")
        print("If this is a friendship you are thinking about making into a romantic relationship now might be your time. But if this person is already in a romantic relationship it might just not be the one.")
    else:
        print(userName, "this is probably your bestfriend or you great pattern. This is the keeper, if you can make this into a romantic relationship, it feels right, and they aren't already dating, go for it.")
        print("This person is sure to stay your rock for years to come.")
    print("Would you like to rate this quiz?")
    check = True
    print()
    while check:
        rateCheck = input("Please input yes or no:")
        if (rateCheck in spellingOfYes):
            rateMyQuiz("Relationships")
            print("Thank you for your input!")
            print("The most ratings we get the better these quizzes will become.")
            check = False
        else:
            print("That's okay, maybe next time!")
            check = False

#Tells the user about what the event quiz provides and where we can our info from.
def eventInfo():
    print(",---.                |        |     ,---.     ")
    print("|--- .    ,,---.,---.|---     |,---.|__. ,---.")
    print("|     \  / |---'|   ||        ||   ||    |   |")
    print("`---'  `'  `---'`   '`---'    ``   '`    `---'")
    print("Everyone has different doubts on wheter they should go to an event.")
    print("From all reasoms of you don't know the bride that well or are too busy and just are unsure, we are here to help with that.")
    print("These results come from different sources.")
    print("Our sources come from common sense and the team's personal experience.")
    print("Any final choice you make is on you. We can not force you to do something nor should you take our word as final.")
    print("To prove this quiz is up to your standards here some ratings from others that have taken this quiz.")
    print()
    getRatings("Events")


def eventQuiz(userName):
    totalPoints = 0
    print(",---.                |        ,---.     o     ")
    print("|--- .    ,,---.,---.|---     |   |.   ..,---,")
    print("|     \  / |---'|   ||        |   ||   || .-' ")
    print("`---'  `'  `---'`   '`---'    `---\`---'`'---'")
    print("Now that we have idenfity your problem",userName,"let's begin with the quiz.")
    print()
    print(",---.               |    o               '|")
    print("|--- ,---..   .,---.|--- .,---.,---.      |")
    print("|    |   ||   |,---||    ||   ||   |      |")
    print("`---'`---|`---'`---^`---'``---'`   '      `")
    print("         |                                 ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mDo you have time for this event?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.    ,--'")
    print("|    |   ||   |,---||    ||   ||   |    |   ")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |  ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mWill there be people there that you like?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.      -|")
    print("|    |   ||   |,---||    ||   ||   |       |")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |                                  ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mAre you going to this event for fun?")
    print("\033[0m")
    totalPoints -= answerQuestion()
    print(",---.               |    o              |  |")
    print("|--- ,---..   .,---.|--- .,---.,---.    `--|")
    print("|    |   ||   |,---||    ||   ||   |       |")
    print("`---'`---|`---'`---^`---'``---'`   '       `")
    print("         |           ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mAre you require to go?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ---.")
    print("|--- ,---..   .,---.|--- .,---.,---.    `--.")
    print("|    |   ||   |,---||    ||   ||   |       |")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |                                 ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mDoes it cost money to go to this event?")
    print("\033[0m")
    totalPoints -= answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.    |--.")
    print("|    |   ||   |,---||    ||   ||   |    |  |")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |   ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mDo you have the money already to go to this event?(If this event does not costs money select 3.)")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ---.")
    print("|--- ,---..   .,---.|--- .,---.,---.       /")
    print("|    |   ||   |,---||    ||   ||   |      | ")
    print("`---'`---|`---'`---^`---'``---'`   '      | ")
    print("         |                            ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mAre you willing to pay to go to this event?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.    ,--.")
    print("|    |   ||   |,---||    ||   ||   |    |  |")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |                        ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mCan you fit this event into your schedule without pushing it.")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.    `__|")
    print("|    |   ||   |,---||    ||   ||   |       |")
    print("`---'`---|`---'`---^`---'``---'`   '       '")
    print("         |     ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mIs there something other than this event that would be a better use of your time?")
    print("\033[0m")
    totalPoints -= answerQuestion()
    print(",---.               |    o               '|,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.      ||  |")
    print("|    |   ||   |,---||    ||   ||   |      ||  |")
    print("`---'`---|`---'`---^`---'``---'`   '      ``--'")
    print("         |                             ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mDo you feel you'd regret going to this event?")
    print("\033[0m")
    totalPoints -= answerQuestion()
    print()
    #results 
    if (totalPoints < 3):
        print(userName,"you should not go to this at all. You do not have the time, resources, or want for this.")
        print("You will most likely regret going to this event in the event or after the event.")
    elif (totalPoints < 6):
        print(userName, "you should not go to this event.")
        print("You might find some joy in it but for the most part you will regret going to it rather than doing something else/")
    elif (totalPoints == 6):
        print(userName, "you might need to get more information about this event.")
        print("It might be best to see if someone could come with you or if you could go to this event for half the time and go do something else for the other half.")
    elif (totalPoints < 12):
        print(userName, "This seems like a good event to go to. You will most likely enjoy yourself.")
        print("If money is an issue for this event you should try to find a solution for it.")
    else:
        print(userName, "you should definetly go to this event.")
        print("You will enjoy yourself, it's worth the time and energy to go to this event.")
    print()
    print("Would you like to rate this quiz?")
    check = True
    while check:
        rateCheck = input("Please input yes or no:")
        if (rateCheck in spellingOfYes):
            rateMyQuiz("Events")
            print("Thank you for your input!")
            print("The most ratings we get the better these quizzes will become.")
            check = False
        else:
            print("That's okay, maybe next time!")
            check = False


#Info about the purchase quiz.
def purchaseInfo():
    print(",---.               |                       |     ,---.     ")
    print("|---'.   .,---.,---.|---.,---.,---.,---.    |,---.|__. ,---.")
    print("|    |   ||    |    |   |,---|`---.|---'    ||   ||    |   |")
    print("`    `---'`    `---'`   '`---^`---'`---'    ``   '`    `---'")
    print("Everyone has made a regretable purchase.")
    print("It's always a good idea to talk over a purchase before you make on you'll regret.")
    print("These results are based on a lot of different sources.")
    print("Here is a list of our sources for our relatioship quiz:")
    print("Our teams own experience.")
    print("Friend's of the experiences.")
    print("https://www.psecu.com/learn/financial-tips-for-every-stage-in-life/2020/06/05/how-to-make-good-purchasing-decisions (PSECU)")
    print("We are not finical agents and any final choice you make is on you.")
    print("To prove this quiz is up to your standards here some ratings from others that have taken this quiz.")
    print()
    getRatings("Purchases")

#Goes through the purchase quiz with the user.
def purchaseQuiz(userName):
    totalPoints = 0
    print(",---.               |                       ,---.     o     ")
    print("|---'.   .,---.,---.|---.,---.,---.,---.    |   |.   ..,---,")
    print("|    |   ||    |    |   |,---|`---.|---'    |   ||   || .-' ")
    print("`    `---'`    `---'`   '`---^`---'`---'    `---\`---'`'---'")
    print("Now that we have idenfity your problem",userName,"let's begin with the quiz.")
    print()
    print(",---.               |    o               '|")
    print("|--- ,---..   .,---.|--- .,---.,---.      |")
    print("|    |   ||   |,---||    ||   ||   |      |")
    print("`---'`---|`---'`---^`---'``---'`   '      `")
    print("         |                                 ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mIs this purchase a tangible item?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.    ,--'")
    print("|    |   ||   |,---||    ||   ||   |    |   ")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |  ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mWill this purchase be used often?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.      -|")
    print("|    |   ||   |,---||    ||   ||   |       |")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |                                  ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mDo you have the money for this purchase?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              |  |")
    print("|--- ,---..   .,---.|--- .,---.,---.    `--|")
    print("|    |   ||   |,---||    ||   ||   |       |")
    print("`---'`---|`---'`---^`---'``---'`   '       `")
    print("         |           ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mIf you waited a month to buy this item would you still want it?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ---.")
    print("|--- ,---..   .,---.|--- .,---.,---.    `--.")
    print("|    |   ||   |,---||    ||   ||   |       |")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |                                 ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mWill this item last long with a normal amount of use?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.    |--.")
    print("|    |   ||   |,---||    ||   ||   |    |  |")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |   ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mCan you use this item more than once?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ---.")
    print("|--- ,---..   .,---.|--- .,---.,---.       /")
    print("|    |   ||   |,---||    ||   ||   |      | ")
    print("`---'`---|`---'`---^`---'``---'`   '      | ")
    print("         |                            ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mWill this item make your item back.")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.    ,--.")
    print("|    |   ||   |,---||    ||   ||   |    |  |")
    print("`---'`---|`---'`---^`---'``---'`   '    `--'")
    print("         |                        ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mWould others disprove of this purchase?")
    print("\033[0m")
    totalPoints -= answerQuestion()
    print(",---.               |    o              ,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.    `__|")
    print("|    |   ||   |,---||    ||   ||   |       |")
    print("`---'`---|`---'`---^`---'``---'`   '       '")
    print("         |     ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mCan it find you and others joy?")
    print("\033[0m")
    totalPoints += answerQuestion()
    print(",---.               |    o               '|,--.")
    print("|--- ,---..   .,---.|--- .,---.,---.      ||  |")
    print("|    |   ||   |,---||    ||   ||   |      ||  |")
    print("`---'`---|`---'`---^`---'``---'`   '      ``--'")
    print("         |                             ")
    print("For this question you are not allowed to type 'Ask' please wait till the end of the quiz.")
    print("\033[1;36mIs this purchase necessary?")
    print("\033[0m")
    totalPoints += answerQuestion()
    #results
    print()
    if (totalPoints < 14):
        print (userName, "this purchase seems like a very bad idea. You should not make this purchase.")
        print("You will most likely regret this purchase later.")
    elif (totalPoints < 24):
        print(userName, "this seems like a bad purchase. You might find some joy in it but overall it be a bad choose.")
        print("We advise not to make this purchase it's not a good idea.")
    elif (totalPoints == 24):
        print(userName,"you seem unsure of this purchase. We advise you to save the money, wait a month, and think on it again then." )
        print("You may find the purchase is good for you in the long run but for now it's a bad idea.")
    elif (totalPoints < 35):
        print(userName, "this is a good purchase to make.")
        print("You might not want to make this purchase again but a one time purchase might not hurt.")
    else:
        print(userName, "this is a great purchase for you. You will not regret this later.")
        print("If you are thinking of this being a more than single purchase maybe this would be good for that.")
        print("But before buy more than one try out one. If you don't like it them don't buy another one.")
    print()
    print("Would you like to rate this quiz?")
    check = True
    while check:
        rateCheck = input("Please input yes or no:")
        if (rateCheck in spellingOfYes):
            rateMyQuiz("Purchases")
            print("Thank you for your input!")
            print("The most ratings we get the better these quizzes will become.")
            check = False
        else:
            print("That's okay, maybe next time!")
            check = False

#Calls all the functions in correct order.
intro()
instructions()
userName = getName()
check = True
#Main loop this will keep going until the user tells the program to stop.
while check:
    userProblem = getProblem()
    if (userProblem == "relationships"):
        relationshipQuiz(userName)
    if (userProblem == "events"):
        eventQuiz(userName)
    stay = replay()
    if (stay == 0):
        check = False
        exit()
