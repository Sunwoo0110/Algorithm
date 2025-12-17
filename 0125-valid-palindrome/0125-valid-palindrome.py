class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ## 대문자 -> 소문자
        # s = s.lower()
        # new_s = []
        
        # ## 알파벳 제외 다 삭제
        # for c in s:
        #     if c.isalpha() or c.isdigit():
        #         new_s.append(c)
        
        # if new_s == new_s[::-1]:
        #     return True
        # return False

        ## two pointer
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not s[left].isalpha() and not s[left].isdigit():
                left += 1
            
            while left < right and not s[right].isalpha() and not s[right].isdigit():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True
        