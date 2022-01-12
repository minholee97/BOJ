import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int count = 0;
    static int[] board;
    public static Boolean check(int x){
        for (int i = 0; i < x; i++) {
            if (board[i] == board[x] || x - i == Math.abs(board[x] - board[i]))
                return false;
        }
        return true;
    }
    public static void nqueen(int x) {
        if (x == N) {
            count++;
            return;
        }
        for (int i = 0; i < N; i++) {
            board[x] = i;
            if (check(x))
                nqueen(x + 1);
        }
        
    }
    
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        board = new int[N];
        nqueen(0);
        bw.write(String.valueOf(count));
        bw.flush();
        bw.close();
      
    }
}
