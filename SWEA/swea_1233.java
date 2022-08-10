package hw;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class swea_1233 {

	public static void main(String[] args) throws IOException{

		System.setIn(new FileInputStream("input/swea_1233.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		for(int t=1;t<=10;t++) {
			
			int n = Integer.parseInt(br.readLine());
			int answer = 1;
			
			for(int node=1;node<=n;node++) {

				String[] arr = br.readLine().split(" ");
				
				//리프 노드가 아니고 숫자가 들어있거나 리프노드면서 연산자가 들어있는 경우는 0 반환
				if(arr.length>=3 && arr[1].charAt(0) >='0' || arr.length==2 && arr[1].charAt(0)<'0') {
					for(int i=node+1;i<=n;i++) {
						br.readLine();
					}
					answer = 0;
					break;
				}
				
			}
			sb.append("#").append(t).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}

}
