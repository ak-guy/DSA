public class test {
    public static void main(String[] args) {
        int[] l = {1000000000,1000000000,1000000000,1000000000};
        int res = 0;
        for (int n : l) {
            res += n;
            System.out.println(res);
        }
    }
}