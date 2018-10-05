def solution(number):
    numbers = []
    for x in range(number -1, 0, -1):
        if (x % 3 == 0):
            numbers.append(x)
            continue
        elif (x % 5 == 0):
            numbers.append(x)
            continue
        else:
            continue
    return sum(numbers)

if __name__ == "__main__":
    result = solution(10)
    print(result)