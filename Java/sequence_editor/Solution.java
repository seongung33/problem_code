package sequence_editor;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
	private static final String answer = null;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int test=1; test <=T; test++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			int L = Integer.parseInt(st.nextToken());
			
			st = new StringTokenizer(br.readLine());
			ArrayList<Integer> sequence = new ArrayList<>();
			
			
			for (int i = 0; i < N; i++) {
				sequence.add(Integer.parseInt(st.nextToken()));
			}
			
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				char command = st.nextToken().charAt(0);
				
				if (command =='I') {
					int idx = Integer.parseInt(st.nextToken());
					int num = Integer.parseInt(st.nextToken());
					sequence.add(idx, num);
				} else if (command == 'D') {
					int idx = Integer.parseInt(st.nextToken());
					sequence.remove(idx);
				} else if (command =='C') {
					int idx = Integer.parseInt(st.nextToken());
					int num = Integer.parseInt(st.nextToken());
					sequence.set(idx, num);
				}
			}
			
			int answer;
			
			if (sequence.size() > L) {
				answer = sequence.get(L);
			} else {
				answer = -1;
			}
			
			System.out.println("#" +test + " " + answer);
		}
	}
}