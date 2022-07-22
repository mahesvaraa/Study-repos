# from collections import Counter
# def is_merge(s, part1, part2):
#     print(s, part1, part2)
#     return Counter(s) == Counter(part1) + Counter(part2)
#
# print(is_merge('codewars', 'code', 'wasr'))

def is_merge(s, part1, part2):
    while s:
        if s[0] == part1[0]:
            s, part1 = s[1:], part1[1:]
        elif s[0] == part2[0]:
            s, part2 = s[1:], part2[1:]
        else:
            break
    return not s


print(is_merge('codewars', 'cwdr', 'oeas'))
