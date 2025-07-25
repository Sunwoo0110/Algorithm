import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            graph.add(new ArrayList<>());

        for (int[] e : edge) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }

        int[] dist = new int[n+1];
        Arrays.fill(dist, -1);   // -1이면 방문 안 함
        
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        dist[1] = 0;

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (int next: graph.get(curr)) {
                if (dist[next] == -1) {
                    dist[next] = dist[curr]+1;
                    queue.add(next);
                }
            }
        }

        int max = 0;
        for(int d: dist){
            max = Math.max(max, d);
        }
        
        int answer = 0;
        for (int d: dist){
            if (d == max)
                answer++;
        }
            

        return answer;
    }
}
