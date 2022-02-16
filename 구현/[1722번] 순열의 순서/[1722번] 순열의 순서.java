import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int q = Integer.parseInt(st.nextToken());
		if (q == 1) {
			long k = Long.parseLong(st.nextToken());
			long size = 1;
			for (long i = 2; i < N; i++) {
				size *= i;
			}
			k -= 1;
			long cnt[] = new long[N];
			int idx = 0;
			for (long i = N - 1; i > 0; i--) {
				if (size <= k) {
					cnt[idx++] = (long) (k / size);
					k %= size;
					size /= i;
				}
				else {
					cnt[idx++] = 0;
					size /= i;
				}
			}
			long result[] = new long[N];
			boolean[] check = new boolean[N];
			for (int i = 0; i < N; i++) {
				long count = 0;
				for (int j = 0; j < N; j++) {
					if (check[j]) continue;
					if (cnt[i] == count) {
						check[j] = true;
						result[i] = j + 1;
						break;
					};
					count++;
				}
			}
			for (int i = 0; i < N; i++) {
				bw.write(String.valueOf(result[i]) + " ");
			}
		}
		else {
			long[] k = new long[N];
			long[] cnt = new long[N];
			for (int i = 0; i < N; i++) {
				k[i] = Long.parseLong(st.nextToken());
			}
			long result = 1, size = N -1;
			boolean[] check = new boolean[N];
			for (int i = 0; i < N; i++) {
				long target = k[i] - 1;
				int count = 0;
				for (int j = 0; j < N; j++) {
					if (check[j]) continue;
					if (target == j) {
						check[j] = true;
						break;
					}
					count++;
				}
				cnt[i] = count;
			}
			long mul = 1, width = 1;
			for (int i = N - 2; i > -1; i--) {
				mul *= width++;
				result += cnt[i] * mul;
			}
			bw.write(String.valueOf(result));
		}
		bw.flush();
		bw.close();
	}

}
