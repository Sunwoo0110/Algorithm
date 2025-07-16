import java.util.*;

class Solution{
    public int solution(int []A, int []B){
        int answer = 0;
        Arrays.sort(A); 
        Arrays.sort(B);

        int n = A.length;
        for (int i=0; i<n; i++) {
            answer += A[i] * B[n-1-i]; // A 큰 순서대로 B 작은 순서대로 곱하기
        }
        
        return answer;
    }
}