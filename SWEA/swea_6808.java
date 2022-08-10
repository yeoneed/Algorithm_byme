package hw;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class swea_6808 {
	static int[] output = new int[9];
	static int a,b;
	static int compare(int[] output, int[] kyu,int a, int b) {
		int win =0;
		for(int i=0; i<9; i++) {
			if(output[i]<kyu[i]) a++;
			else b++;
		}
		if(a>b) win++;
		return win;
	}
	static int permut(int[] arr, int[] output, boolean[] visited, int depth, int n, int r, int a, int b) {
	    if (depth == r) {
	    	int[] kyu = Arrays.copyOf(arr, 9);
	        return compare(output, kyu,a,b);
	    }
	    for (int i=0; i<n; i++) {
	        if (visited[i] != true) {
	            visited[i] = true;
	            output[depth] = arr[i];
	            permut(arr, output, visited, depth + 1, n, r,a,b);       
	            //output[depth] = 0;
	            visited[i] = false;
	        }
	    }
	    return 999;
	}

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("input/swea_6808.txt"));
		Scanner sc = new Scanner(System.in);
		int t_num = sc.nextInt();
		for(int t=1; t<t_num; t++) {
			int[] tc = new int[9];
			for(int i=0; i<9; i++) {
				tc[i] = sc.nextInt();
			}
			boolean[] visited = new boolean[9];
			int[] kyu = Arrays.copyOf(tc, 9);
			permut(tc, output, visited, 0, 9,9,0,0);
			
			int a = 0,b = 0, x=0, y=0;
			for(int i=0; i<9; i++) {
				if(output[i]<kyu[i]) a+=1;
				else b+=1;
			}
			if(a>b) x+=1;
			else y+=1;
			
			System.out.printf("#%d %d %d%n", t, x,y);
		}
	}

}
