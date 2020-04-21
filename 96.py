
Су Доку
Задача 96
Су Доку (в переводе с японского означает цифра ) - это название популярной головоломки. Его происхождение неясно, но следует отдать должное Леонхарду Эйлеру, который придумал аналогичную и гораздо более сложную идею головоломки под названием «Латинские квадраты». Цель загадок Су Доку, однако, состоит в том, чтобы заменить пробелы (или нули) в сетке 9 на 9 таким образом, чтобы каждая строка, столбец и поле 3 на 3 содержали каждую из цифр от 1 до 9. Ниже приведен пример типичной стартовой сетки головоломки и сетки ее решения.

0 0 3
9 0 0
0 0 1	0 2 0
3 0 5
8 0 6	6 0 0
0 0 1
4 0 0
0 0 8
7 0 0
0 0 6	1 0 2
0 0 0
7 0 8	9 0 0
0 0 8
2 0 0
0 0 2
8 0 0
0 0 5	6 0 9
2 0 3
0 1 0	5 0 0
0 0 9
3 0 0

4 8 3
9 6 7
2 5 1	9 2 1
3 4 5
8 7 6	6 5 7
8 2 1
4 9 3
5 4 8
7 2 9
1 3 6	1 3 2
5 6 4
7 9 8	9 7 6
1 3 8
2 4 5
3 7 2
8 1 4
6 9 5	6 8 9
2 5 3
4 1 7	5 1 4
7 6 9
3 8 2
Хорошо построенная головоломка Су Доку имеет уникальное решение и может быть решена с помощью логики, хотя может потребоваться использование методов «угадать и проверить», чтобы исключить варианты (по этому поводу существует много спорных мнений). Сложность поиска определяет сложность головоломки; Приведенный выше пример считается простым, поскольку он может быть решен прямым прямым выводом.

Текстовый файл 6K, sudoku.txt (щелчок правой кнопкой мыши и «Сохранить ссылку / цель как ...»), содержит пятьдесят различных головоломок Су Доку различной сложности, но все с уникальными решениями (первая головоломка в файле - пример выше ).

Решив все пятьдесят головоломок, найдите сумму трехзначных чисел, найденных в верхнем левом углу каждой решетки; например, 483 - это трехзначное число, найденное в верхнем левом углу таблицы решений выше.
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
    f = open('p096_sudoku.txt', 'r').readlines()
    data = ''.join(line[:9] for line in f if not 'Grid' in line)
    data = [data[n:(n + 81)] for n in range(0, len(data), 81)]

    for puzzle in data:
        fill_puzzle(puzzle)

    return sum_
