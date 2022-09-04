import java.util.*;
import java.io.*;

public class swea_4008_숫자만들기 {
	static int[] num;
	static int[] sign;
	static int max_int = Integer.MIN_VALUE; //최대값
	static int min_int = Integer.MAX_VALUE; //최소값
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int t_num = sc.nextInt();
		for(int t=1; t<=t_num; t++) {
			int n = sc.nextInt();
			num = new int[n];
			sign = new int[n-1];
			for(int i=0; i<n-1; i++) {
				sign[i] = sc.nextInt();
			} //기호 입력
			for(int i=0; i<n; i++) {
				num[i] = sc.nextInt();
			}//숫자 입력
			perm(sign, n, 0, num[0]);
			System.out.printf("#%d %d", t, max_int-min_int);
		}
	}

	private static void perm(int[] sign, int n, int lv, int result) {
		if(lv>=n) return;
		if(lv==n-1) {
			if(result>max_int) {
				max_int = result;
				System.out.println(max_int);
			}
			if(result<min_int) {
				min_int = result;
				System.out.println(min_int);
			}
		}
		else {
			for(int i=0; i<n-1; i++) {
				if(sign[i]<=0) continue;
				else {
					sign[i]--;
					result = calculate(result, i, lv);
					perm(sign, n,lv+1,result);
					sign[i]++;
				}
			}
		}
	}

	private static int calculate(int result, int i, int lv) {
		switch(i) {
		case 0: {
			result+= num[lv+1];
			break;
		}
		case 1:{
			result-= num[lv+1];
			break;
		}
		case 2:{
			result*= num[lv+1];
			break;
		}
		case 3:{
			result/= num[lv+1];
			break;
		}
		
		}
		return result;
	}

}
