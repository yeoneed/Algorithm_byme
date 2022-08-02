package ws_0801;

import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
 
public class boj_1244 {
	public static int[] boy(int n, int[] tc) {
		for(int i=0; i<tc.length; i++) {
			if((i+1)%n==0) tc[i]^=1;
		}
		return tc;
	}
	
	public static int[] girl(int n, int[] tc) {
		int k =1;
		int[] result = tc;
		while(n-k>=0 && n+k<tc.length) {
			if(tc[n-k]==tc[n+k]) k+=1;
			else break;
		}
		result = xor(n,k-1,tc);
		return result;
	}
	
	public static int[] xor(int n, int k, int[] tc) {
		for(int i=n-k; i<=n+k; i++) {
			tc[i]^=1;
		}
		return tc;
	}
	
	public static void main(String[] args) throws FileNotFoundException {
		System.setIn(new FileInputStream("input.txt"));
		Scanner sc= new Scanner(System.in);
		int n= sc.nextInt();
		int[] tc = new int[n];
		for(int i=0; i<n; i++) {
			tc[i] = sc.nextInt();
		}
		int num = sc.nextInt();
		
		for(int i2=0; i2<num; i2++) {
			int type = sc.nextInt();
			int start = sc.nextInt();
			if(type==1) tc = boy(start, tc);
			else tc = girl(start-1, tc);
		}
		for(int i3=0; i3<tc.length; i3++) {
			System.out.printf("%d ", tc[i3]);
			if(i3!=0 && ((i3+1)%20==0)) System.out.println();
		
		}
	}

}
    