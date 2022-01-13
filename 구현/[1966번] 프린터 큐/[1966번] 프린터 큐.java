import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    int T = Integer.parseInt(br.readLine());
    for (int i = 0; i < T; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        ArrayList<Integer> array = new ArrayList<Integer>();
        while (st.hasMoreTokens())
            array.add(Integer.parseInt(st.nextToken()));
        int count = 1;
        while (true) {
            int front = array.remove(0);
            int len = array.size();
            if (len == 0)
                break;
            Boolean flag = false;
            for (int j = 0; j < len; j++) {
                if (front < array.get(j)) {
                    array.add(front);
                    flag = true;
                    break;
                }
            }
            if (flag == false) {
                if (M == 0)
                    break;
                else
                    M -= 1;
                count++;
            }
            else {
                if (M == 0)
                    M = array.size() - 1;
                else
                    M -= 1;
            }

        }
        bw.write(String.valueOf(count) + '\n');
    }
    bw.flush();
    bw.close();
    }
}
