f = open('Input1.txt', 'r')
line = 0
positions = []
scores = []
fileContent = f.read().split("\n")
while (fileContent[line] != '0 0'):
    prix = int(fileContent[line][0])
    players = int(fileContent[line][2])
    while(prix != 0):
        line += 1
        positions.append(fileContent[line])
        prix -= 1
    line += 1
    numSystem = int(fileContent[line])
    while (numSystem != 0):
        line += 1
        scores.append(fileContent[line])
        numSystem -= 1
    line += 1
    print(f'Prix {prix} -- {players}')
    print(f'Positions {positions}')
    print(f'Scores {scores}')
    print('-----------------------')
