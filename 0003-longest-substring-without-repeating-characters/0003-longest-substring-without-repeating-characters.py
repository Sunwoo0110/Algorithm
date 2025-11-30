class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_set = set()
        left = 0
        answer = 0

        for right in range(len(s)):
            ## duplicate -> remove dup
            while s[right] in curr_set:
                curr_set.remove(s[left])
                left += 1
            curr_set.add(s[right])
            answer = max(answer, right-left + 1)

        return answer
