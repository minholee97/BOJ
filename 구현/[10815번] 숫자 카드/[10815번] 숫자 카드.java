import java.io.*;
import java.util.*;
public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int[] plus  = new int[10000001];
        int[] minus = new int[10000001];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int card = Integer.parseInt(st.nextToken());
            if (card < 0)
                minus[-card] = 1;
            else
                plus[card] = 1;
        }
        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int card = Integer.parseInt(st.nextToken());
            if (card < 0)
                bw.write(String.valueOf(minus[-card]) + " ");
            else
                bw.write(String.valueOf(plus[card]) + " ");
        }
        bw.flush();
        bw.close();
    }
}
