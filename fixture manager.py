
# Opens the fixtures and results and stores them as arrays

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

print("")
print("Welcome ... ")
print("")
print("Option A  -  Search for a fixture")
print("Option B  -  Outstanding fixtures")
print("Option C  -  Display leaderboard")
print("")
print("Enter Q to quit")
print("")

#Menu choices

menuChoice = str(input("Please enter the letter of the option you want to choose >>> ")).upper()

if menuChoice == "A":
    fixtureChoice = str(input("Please enter the fixture you want to see ( 1 - 190 ) >>> "))
    
    for counter in range(len(fixtureArray)):
        if fixtureChoice == fixtureArray[counter][0]:
            print("")
            print("Printing fixture ... ")
            print("")
            print("{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}{6:15}".format("Fixture","Fixture","Fixture","Player 1","Player 2","Fixture","Winning"))
            print("{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}{6:15}".format("Number","Date","Time","Nickname","Nickname","Played","Nickname"))
            print("")
            print("{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}{6:15}".format(fixtureArray[counter][0],fixtureArray[counter][1],fixtureArray[counter][2],fixtureArray[counter][3],fixtureArray[counter][4],fixtureArray[counter][5],fixtureArray[counter][6]))
            
if menuChoice == "B":
    print(resultsArray)
    
if menuChoice == "C":
    print("siu")
    
if menuChoice == "Q":
    exit()

    
