from Elf import Elf

def createElves():
    elves = []
    with open('day1/input.txt') as f:
        lines = f.readlines()
        calories = []
        for line in lines:
            if line not in ['\r\n',"\n"]:
                calories.append(int(line))
            else:
                elves.append(Elf(calories))
                calories = []
                
    return elves

### PART 1
elves = createElves()
highest_id = None
highest_calories = 0

for idx, elf_ in enumerate(elves):
    if elf_.total_calories > highest_calories:
        highest_calories = elf_.total_calories
        highest_id = idx
print('Part 1 answer:')
print(highest_id, highest_calories)


### PART 2
all_total_calories = [elf_.total_calories for elf_ in elves]
all_total_calories.sort(reverse=True)
print('Part 2 answer:')
top_3 = all_total_calories[:3]
print(top_3, sum(top_3))
