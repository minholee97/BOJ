import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
	static int[] dr = {0, 0, -1, 1};
	static int[] dc = {1, -1, 0, 0};
	static boolean[][] map;
	static int M, N, K;
	static ArrayList<Node> q;
	static class Node {
		int i, j;
		public Node(int i, int j) {
			this.i = i;
			this.j = j;
		}
	}
	public static void bfs() {
		while (!q.isEmpty()) {
			Node c = q.remove(0);
			int x = c.i;
			int y = c.j;
			for (int i = 0; i < 4; i++) {
				int dx = x + dr[i];
				int dy = y + dc[i];
				if (dx > -1 && dx < M && dy > -1 && dy < N && map[dx][dy]) {
					map[dx][dy] = false;
					q.add(new Node(dx, dy));
				}
			}
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());
		for (; T > 0; T--) {
			String[] tokens = br.readLine().split(" ");
			int cnt = 0;
			M = Integer.parseInt(tokens[0]);
			N = Integer.parseInt(tokens[1]);
			K = Integer.parseInt(tokens[2]);
			map = new boolean[M][N];
			q = new ArrayList<Node>();
			for (int i = 0; i < K; i++) {
				String[] inputs = br.readLine().split(" ");
				int x = Integer.parseInt(inputs[0]);
				int y = Integer.parseInt(inputs[1]);
				map[x][y] = true;
			}
			for (int i = 0; i < M; i++) {
				for (int j = 0; j < N; j++) {
					if (map[i][j]) {
						q.add(new Node(i, j));
						map[i][j] = false;
						bfs();
						cnt++;
					}
						
				}
			}
			bw.write(String.valueOf(cnt) + '\n');
		}
		bw.flush();
		bw.close();
	}
}
