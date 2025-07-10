import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> result = new ArrayList<>();
        
        // 장르, 총 재생 수
        Map<String, Integer> genPlay = new HashMap<>();
        // 장르, 노래 리스트(id, 재생 수)
        Map<String, List<int []>> genSong = new HashMap<>();
        
        for(int i=0; i<genres.length; ++i){
            genPlay.put(genres[i], genPlay.getOrDefault(genres[i], 0)+plays[i]);
            
            genSong.putIfAbsent(genres[i], new ArrayList<>());
            genSong.get(genres[i]).add(new int[]{i, plays[i]});
        }
        
        List<String> sortGenres = new ArrayList<>(genPlay.keySet());
        sortGenres.sort((a, b) -> genPlay.get(b) - genPlay.get(a)); // 내림차순
        
        for(String gen: sortGenres){
            List<int []> songs = new ArrayList<>(genSong.get(gen));
            songs.sort((a, b) -> b[1] - a[1]); // 내림차순
            
            if (songs.size() >= 2){
                result.add(songs.get(0)[0]);
                result.add(songs.get(1)[0]);
            }
            else if (songs.size() == 1){
                result.add(songs.get(0)[0]);
            }
        }
        
        
        
        int[] answer = new int[result.size()];
        
        for(int i=0; i<result.size(); ++i){
            answer[i] = result.get(i);
        }
        
        
        return answer;
    }
}