import numpy as np
with open('data/day1input.txt', 'r') as input_:
    expense_report = [int(n[:4]) for n in input_.readlines()]


def find_duplet(arr, sum_):
    subtracted = [sum_ - i for i in expense_report]
    possibles = []
    for i in subtracted:
        if i in expense_report:
            possibles.append(i)

    if len(possibles) == 2 and sum(possibles) == sum_:
        return possibles
    else:
        return False


duplet = find_duplet(expense_report, 2020)
if duplet:
    mult = np.product(duplet)
    text_result = """\t--- PART ONE ---\nThe two entries that sum to 2020 are {}.\nThe product of the two entries is {}.""".format(
        duplet, mult)
    print(text_result)


def find_all_triplets(arr, n, sum):
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k] == sum):
                    return arr[i], arr[j], arr[k]

    return False


result = find_all_triplets(expense_report, len(expense_report), 2020)

if result:
    text_result = f"\n\t--- PART TWO ---\nThe product of the three entries {result} that sum to 2020 is {np.prod(result)}.\n"
    print(text_result)
