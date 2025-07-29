import java.util.*;

class Solution {
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        
        int[] answer = new int[sources.length];
        
        // 그래프
        List<List<Integer>> graph = new ArrayList<>();
        for(int i=0; i<=n; ++i) graph.add(new ArrayList<>());
        for(int[] road : roads){
            graph.get(road[0]).add(road[1]);
            graph.get(road[1]).add(road[0]);
        }

        // destination 시작 BFS
        int[] dist = new int[n+1];
        Arrays.fill(dist, -1); // -1로 초기화(방문 안 함)
        
        Queue<Integer> q = new LinkedList<>();
        q.add(destination);
        dist[destination] = 0;

        while (!q.isEmpty()) {
            int curr = q.poll();
            for (int next : graph.get(curr)) {
                if (dist[next] == -1) {
                    dist[next] = dist[curr]+1;
                    q.add(next);
                }
            }
        }

        for(int i=0; i<sources.length; ++i){
            answer[i] = dist[sources[i]];
        }

        return answer;
    }
}