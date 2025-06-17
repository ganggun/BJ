class Solution {
    public String solution(String my, int[] index) {
        String answer = "";
        char[] arr= my.toCharArray();
        for(int i : index){
            answer += arr[i];
        }
        return answer;
    }
}