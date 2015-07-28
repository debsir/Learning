public class PrimeNum {
    public static void main(String[] args) {
        for (int num = 100; num <= 200; num++) {
            int flag = 0;
            for (int i = 1; i <= num; i++) {
                if (num % i == 0) {
                    flag ++;
                }
            }
            if (flag <= 2) {
                System.out.println(num);
            }
        }
    }
}
