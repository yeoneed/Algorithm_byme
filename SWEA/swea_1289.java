package ws_0801;
import java.util.Scanner;

public class swea_1289 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int t_idx =1; t_idx<=t; t_idx++) {
			String tc = sc.next(); //testcase 입력
			int cnt=0;
			if(tc.charAt(0)=='1') {
				cnt+=1;
			}
			for(int i=1; i<tc.length(); i++) {
				if((tc.charAt(i))!=(tc.charAt(i-1))) {
					cnt+=1;
				}
			}
			System.out.printf("#%d %d", t_idx, cnt);
			System.out.println();
		}
	}
}
