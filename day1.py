with open('data/day1input.txt', 'r') as input_:
    expense_report = [int(n[:4]) for n in input_.readlines()]

print('\t--- PART ONE ---')
subtracted = [2020 - i for i in expense_report]
possibles = []
for i in subtracted:
    if i in expense_report:
        possibles.append(i)

if len(possibles) == 2:
    if (possibles[0] + possibles[1]) == 2020:
        #print(possibles[0] * possibles[1])
        result = """The two entries that sum to 2020 are {} and {}.\nIf we multiply them together, we get {}.""".format(
            possibles[0], possibles[1], possibles[0] * possibles[1])
        print(result)
