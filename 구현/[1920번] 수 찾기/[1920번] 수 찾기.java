import java.io.*;
import java.util.*;
public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder  sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int idx = 0;
        while(st.hasMoreTokens()) {
            A[idx++] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);
        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        while(st.hasMoreTokens()) {
            int X = Integer.parseInt(st.nextToken());
            int left = 0, right = N - 1;
            boolean flag = false;
            while (left <= right) {
                int mid = (left + right) / 2;
                if (A[mid] == X) {
                    flag = true;
                    break;
                }
                else if (A[mid] < X)
                    left = mid + 1;
                else
                    right = mid - 1;
            }
            if (flag)
                sb.append("1\n");
            else
                sb.append("0\n");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
