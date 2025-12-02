class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)  ## 1시간에 먹을 수 있는 바나나 수
        
        while left < right:
            mid = (left+right) // 2
            
            ## 올림으로 계산
            if sum((pile+mid-1)//mid for pile in piles) <= h:
                right = mid
            else:
                left = mid+1

        return left