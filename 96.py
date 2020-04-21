

sum_ = 0
last = []


def go_to_last_valid(puzzle, blank=None):
    global last
    prev = last.pop()
    prev_index = prev[1]
    prev_value = prev[0]
    if prev_value + 1 <= 9:
        last.append([prev_value + 1, prev_index])
        rest = set()
        for a in range(81):
            if prev_index / 9 == a / 9 or not (prev_index - a) % 9 or (
                    prev_index / 27 == a / 27 and (prev_index % 9) / 3 == (a % 9) / 3):
                rest.add(puzzle[a])
        rest.remove('0')

        if len(rest) == 9:
            prev = go_to_last_valid(puzzle)

        for num in '123456789'[:prev_value]:
            if num not in rest:
                last.append([int(num), blank])
                fill_puzzle(puzzle[:blank] + num + puzzle[blank + 1:])
                break
        puzzle = puzzle[:prev_index] + '0' + puzzle[prev_index + 1:]
        go_to_last_valid(puzzle)
    else:
        puzzle = puzzle[:prev_index] + '0' + puzzle[prev_index + 1:]
        go_to_last_valid(puzzle)


def fill_puzzle(puzzle):
    global sum_
    global last
    blank = puzzle.find('0')

    # puzzle finished!
    if blank == -1:
        sum_ += int(puzzle[:3])
        print(puzzle[:3], sum_)
        last = []
        return

    rest = set()
    for a in range(81):
        if blank / 9 == a / 9 or not (blank - a) % 9 or (blank / 27 == a / 27 and (blank % 9) / 3 == (a % 9) / 3):
            rest.add(puzzle[a])

    rest.remove('0')

    if len(rest) == 9:
        prev = go_to_last_valid(puzzle)

    for num in '123456789':
        if num not in rest:
            last.append([int(num), blank])
            fill_puzzle(puzzle[:blank] + num + puzzle[blank + 1:])
            break



def answer():
    f = open('p096_sudoku.rtf', 'r').readlines()
    data = ''.join(line[:9] for line in f if not 'Grid' in line)
    data = [data[n:(n + 81)] for n in range(0, len(data), 81)]

    for puzzle in data:
        fill_puzzle(puzzle)

    return sum_
