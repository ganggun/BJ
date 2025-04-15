class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String a1= Integer.toString(a);
        String b1= Integer.toString(b);
        String an=a1+b1;
        String an1=b1+a1;
        int i= Integer.parseInt(an);
        int i1= Integer.parseInt(an1);
        answer+= (i>i1)? i :i1;
        return answer;
    }
}