package ex_0802;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class swea_1210 {

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input/1210.txt"));
		Scanner sc = new Scanner(System.in);
		for(int t=1; t<=10; t++) {
			int n = sc.nextInt();
			int[][] tc = new int[100][100];
			int row=0, col = 0;

			for(int i=0; i<100; i++) {
				for(int j=0; j<100; j++) {
					tc[i][j] = sc.nextInt();
					if(tc[i][j]==2) {
						row=i;
						col=j;
					}
				} //배열 인자 입력
			}
			//반복문 입력(큐 사용안하면 역순탐색이 필요함)
			while(row!=0) {
				if(col-1>=0 && tc[row][col-1]==1) {
					do {
						--col;
					}while(col-1>=0 && tc[row][col-1]==1);
				}
				else if(col+1<100 && tc[row][col+1]==1) {
					do {
						++col;
					}while(col+1<100 && tc[row][col+1]==1);
				}	
				--row;
			}
			
			System.out.printf("#%d %d%n", t, col);
		}

	}

}
