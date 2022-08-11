package hw;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class swea_5215 {
	static int[] score = new int[21];
	static int[] kcal = new int[21];
	static int answer = 0;
	static int n, l;
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int tc = sc.nextInt();
		for (int idx = 1; idx <= tc; ++idx) {
			answer = 0;
			n = sc.nextInt();
			l = sc.nextInt();
			
			for (int i = 0; i < n; ++i)
			{
				score[i] = sc.nextInt();
				kcal[i] = sc.nextInt();
			}
			
			solve(0, 0, 0);
			System.out.println("#" + idx + " " + answer);
		}
		
		sc.close();
	}
    
static void solve(int idx, int sumScore, int sumKcal) {
		if (idx == n) {
			if (answer < sumScore && sumKcal <= l) { //가장 우선시 되는 종료조건이 뭘지 잘 생각하고 문제 풀기!
				answer = sumScore;
			}
			
			return;
		}
		
		solve(idx + 1, sumScore + score[idx], sumKcal + kcal[idx]);
		solve(idx + 1, sumScore, sumKcal);
	}
}
