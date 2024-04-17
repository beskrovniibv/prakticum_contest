#! usr/bin/python

# B. Ловкость рук

from string import digits

def main(k, keyboard):
    nums = {}
    # mx = 0
    result = 0
    for i in range(4):
        for j in range(4):
            value = keyboard[i][j]
            if value in digits:
                value = int(value)
                # mx = max(mx, value)
                nums[value] = nums.get(value, 0) + 1
    for key, value in nums.items():
        if value <= 2*k:
            result += 1
    return result


if __name__ == "__main__":
    k = int(input())
    keyboard = []
    for _ in range(4):
        row = list(input())
        keyboard.append(row)
    result = main(k, keyboard)
    print(result)
