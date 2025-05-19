# 1. Longest Substring Without Repeating Characters
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    l = 0
    result = 0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        result = max(result, r - l + 1)
    return result

# 2. Valid Anagram
def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# 3. Implement strStr() (Substring Search)
def str_str(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

# 4. Longest Palindromic Substring
def longest_palindrome(s: str) -> str:
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    res = ""
    for i in range(len(s)):
        tmp = expand(i, i)
        if len(tmp) > len(res):
            res = tmp
        tmp = expand(i, i + 1)
        if len(tmp) > len(res):
            res = tmp
    return res

# 5. Group Anagrams
from collections import defaultdict
def group_anagrams(strs):
    res = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        res[key].append(s)
    return list(res.values())

# 6. Valid Parentheses
def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

# 7. Longest Common Prefix
def longest_common_prefix(strs) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# 8. String to Integer (atoi)
def my_atoi(s: str) -> int:
    s = s.lstrip()
    if not s:
        return 0
    sign = 1
    res = 0
    i = 0
    if s[0] in ['-','+']:
        if s[0] == '-':
            sign = -1
        i += 1
    while i < len(s) and s[i].isdigit():
        res = res * 10 + int(s[i])
        i += 1
    res *= sign
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    if res < INT_MIN:
        return INT_MIN
    if res > INT_MAX:
        return INT_MAX
    return res

# 9. Palindrome Number (as a string problem)
def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

# 10. Roman to Integer
def roman_to_int(s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    total = 0
    for c in s[::-1]:
        if roman[c] >= prev:
            total += roman[c]
        else:
            total -= roman[c]
        prev = roman[c]
    return total
