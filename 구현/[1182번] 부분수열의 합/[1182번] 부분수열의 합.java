import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	static int N, S, result;
	static int[] check;
	public static void calc(int idx, int sum) {
		sum += check[idx];
		if (idx == N)
			return;
		if (sum == S)
			result++;
		calc(idx+1, sum);
		calc(idx+1, sum-check[idx]);
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		check = new int[N+1];
		S = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		result = 0;
		int idx = 0;
		while(st.hasMoreTokens()) {
			check[idx++] = Integer.parseInt(st.nextToken());
		}
		calc(0, 0);
		bw.write(String.valueOf(result));
		bw.flush();
		bw.close();
	}
}
