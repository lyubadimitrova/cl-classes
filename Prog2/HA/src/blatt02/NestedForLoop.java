package blatt02;

public class NestedForLoop {
	
	public static void main(String[] args) {
		
		 int[] arr = new int[12];                 
		 int nLast = 0;
		 for(int i = 0; i < 12; i++) {
			for(int n = nLast + 1; n <= 56; n++) {
				if(n/10 + n%10 > 9) {
					arr[i] = n;
					nLast = n;
					break;
				}
			}
		  }
		 for (int elm: arr) {
			 System.out.println(elm);
		 }
	}
}
