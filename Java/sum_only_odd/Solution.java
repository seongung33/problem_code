package sum_only_odd;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for (int i =1; i<= T; i ++) {
			st = new StringTokenizer(br.readLine());
			int answer = 0;
			int[] arr = new int[10];
			for (int j= 0; j <10; j ++) {
				arr[j] = Integer.parseInt(st.nextToken());
				if(arr[j] % 2 == 1) {
					answer += arr[j];
				}
			}
			System.out.println("#"+i+" "+ answer);
		}
	}
}
