rawData = open("input/input.txt")


def scoreFromChoice(choice):
    match choice:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3
        case _:
            return

def scoreFromResult(myPlay, oppPlay):
    match oppPlay:
        case "A":
            match myPlay:
                case "X":
                    return 3
                case "Y":
                    return 6
                case "Z":
                    return 0
        case "B":
            match myPlay:
                case "X":
                    return 0
                case "Y":
                    return 3
                case "Z":
                    return 6
        case "C":
            match myPlay:
                case "X":
                    return 6
                case "Y":
                    return 0
                case "Z":
                    return 3

def resultScore(result):
    match result:
        case "X":
            return 0
        case "Y":
            return 3
        case "Z":
            return 6

def generateLose(oppChoice):
    match oppChoice:
        case "A":
            return "Z"
        case "B":
            return "X"
        case "C":
            return "Y"

def generateDraw(oppChoice):
    match oppChoice:
        case "A":
            return "X"
        case "B":
            return "Y"
        case "C":
            return "Z"

def generateWin(oppChoice):
    match oppChoice:
        case "A":
            return "Y"
        case "B":
            return "Z"
        case "C":
            return "X"


totalScore = 0

for line in rawData.readlines():
    eventAsArray = line.split()
    opponentPlay = eventAsArray[0]
    reqResult = eventAsArray[1]

    resScore = resultScore(reqResult)

    myChoice = ""

    match reqResult:
        case "X":
            myChoice = generateLose(opponentPlay)
        case "Y":
            myChoice = generateDraw(opponentPlay)
        case "Z":
            myChoice = generateWin(opponentPlay)

    myChoiceScore = scoreFromChoice(myChoice)

    totalScore += resScore + myChoiceScore



print(totalScore)




