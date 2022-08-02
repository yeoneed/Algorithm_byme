package ex_0802;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.StringTokenizer;

public class swea_2805 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		System.setIn(new FileInputStream("input/2805.txt"));
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int ti = 1; ti<=t; ti++) {
			int n = sc.nextInt();
			char[][] tc = new char[n][n];
			int[][] arr = new int[n][n];
			
			for(int i=0; i<n; i++) {
					tc[i] = sc.next().toCharArray();
			}
			
			for(int a=0; a<n; a++) {
				for(int b=0; b<n; b++) {
					arr[a][b]= tc[a][b]-'0';
				}
			}
			
			int mid = n/2;
			int sum = 0;
			for(int x=0; x<n; x++) {
					if(x<=mid) {
						for(int k=mid-x; k<=mid+x; k++) {
							sum+=arr[x][k];
						}
					}
					else {
						for(int k=mid-(2*mid-x); k<=mid+(2*mid-x); k++) {
							sum+=arr[x][k];
						}
					}
				}
			System.out.printf("#%d %d%n", ti, sum);
		}
	}

}
