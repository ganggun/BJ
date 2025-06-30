class Solution {
    public int solution(String number) {
        int answer = 0;
        char[] a =number.toCharArray();
        for (char c : a) {
            answer+=Character.getNumericValue(c);
        }
        answer%=9;
        return answer;
    }
}