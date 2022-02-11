import java.io.*;
import java.util.*;
public class Main {
    static int N, M, count, dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1}, map[][];
    static boolean[][] visited;
    public static boolean clear() {
        ArrayList<Integer[]> q = new ArrayList<Integer[]>();
        q.add(new Integer[] {0, 0});
        visited = new boolean[N][M];
        visited[0][0] = true;
        boolean flag = true;
        while (!q.isEmpty()) {
            Integer[] cur = q.remove(0);
            for (int i = 0; i < 4; i++) {
                int dx = cur[0] + dr[i];
                int dy = cur[1] + dc[i];
                if (dx > -1 && dx < N && dy > -1 && dy < M) {
                    if(!visited[dx][dy] && map[dx][dy] == 0) {
                        visited[dx][dy] = true;
                        q.add(new Integer[] {dx, dy});
                    }
                    if (map[dx][dy] != 0) {
                        map[dx][dy]++;
                        flag = false;
                    }
                }
            }
        }
        return flag;
    }
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        count = 0;
        ArrayList<Integer[]> ch = new ArrayList<Integer[]>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 1) {
                    count++;
                    ch.add(new Integer[] {i, j});
                }
            }
        }
        int result = 0;
        while (true) {
            if (clear()) break;
            result++;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (map[i][j] > 2)
                        map[i][j] = 0;
                    else if (map[i][j] == 2)
                        map[i][j] = 1;
                    
                }
            }
        }
        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
    }
}
