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
