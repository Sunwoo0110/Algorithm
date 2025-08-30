class Solution {
    public int solution(int[] arr) {
        int answer = arr[0];
        
        for(int n: arr){
            answer = (answer*n) / gcd(answer, n);
        }
        
        return answer;
    }
    
    public int gcd(int a, int b){
        while(b != 0){
            int tmp = a;
            a = b;
            b = tmp%b;
        }
        return a;
    }
}