import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String S = br.readLine();
        String T = br.readLine();
        Boolean reversed = false;
        int idx;
        char c;
        for(int i = T.length(), end = S.length(); i > end; i--) {
            if (!reversed) {
                idx = 0;
                c = T.charAt(T.length() - 1);
                T = T.substring(idx, T.length() - 1);
            }
            else {
                idx = 1;
                c = T.charAt(0);
                T = T.substring(idx, T.length());
            }
            if (c == 'B')
                reversed = !reversed;
        }
        if (reversed) {
            StringBuffer sb = new StringBuffer(T);
            T = sb.reverse().toString();
        }
        if (S.equals(T))
            bw.write("1");
        else
            bw.write("0");
        bw.flush();
        bw.close();
    }
}
