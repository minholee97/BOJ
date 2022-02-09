import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		boolean[] prime = new boolean[1000001];
		prime[0] = true;
		prime[1] = true;
		for (int i = 2; i < Math.sqrt(1000001); i++) {
			if (prime[i]) continue;
			int j = 2;
			while (i * j < 1000001) {
				prime[i * j++] = true;
			}
		}		
		while (true) {
			int n = Integer.parseInt(br.readLine());
			if (n == 0) break;
			int p = -1;
			for (int i = 2; i < (n / 2) + 1; i++) {
				if (prime[i]) continue;
				if (!prime[n - i]) {
					p = i;
					break;
				}
			}
			if (p == -1) bw.write("Goldbach's conjecture is wrong.\n");
			else bw.write(String.valueOf(n) + " = " + String.valueOf(p) +" + "+ String.valueOf(n - p) + "\n");
			
		}
		bw.flush();
		bw.close();
	}

}
