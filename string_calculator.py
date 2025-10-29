def add(numbers: str) -> int:
    if numbers == "":
        return 0
    parts = numbers.split(",")
    total = 0
    for num in parts:
        total += int(num)
    return total

