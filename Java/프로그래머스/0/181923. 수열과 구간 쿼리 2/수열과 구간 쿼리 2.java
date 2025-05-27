import java.util.Arrays;

class Solution {
            public int[] solution(int[] arr, int[][] queries) {
                int[] answer = new int[queries.length];
                int f=0;
                for (int[] query : queries) {
                    int s=query[0];
                    int e=query[1]+1;
                    int k=query[2];
                    int[] ans =Arrays.stream(Arrays.copyOfRange(arr, s, e))
                            .filter(x -> x>k)
                            .toArray();
                    Arrays.sort(ans);
                    answer[f++] = ans.length > 0 ? ans[0] : -1;
                    
                }

                return answer;
            }
        }