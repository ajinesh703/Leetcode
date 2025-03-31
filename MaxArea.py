def maxAreaBruteForce(height):
    max_area = 0
    n = len(height)
    for i in range(n):
        for j in range(i + 1, n):
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
    return max_area
