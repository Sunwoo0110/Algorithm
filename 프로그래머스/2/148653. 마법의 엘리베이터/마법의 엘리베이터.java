
class Solution {
    public int solution(int storey) {
        int answer = 0;
        
        while (storey > 0) {
            int curr = storey % 10;   // 1의 자리   
            int next = (storey / 10) % 10; // 10의 자리
            
            if (curr < 5) {
                // 내림
                answer += curr;
                storey /= 10;
            } else if (curr > 5) {
                // 올림
                answer += (10 - curr);
                storey = storey/10 + 1;
            } else {
                // 5일 때는 10의 자리도 확인
                if (next >= 5) {
                   // 올림
                    answer += (10 - curr);
                    storey = storey/10 + 1;
                } else {
                    // 내림
                    answer += curr;
                    storey /= 10;
                }
            }
        }
        
        return answer;
    }
}