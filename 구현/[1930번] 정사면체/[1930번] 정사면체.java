import java.io.*;
import java.util.*;
public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for (; T > 0; T--) {
            String[] inputs = br.readLine().split(" ");
            int f1 = Integer.parseInt(inputs[0]);
            ArrayList<Integer> t1 = new ArrayList<Integer>();
            for (int i = 1; i < 4; i++)
                t1.add(Integer.parseInt(inputs[i]));
            int f2 = Integer.parseInt(inputs[4]);
            ArrayList<Integer> t2 = new ArrayList<Integer>();
            for (int i = 5; i < 8; i++)
                t2.add(Integer.parseInt(inputs[i]));
            int c1 = 0;
            for (int i = 0; i < 3; i++) {
                if (f1 == t1.get(i))
                    c1++;
            }
            if (f1 != f2) {
                for (int i = 0; i < 3; i++) {
                    int head = t2.remove(0);
                    if (f1 != head)
                        t2.add(head);
                    else {
                        t2.add(t2.remove(0));
                        t2.add(f2);
                        f2 = head;
                    }
                }
                if (f1 != f2) {
                    bw.write("0\n");
                    continue;
                }
            }
            boolean result = false;
            if (c1 == 1) {
                ArrayList<Integer> t3 = new ArrayList<Integer>();
                for (int i = 0; i < 3; i++)
                    t3.add(t1.get(i));
                t3.add(t3.remove(1));
                for (int i = 0; i < 3; i++) {
                    if (t2.equals(t1) || t2.equals(t3)) {
                        result = true;
                        break;
                    }
                    t1.add(t1.remove(0));
                    t3.add(t3.remove(0));
                }
            }
            else {
                for (int i = 0; i < 3; i++) {
                    if (t2.equals(t1)) {
                        result = true;
                        break;
                    }
                    t1.add(t1.remove(0));
                }
            }
            if (result)
                bw.write("1\n");
            else
                bw.write("0\n");
        }
        bw.flush();
        bw.close();
    }
}
