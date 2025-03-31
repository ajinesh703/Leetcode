import bisect

def twoSumBinarySearch(numbers, target):
    for i in range(len(numbers)):
        complement = target - numbers[i]
        index = bisect.bisect_left(numbers, complement, i + 1)  # Binary search for complement
        if index < len(numbers) and numbers[index] == complement:
            return [i + 1, index + 1]
    return []
