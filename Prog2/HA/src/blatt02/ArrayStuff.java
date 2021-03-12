package blatt02;

public class ArrayStuff {
	public static void main(String[] args) {
		
		 int sum = 0;
	     int [] numbers = new int[100];         //creates a new int array with 100 elements

	     for (int i=0; i < 100; i++){           //iterates over the new array to fill it with the numbers 0-99
	    	 numbers[i]=i;
	     }

	     for (int n : numbers){
	    	 
	    	 sum += n;						  //sums all elements of the array numbers
	    	 
	         if (n%10==0){
	        	 System.out.println(n);       //uses the out-stream to output all array elements divisible by 10
	         }
	         if (n%5==0 || n%3==0){
	             System.err.println(n);       //uses the error-stream to output all array elements divisible by 3, 5, or both
	         }
	     }

	     System.out.println(sum);

	}
}
