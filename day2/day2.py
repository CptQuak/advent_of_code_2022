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

def read_rounds():
    rounds = []
    with open('day2/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            rounds.append(tuple(line.rstrip().split(' ')))
    return rounds

def calculate_score_part1(rounds):
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
    return score

rounds = read_rounds()
print(calculate_score_part1(rounds))

def calculate_score_part2(rounds):
    score = 0
    for rnd in rounds:
        op = oponent[rnd[0]]
        p_sign = rnd[1]
        # chosing sign to lose
        if p_sign == 'X':
            if op == 'Rock':
                pl = 'Scisors'

            elif op =='Paper':
                pl = 'Rock'

            else:
                pl = 'Paper'
            score += 0
        # chosing sign to win
        elif p_sign == 'Z':
            if op == 'Rock':
                pl = 'Paper'

            elif op =='Paper':
                pl = 'Scisors'

            else:
                pl = 'Rock'
            score += 6
        # chosing sign to draw
        else:
            pl = op
            score += 3
        
        # calc score
        score += shape_points[pl]

    return score

print(calculate_score_part2(rounds))