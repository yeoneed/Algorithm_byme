package hw;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class hwalgo09_서울_12반_김수연 {

	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("input/boj_2563.txt"));
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int cnt=0;
		int[][] arr = new int[101][101];
		for(int t=0; t<n; t++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			for(int i=x; i<x+10; i++) {
				for(int j=y; j<y+10; j++) {
					arr[i][j]=1;
				}
			}
		}
		for(int i=0; i<=100; i++) {
			for(int j =0;j<=100; j++) {
				if(arr[i][j]==1) {
					cnt++;
				}
			}
		}

		System.out.println(cnt);
		}
		
	}

	