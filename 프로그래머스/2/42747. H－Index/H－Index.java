import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = citations.length;
        int len = citations.length;
        
        Arrays.sort(citations);
        
        while(answer > 0){
            if((answer == len && citations[len-answer] >= answer) 
                || (answer < len && citations[len-answer] >= answer && citations[len-answer-1] <= answer)) break;
            answer--;
        }
        return answer;
    }
}