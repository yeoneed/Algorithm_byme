package ex_0802;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class swea_1208_2 {

	public static void main(String[] args) throws FileNotFoundException {
		// TODO Auto-generated method stub
		System.setIn(new FileInputStream("input/1208.txt"));
		Scanner sc = new Scanner(System.in);
		//BufferedReader in 
		for(int i=1; i<=10;i++) {
			int n = sc.nextInt();
			int[] tc = new int[100];
//			for(int i2=0; i2<100; i2++) {
//				tc[i2]= sc.nextInt();
//			}
			sc.nextLine();
			
			StringTokenizer st = new StringTokenizer(sc.nextLine(), " ");
			for(int j=0; j<100; j++) {
				tc[j] = Integer.parseInt(st.nextToken());
			} //배열 인자 입력
			
			for(int idx=0; idx<n; idx++) {
				Arrays.sort(tc);
				tc[0]++;
				tc[99]--;
			}
			Arrays.sort(tc);
			System.out.printf("#%d %d%n", i, tc[99]-tc[0]);
	}

}
}
