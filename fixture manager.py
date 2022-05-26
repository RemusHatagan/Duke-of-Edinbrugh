
# Opens the fixtures and results and stores them as arrays

import time
import math

fixtureList = open("firesideFixtures.txt" , "r")
fixtureArray = []

for line in fixtureList.readlines():
    line = line.replace('\n' , "")
    fixtureArray.append(line.split(","))
fixtureList.close()

resultsList = open("firesideResults.txt" , "r")
resultsArray = []

for lines in resultsList.readlines():
    lines = lines.replace('\n' , "")
    resultsArray.append(lines.split(","))
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

def bubbleSort(resultsArray):
    n = len(resultsArray)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(resultsArray[j][2]) < int(resultsArray[j+1][2]) :
                resultsArray[j], resultsArray[j+1] = resultsArray[j+1], resultsArray[j]
    return resultsArray
            
scores = []

if menuChoice == "C":
    time.sleep(0.1)
    bubbleSort(resultsArray)
    for counter in range(len(resultsArray)):
        resultsArray[counter][2] = int(resultsArray[counter][2])
        scores.append(resultsArray[counter][2])
    print(resultsArray)
    print("")
    print(scores)
    print(resultsArray[2])
    print("")
    
for leadScore in range(len(scores)):
        print("{0:15}{1:15}{2:15}{3:15}{4:15}".format("Player","Matches","Matches","Matches","Points",))
        print("{0:15}{1:15}{2:15}{3:15}{4:15}".format("Nickname","Played","Won","Lost",""))
        print("")
        print("{0:15}{1:15}{2:15}{3:15}{4:15}".format(resultsArray[counter][0],resultsArray[counter][1],resultsArray[counter][2],resultsArray[counter][3],scores[counter]))
        print("")
