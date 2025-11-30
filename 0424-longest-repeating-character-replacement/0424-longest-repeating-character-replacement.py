from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_cnt = 0
        answer = 0

        for right in range(len(s)):
            ## 1. add right char
            ch = s[right]
            count[ch] += 1
            max_cnt = max(max_cnt, count[ch])

            ## 2. check possible
            while (right-left+1) - max_cnt > k:
                count[s[left]] -= 1
                left += 1

            answer = max(answer, right-left+1)

        return answer
