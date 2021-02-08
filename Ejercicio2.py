g = 1
p = 1
while(g != 0 and p != 0):
    s = 0
    k = 0
    positions = []
    scores = []
    g, p = map(int, input().split())
    if ((g > 0 and g <= 100) and (p > 0 and p <= 100)):
        aux = 0
        while (aux < g):
            inputPositions = input()
            positions.append(inputPositions.split(" "))
            aux += 1
        k = int(input())
        aux = 0
        while (aux < k):
            inputScores = input().split(" ")
            lastFinishing = int(inputScores[0]) + 1
            historicPositions = [0] * p
            # Setting historial per player
            for x in range(g):
                for y in range(1, lastFinishing):
                    idx = positions[x].index(str(y))
                    historicPositions[idx] += int(inputScores[y])
            # calculate de winner/s
            max = 0
            winner = ""
            count = 1
            for x in historicPositions:
                if max <= int(x):
                    if max == int(x):
                        winner = winner + " " + str(count)
                    else:
                        winner = str(count)
                        max = x
                count += 1
            aux += 1
            print(winner)
