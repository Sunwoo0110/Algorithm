class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.strip().split()[::-1]
        answer = " ".join(lst)

        return answer
        