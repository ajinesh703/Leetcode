class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = deque()  # Stores the current window
        self.sum = 0  # Track sum for O(1) average calculation

    def next(self, val: int) -> float:
        # Add new value to window and sum
        self.window.append(val)
        self.sum += val
        
        # Remove oldest element if window exceeds size
        if len(self.window) > self.size:
            removed = self.window.popleft()
            self.sum -= removed
        
        return self.sum / len(self.window)
