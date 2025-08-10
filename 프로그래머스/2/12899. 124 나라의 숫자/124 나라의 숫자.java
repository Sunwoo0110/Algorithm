import java.util.*;

class Solution {
    public String solution(int n) {
        StringBuilder answer = new StringBuilder();
        
         while (n > 0) {
            n -= 1;

            if (n % 3 == 0) answer.append("1");
            else if (n % 3 == 1) answer.append("2");
            else answer.append("4");

            n /= 3;
        }
        
        return answer.reverse().toString();
    }
}