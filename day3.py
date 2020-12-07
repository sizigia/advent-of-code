import numpy as np

with open('data/day3input.txt', 'r') as input_:
    pattern = [i.strip() for i in input_.readlines()]

slope = (3, 1)


def check_trees(slope, start=(0, 0)):
    right, down = slope  # slope
    x, y = start  # current position
    tree = '#'
    t_enc = 0  # trees encountered

    while y < len(pattern) - 1:
        x += right
        x %= len(pattern[0])
        y += down

        if y < len(pattern):
            if pattern[y][x] == tree:
                t_enc += 1

    return t_enc


answer_1 = check_trees(slope)


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
answer_2 = np.product([check_trees(i) for i in slopes])


text_result = '\t--- PART ONE ---\nStarting at the top-left corner of your map and following a slope of right 3 and down 1, you\'d encounter {} trees.\n\n\t--- PART TWO - --\nIf you multiply together the number of trees encountered on each of the listed slopes, you get {}.\n'.format(
    answer_1, answer_2)
print(text_result)
