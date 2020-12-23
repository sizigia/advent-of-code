with open('data/day5input.txt', 'r') as input_:
    boarding_input = input_.read().split('\n')


def get_seat_loc(loc: str, letters):
    no = {
        'rows': 128,
        'columns': 8
    }
    breakdown = {
        'upper': lambda r: r[len(r) // 2:],
        'lower': lambda r: r[:len(r) // 2]
    }
    keys = {
        'F': breakdown['lower'],
        'B': breakdown['upper'],
        'R': breakdown['upper'],
        'L': breakdown['lower'],
    }
    line = list(range(no[loc]))

    for letter in letters:
        line = keys[letter](line)

    return line[0]


def get_seat_ID(row, col):
    return row * 8 + col


def get_seat_ids(boarding_input):
    seat_ids = []

    for boarding_pass in boarding_input:
        row, column = get_seat_loc('rows', boarding_pass[:7]), get_seat_loc(
            'columns', boarding_pass[7:])

        seat_ids.append(get_seat_ID(row, column))

    return seat_ids


def get_highest_ID(seat_ids):
    return max(seat_ids)


seat_ids = get_seat_ids(boarding_input)


answer_1 = get_highest_ID(seat_ids)


def get_my_seat_id(seat_ids):
    possible_ids = [id_ for id_ in seat_ids if (
        (id_ - 1) not in seat_ids or (id_ + 1) not in seat_ids)]
    possible_ids = [id_ for id_ in possible_ids if id_ not in (
        min(possible_ids), max(possible_ids))]

    for i in possible_ids:
        if (i - 2) in seat_ids:
            if (i + 2) in seat_ids:
                return i + 1


answer_2 = get_my_seat_id(seat_ids)

text_result = '\t--- PART ONE ---\nThe highest seat ID on a boarding pass is {}.\n\n\t--- PART TWO - --\nMy seat ID is {}.\n'.format(
    answer_1, answer_2)
print(text_result)
