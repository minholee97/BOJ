import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, M, x, y, dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
	static char map[][];
	static int visit[][];
	static boolean visited[][];
	static Queue<Integer[]> fire;
	public static void bfs() {
		Queue<Integer[]> q = new LinkedList<Integer[]>();
		q.offer(new Integer[] {x, y, 0});
		visit[x][y] = 0;
		while(!q.isEmpty()) {
			Integer[] cur = q.poll();
			for (int i = 0; i < 4; i++) {
				int dx = cur[0] + dr[i];
				int dy = cur[1] + dc[i];
				if (dx > -1 && dx < N && dy > -1 && dy < M && visit[dx][dy] == -1 && map[dx][dy] == '.') {
					visit[dx][dy] = cur[2] + 1;
					q.offer(new Integer[] {dx, dy, cur[2] + 1});
				}
			}
		}
	}
	public static void bfs2() {
		while(!fire.isEmpty()) {
			Integer[] cur = fire.poll();
			for (int i = 0; i < 4; i++) {
				int dx = cur[0] + dr[i];
				int dy = cur[1] + dc[i];
				int move = cur[2] + 1;
				if (dx > -1 && dx < N && dy > -1 && dy < M && !visited[dx][dy] && map[dx][dy] == '.') {
					if (visit[dx][dy] >= move)
						visit[dx][dy] = -1;
					visited[dx][dy] = true;
					fire.offer(new Integer[] {dx, dy, move});
				}
			}
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for (int t = 1; t < T + 1; t++) {
			st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			N = Integer.parseInt(st.nextToken());
			map = new char[N][M];
			visit = new int[N][M];
			visited = new boolean[N][M];
			fire = new LinkedList<Integer[]>();
			for (int i = 0; i < N; i++) {
				String line = br.readLine();
				for (int j = 0; j < M; j++) {
					map[i][j] = line.charAt(j);
					if (map[i][j] == '@') {
						map[i][j] = '.';
						x = i;
						y = j;
					}
					else if (map[i][j] == '*') {
						fire.add(new Integer[] {i, j, 0});
						visited[i][j] = true;
					}
					
				}
			}
			for (int[] v : visit)
				Arrays.fill(v, -1);
			bfs();
			bfs2();
			ArrayList<Integer> result = new ArrayList<Integer>();
			for (int i = 0; i < N; i++) {
				if (i != 0 && i != N-1) {
					if (visit[i][0] != -1)
						result.add(visit[i][0]);
					if (visit[i][M-1] != -1)
						result.add(visit[i][M-1]);
					continue;
				}
				for (int j = 0; j < M; j++) {
					if (visit[i][j] != -1)
						result.add(visit[i][j]);
				}
			}
			if (result.size() == 0)
				bw.write("IMPOSSIBLE\n");
			else
				bw.write(String.valueOf(Collections.min(result)+1)+"\n");
		}
		bw.flush();
		bw.close();
	}
}
