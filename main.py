def normalize_to_minus_one_one(numbers: list[float]) -> list[float]:

    if not numbers:
        return []

    max_val = max(numbers)
    min_val = min(numbers)

    if max_val == min_val:
        return [0] * len(numbers)

    result = []
    for number in numbers:
        norm = (2 * (number - min_val) / (max_val - min_val)) - 1
        result.append(norm)

    return result


def main():

    print(normalize_to_minus_one_one([5, 7, -2]))


if __name__ == '__main__':
    main()
