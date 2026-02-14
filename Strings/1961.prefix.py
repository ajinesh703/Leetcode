class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        total_len = 0
        
        for i, word in enumerate(words):
            total_len += len(word)
            
            # If we've exceeded s, impossible
            if total_len > len(s):
                return False
            
            # If lengths match, check if concatenation equals s
            if total_len == len(s):
                return ''.join(words[:i + 1]) == s
        
        return False
