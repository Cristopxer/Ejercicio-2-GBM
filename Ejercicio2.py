g = 1
p = 1
s = 0
k = 0
positions = []
scores = []
while(g != 0 and p != 0):
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
            # define winner
            lastFinishing = int(inputScores[0]) + 1
            historicPositions = [0] * p
            for x in range(g):
                for y in range(1, lastFinishing):
                    idx = positions[x].index(str(y))
                    historicPositions[idx] += int(inputScores[y])
            print(historicPositions)
            aux += 1
