
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int T = Integer.parseInt(br.readLine());
    	
    	for (int tc = 1; tc <= T; tc++) {
    		
	        String str = br.readLine();
	        StringTokenizer st = new StringTokenizer(str," ");
	
	        int n = Integer.parseInt(st.nextToken());
	        int m = Integer.parseInt(st.nextToken());
	        
	        String bin = Integer.toBinaryString(m);
	        
	        int len = bin.length();
	        
	        char c = bin.charAt(len-n);
	        
	        String answer = "ON";
	        for (int i = c; i <=len; i++) {
	        	if (bin.charAt(i) == 0) {
	        		answer = "OFF";
	        		break;
	        	}
	        }
	        
	        System.out.println(answer);

    	}
    }
}
