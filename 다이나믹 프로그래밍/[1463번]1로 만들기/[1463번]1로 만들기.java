import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int[] dp = new int[1000001];
        dp[1] = 0;
        dp[2] = 1;
        dp[3] = 1;
        if (N > 3) {
            for (int i = 4; i < N + 1; i++) {
                if (i % 3 == 0) {
                    dp[i] = dp[i / 3] + 1;
                }
                if (i % 2 == 0) {
                    if (dp[i] == 0)
                        dp[i] = dp[i / 2] + 1;
                    else
                        dp[i] = Math.min(dp[i], dp[i / 2] + 1); 
                }
                if (dp[i] == 0)
                    dp[i] = dp[i - 1] + 1;
                else
                    dp[i] = Math.min(dp[i], dp[i - 1] + 1);
            }
        }
        System.out.println(dp[N]);
    }
}
