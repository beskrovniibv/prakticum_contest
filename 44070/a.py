#! usr/bin/python

# A. Ближайший ноль

def main(n: int, data: list[int]) -> list[int]:
    answer = [0]*n
    zeroes = []
    for i in range(n):
        if data[i] == 0:
            zeroes.append(i)
    for i in range(zeroes[0]):
        answer[i] = zeroes[0] - i
    for i in range(1, len(zeroes)):
        for j in range(zeroes[i - 1] + 1, zeroes[i]):
            answer[j] = min(j - zeroes[i - 1], zeroes[i] - j)
    for i in range(zeroes[-1] + 1, n):
        answer[i] = i - zeroes[-1]
    return answer


if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    result = main(n, data)
    print(*result)
