Двухосновные палиндромы

Задача 36
Десятичное число 585 = 1001001001 2 (двоичное) является палиндромным в обоих основаниях.

Найдите сумму всех чисел, меньше одного миллиона, которые являются палиндромными в базе 10 и базе 2.

(Обратите внимание, что число палиндромов в любой из баз не может включать начальные нули.)

def answer():
    sum_ = 0
    for num in range(1000000):
        if palindromic_10_2(num):
            sum_ += num
    return sum_


def palindromic_10_2(num):
    if palindromic(num) and palindromic(bin(num)[2:]):
        return True
    return False


def palindromic(num):
    num_str = str(num)
    for i in range(len(num_str) / 2):
        if num_str[i] != num_str[-(i + 1)]:
            return False
    return True


if __name__ == "__main__":
    print(answer())
