from collections import Counter

with open('data/day6input.txt', 'r') as input_:
    answers = input_.read().split('\n\n')


def get_answer_count(group):
    group_counts = set()
    group_counts.update(set(group))
    try:
        group_counts.remove('\n')
    except:
        pass
    return len(group_counts)


answer_1 = sum([get_answer_count(g) for g in answers])


def get_everyone_answer_count(group):
    group = group.strip()
    group_counts = Counter(group)

    if group.count('\n') == 0:
        q_count = len([k for k in group_counts.keys() if k != '\n'])
        return q_count
    else:
        people = len(group.split('\n'))
        q_count = len([q[0] for q in group_counts.items()
                       if ((q[1] == people) and (q[0] != '\n'))])
        return q_count


answer_2 = sum([get_everyone_answer_count(group) for group in answers])

text_result = '\t--- PART ONE ---\nThe sum of the counts of questions to which anyone answered "yes" is {}.\n\n\t--- PART TWO - --\nThe sum of counts of number of questions to which everyone answered "yes" is {}.\n'.format(
    answer_1, answer_2)
print(text_result)
