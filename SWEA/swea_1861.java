package hw;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class swea_1861 {
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	
	static boolean valid(int n, int x, int y) {
		return x>=0 && x<n && y>=0 && y<n;
	}
	
	static int dfs(int[][] arr, int n, int start_x, int start_y, int cnt) {
		for(int i=0; i<4; i++) {
			int nx = start_x + dx[i];
			int ny = start_y + dy[i];
			if(valid(n,nx,ny)==true && arr[start_x][start_y]+1==arr[nx][ny]) {
				cnt++;
				cnt = dfs(arr, n, nx, ny, cnt);
			}
		}
		return cnt;
	}
	
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input/swea_1861.txt"));
		Scanner sc = new Scanner(System.in);
		int t_num = sc.nextInt();
		for(int t=1; t<=t_num; t++) { //테스트케이스 수 입력
			int n = sc.nextInt();
			int[][] arr = new int[n][n];
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					arr[i][j]= sc.nextInt(); //배열 인자 받아오기
				} 
			}
			
			int max_cnt = 1;
			int cnt;
			int[][] visited = new int[n][n];
			int min_val = (int)1e9;
			StringBuilder sb= new StringBuilder();
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					//int[][] visited = new int[n][n];
					cnt = dfs(arr, n, i,j, 1);
					if(cnt>max_cnt) {
						max_cnt=cnt;
						sb.setLength(0); //가장 큰 값이 바뀌면 해당 배열 값도 초기화하기 
						sb.append(arr[i][j] +" ");
					}
					else if(cnt==max_cnt) {
						sb.append(arr[i][j] + " ");
					}
				} 
			}
			
			String ans1 = sb.toString();
			String[] ans = ans1.split(" ");
			for(int i=0; i<ans.length; i++) {
				if(min_val>Integer.parseInt(ans[i])) {
					min_val = Integer.parseInt(ans[i]);
				}
			}
			System.out.printf("#%d %d %d%n", t, min_val, max_cnt);
		}
	}

}
