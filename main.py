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

totalScore = 0

for line in rawData.readlines():
    eventAsArray = line.split()
    opponentPlay = eventAsArray[0]
    myPlay = eventAsArray[1]

    choiceScore = scoreFromChoice(myPlay)
    resultScore = scoreFromResult(myPlay, opponentPlay)

    totalScore += choiceScore + resultScore

print(totalScore)




