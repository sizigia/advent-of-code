import re

with open('data/day2input.txt', 'r') as input_:
    psswrd_corporate_pol = input_.readlines()


def check_times(item):
    tmin, tmax, letter_, psswrd = [
        re.match(r"(\d+)-(\d+) (\D): (\D+)", item).group(i) for i in range(1, 5)]
    tmin, tmax = [int(t) for t in (tmin, tmax)]
    occ = psswrd.count(letter_)

    return (occ >= tmin and occ <= tmax)


def check_positions(item):
    plow, phigh, letter_, psswrd = [
        re.match(r"(\d+)-(\d+) (\D): (\D+)", item).group(i) for i in range(1, 5)]
    plow, phigh = [int(t) - 1 for t in (plow, phigh)]

    return (psswrd[plow] == letter_ or psswrd[phigh] == letter_) and (psswrd[plow] != psswrd[phigh])


pcount = 0
vcount = 0

for item in psswrd_corporate_pol:
    if check_times(item):
        pcount += 1

    if check_positions(item):
        vcount += 1


text_result = '\t--- PART ONE ---\nThere are {} valid passwords, according to their policies.\n\n\t--- PART TWO - --\nThere are {} valid passwords, according to the new interpretation of the policies.\n'.format(
    pcount, vcount)
print(text_result)
