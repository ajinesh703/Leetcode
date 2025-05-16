from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        def is_one_letter_diff(s: str, t: str) -> bool:
            return len(s) == len(t) and sum(a != b for a, b in zip(s, t)) == 1

        lengths = [1] * n
        previous_index = [-1] * n

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and is_one_letter_diff(words[i], words[j]):
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        previous_index[i] = j

        max_length = max(lengths)
        index = lengths.index(max_length)

        result = []
        while index != -1:
            result.append(words[index])
            index = previous_index[index]

        return result[::-1]
