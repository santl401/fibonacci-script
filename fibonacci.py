def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    count = int(input("Сколько чисел Фибоначчи вывести? "))
    print(fibonacci(count))