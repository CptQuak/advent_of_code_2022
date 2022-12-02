oponent = {
    'A': 'Rock',
    'B': 'Paper', 
    'C': 'Scisors'
}

player = {
    'X': 'Rock',
    'Y': 'Paper', 
    'Z': 'Scisors'
}

shape_points = {
    'Rock': 1,
    'Paper': 2,
    'Scisors': 3
}

rounds = []
with open('day2/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        rounds.append(tuple(line.rstrip().split(' ')))
            

score = 0
for rnd in rounds:
    op = oponent[rnd[0]]
    pl = player[rnd[1]]
    score += shape_points[pl]

    if pl == op:
        score +=3
    elif (pl == 'Rock' and op == 'Paper') or (pl == 'Paper' and op == 'Scisors') or (pl == 'Scisors' and op == 'Rock'):
        score +=0
    else:
        score +=6

print(score)

