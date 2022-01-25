import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
      int N = Integer.parseInt(br.readLine());
      char[][] fr = new char[N][N];
      for (int i = 0; i < N; i++) {
          fr[i] = br.readLine().toCharArray();
      }
      int result = 0;
      for (int i = 0; i < N; i++) {
          boolean[] check = new boolean[N];
          for (int j = 0; j < N; j++) {
              if(fr[i][j] == 'Y') {
                  check[j] = true;
                  for(int k = 0; k < N; k++) {
                     if (fr[j][k] == 'Y')
                        check[k] = true;
                  }
              }
          }
          int cnt = 0;
          for (int j = 0; j < N; j++) {
              if (j == i)
                continue;
              if(check[j])
                cnt++;
          }
          result = Math.max(result, cnt);
      }
      bw.write(String.valueOf(result));
      bw.flush();
      bw.close();
    }
}
