package elementutils;

@FunctionalInterface
public interface TwoElementPredicate<T> {
	
	public boolean test(T a, T b) ;
}
