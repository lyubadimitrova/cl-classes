package elementutils;

public class ElementUtils{
	
	public static <T> T betterElement(T a, T b, TwoElementPredicate<T> p) {
		
		if(p.test(a,b)) {
            return a;
        } else {return b;}
	}
	
	public static void main(String[] args) {
		
		String s = betterElement("java", "python",(x,y) -> x.length() > y.length());
		System.out.println(s);
		
		Integer i = betterElement(20, 5,(x,y) -> x % y == 0);
		System.out.println(i);
		
		Object o = betterElement("java", 8, (x,y) -> x.toString().concat(y.toString()).equals("java8"));
		System.out.println(o);
		
		Integer d = betterElement(20, 5,(x,y) -> x > y ? x % y == 0 : y % x == 0);
		System.out.println(d);
	}
}
