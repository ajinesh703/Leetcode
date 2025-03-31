def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        # Compute current area
        width = right - left
        curr_height = min(height[left], height[right])
        curr_area = width * curr_height

        # Update max area
        max_area = max(max_area, curr_area)

        # Move the pointer with the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
