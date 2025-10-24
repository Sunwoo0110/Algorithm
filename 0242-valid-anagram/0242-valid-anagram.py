from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## 애너그램은 순서가 중요하지 않고, 단어의 개수가 중요할 것 같습니다. 따라서 저라면 map 을 사용해 각 문자열의 숫자 개수를 세고, 그 개수가 동인한 경우에 같고 아니면 다르다 라고 표현할 것 같습니다.

        s_map, t_map = defaultdict(int), defaultdict(int)
        
        if len(s) != len(t):
            return False
        
        for s_ch, t_ch in zip(s, t):
            s_map[s_ch] += 1
            t_map[t_ch] += 1

        if s_map == t_map:
            return True
        
        return False

