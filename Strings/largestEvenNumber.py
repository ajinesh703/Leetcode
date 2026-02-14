class Solution:
    def largestEvenNumber(self, num: str) -> str:
        # Convert to list and sort descending
        digits = sorted(num, reverse=True)
        
        # Find the smallest even digit from the end
        even_idx = -1
        for i in range(len(digits) - 1, -1, -1):
            if int(digits[i]) % 2 == 0:
                even_idx = i
                break
        
        # No even digit found
        if even_idx == -1:
            return ""
        
        # Build result: all digits except the even one, then the even digit
        result = digits[:even_idx] + digits[even_idx + 1:] + [digits[even_idx]]
        
        # Join and handle leading zeros
        result_str = ''.join(result)
        
        # If all zeros, return "0"
        if all(c == '0' for c in result_str):
            return "0"
        
        return result_str
```

## Step-by-Step Example

Input: `"2465"`

**Step 1: Sort descending**
```
digits = ['6', '5', '4', '2']
```

**Step 2: Find smallest even digit**
```
Scan from right: '2' is even
even_idx = 3
```

**Step 3: Build result**
```
Before even digit: ['6', '5', '4']
After even digit: []
Even digit: ['2']
Result: ['6', '5', '4', '2']
Final: "6542"
```

## Another Example

Input: `"4206"`

**Step 1: Sort descending**
```
digits = ['6', '4', '2', '0']
```

**Step 2: Find smallest even digit**
```
Scan from right: '0' is even
even_idx = 3
```

**Step 3: Build result**
```
Result: ['6', '4', '2', '0']
Final: "6420"
