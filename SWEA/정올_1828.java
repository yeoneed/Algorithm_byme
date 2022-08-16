package hw;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Comparator;

public class 정올_1828 {
	static int[][] arr;
	static int max;
	static int cnt;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()); //한 줄로 입력받은거 st로 다시 입력
		int n = Integer.parseInt(st.nextToken());
		arr = new int[n][2];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			arr[i][0] = start;
			arr[i][1] = end;
			
		}

		cnt = 1;
		compare(arr); //2차원 배열 최저값 기준 내림차순 정렬
		max = arr[0][0];
		
//		for(int i=0; i<n; i++) {
//			System.out.print(arr[i][0]+ " ");
//			System.out.println(arr[i][1]);
//		}
		
		for(int i=0; i<n; i++) {
			if(max>arr[i][1]) {
				max = arr[i][0];
				cnt++;
			}
		}
		
		System.out.println(cnt);
		}
	
	static void compare(int[][] arr) {
		
		Arrays.sort(arr, new Comparator<int[]>() {
		    @Override
			public int compare(int[] o1, int[] o2) {
		    	 return o1[0] == o2[0] ? o2[1] - o1[1] : o2[0] - o1[0]; //0번째 인덱스 위치 같을 경우 1열로 비교, 아니면 내림차순 정렬
	           }
	        });
	}
	
	

}
