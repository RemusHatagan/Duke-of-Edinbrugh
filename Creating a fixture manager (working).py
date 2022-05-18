
# Opens the fixtures and results and stores them as arrays

import time

fixtureList = open("firesideFixtures.txt" , "r")
fixtureArray = []

for line in fixtureList.readlines():
    line = line.replace('\n' , "")
    fixtureArray.append(line.split(","))
fixtureList.close()

resultsList = open("firesideResults.txt" , "r")
resultsArray = []

allResults = resultsList.read()

for lines in resultsList.readlines():
    lines = lines.replace('\n' , "")
    resultsArray.append(line.split(","))
resultsList.close()

#Menu is displayed

def menu():
    time.sleep(0.3)
    print("")
    print("Welcome ... ")
    time.sleep(0.3)
    print("")
    print("Option A  -  Search for a fixture")
    print("Option B  -  Outstanding fixtures")
    print("Option C  -  Display leaderboard")
    print("")
    print("Enter Q to quit")
    print("")
    
    time.sleep(0.25)
    menuCh = str(input("Please enter the letter of the option you want to choose >>> ")).upper()
    return menuCh

menuChoice = menu()

if menuChoice == "A":
    time.sleep(0.1)
    fixtureChoice = str(input("Please enter the fixture you want to see ( 1 - 190 ) >>> "))
    
    for counter in range(len(fixtureArray)):
        if fixtureChoice == fixtureArray[counter][0]:
            print("Printing fixture ... ")
            print("")
            time.sleep(0.2)
            print("{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}".format("Fixture","Fixture","Fixture","Player 1","Player 2","Fixture","Winning"))
            print("{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}".format("Number","Date","Time","Nickname","Nickname","Played","Nickname"))
            print("")
            print("{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}".format(fixtureArray[counter][0],fixtureArray[counter][1],fixtureArray[counter][2],fixtureArray[counter][3],fixtureArray[counter][4],fixtureArray[counter][5]))
    if fixtureChoice not in fixtureArray[counter][0]:
        time.sleep(0.2)
        print("Fixture not found in database - Please try again ")
        menu()
            
# Option B

if menuChoice == "B":
    time.sleep(0.1)
    print("Displaying fixtures that have not been played ... ")
    print("Printing fixtures ... ")
    for counter in range(len(fixtureArray)):
        if fixtureArray[counter][5] != "Y":
            print("")
            time.sleep(0.2)
            print("{0:15}{1:15}{2:15}{3:15}{4:15}".format("Fixture","Fixture","Fixture","Player 1","Player 2","Winning"))
            print("{0:15}{1:15}{2:15}{3:15}{4:15}".format("Number","Date","Time","Nickname","Nickname","Nickname"))
            print("{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}".format(fixtureArray[counter][0],fixtureArray[counter][1],fixtureArray[counter][2],fixtureArray[counter][3],fixtureArray[counter][4],fixtureArray[counter][5]))

# Option C            

if menuChoice == "C":
    time.sleep(0.1)
    for counter in range(len(firesideResults)):

        # use bubble sort from Subprograms 3.py from github

menu()
