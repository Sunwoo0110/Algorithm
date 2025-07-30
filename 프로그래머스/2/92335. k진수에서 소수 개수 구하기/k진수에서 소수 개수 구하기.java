class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        
        StringBuilder sb = new StringBuilder();
        
        // k진수 변환
        while(n > 0){
            sb.append(String.valueOf(n%k));
            n /= k;
        }
        
        StringBuilder prime = new StringBuilder();
        
        for(char c: sb.reverse().toString().toCharArray()) {
            if(c == '0'){
                if(prime.toString().length() != 0 && isPrime(Long.parseLong(prime.toString()))) answer++;
                prime = new StringBuilder();
            } else {
                prime.append(c);
            }
        }

        if(prime.toString().length() != 0 && isPrime(Long.parseLong(prime.toString()))) answer++;
        
        return answer;
    }
    
    public boolean isPrime(long n){
        if (n<2) return false;
        
        long sqrt = (int)Math.sqrt(n);
        for(long i=2; i<=sqrt; ++i){
            if(n%i == 0){
                return false;
            }
        }
        return true;
    }
}