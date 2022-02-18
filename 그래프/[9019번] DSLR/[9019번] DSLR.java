import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static char alpha[] = {' ', 'D', 'S', 'L', 'R'};
	static int[] visited;
	static char[] word;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for (int t = 0; t < T; t++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			visited = new int[10000];
			word = new char[10000];
			Queue<Integer[]> q = new LinkedList<Integer[]>();
			visited[N] = -1;
			word[N] = 'A';			
			q.offer(new Integer[] {N, 0});
			int result = 0;
			while (!q.isEmpty()) {
				Integer[] cur = q.poll();
				int value = cur[0];
				int s_value = value;
				int move  = cur[1];
				if (value == M) {
					result = value;
					break;
				}
				int[] DSLR = new int[4]; 
				DSLR[0] = value * 2 % 10000;
				DSLR[1] = value - 1;
				if (DSLR[1] == -1) DSLR[1] = 9999;
				int[] v  = new int[4];
				v[0] = (s_value / 1000);
				s_value %= 1000;
				v[1] = (s_value / 100);
				s_value %= 100;
				v[2] = (s_value / 10);
				s_value %= 10;
				v[3] = (s_value);
				String _L = String.valueOf(v[1]) + String.valueOf(v[2]) + String.valueOf(v[3]) + String.valueOf(v[0]);
				String _R = String.valueOf(v[3]) + String.valueOf(v[0]) + String.valueOf(v[1]) + String.valueOf(v[2]);
				DSLR[2] = Integer.parseInt(_L);
				DSLR[3] = Integer.parseInt(_R);
				for (int i = 1; i < 5; i++) {
					if (word[DSLR[i-1]] == 0) {
						visited[DSLR[i-1]] = value;
						word[DSLR[i-1]] = alpha[i];
						q.add(new Integer[] {DSLR[i-1], move+1});
					}
				}
			}
			Stack<Character> stk = new Stack<Character>();
			while (word[result] != 'A') {
				stk.add(word[result]);
				result = visited[result];	
			}
			while (!stk.isEmpty()) {
				bw.write(stk.pop());
			}
			bw.write("\n");
		}
	
		bw.flush();
		bw.close();
	}
}
