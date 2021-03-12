package blatt02;

public class AnagrammCheck {
	
	private static int getLetterCount (char[] array) {
		int letterCount = 0;
		for(char letter:array) {
			if(letter != ' ') {
				letterCount++;
			}
		}
		return letterCount;
	}
	
	private static void noSpaces (char[] newArray, char[] oldArray) {
		int counter = 0;
		for(int i = 0; i<oldArray.length; i++) {
			if(oldArray[i] != ' ') {
				newArray[counter] = oldArray[i];
				counter++;
			}
		}
	}
		
	public static boolean anagrammCheck(String s1, String s2) {
		char[] s1chars = s1.toLowerCase().toCharArray();
		char[] s2chars = s2.toLowerCase().toCharArray();
		
		int s1LetterCount = getLetterCount(s1chars);
		int s2LetterCount = getLetterCount(s2chars);
		
		if(s1LetterCount != s2LetterCount)
			return false;
		
		char[] newS1 = new char[s1LetterCount];
		char[] newS2 = new char[s2LetterCount];
		
		noSpaces(newS1,s1chars);
		noSpaces(newS2,s1chars);
		
		int[] instances = new int[26];
		for(int i=0; i<newS1.length; i++) {
			instances[newS1[i]-97]++;
			instances[newS2[i]-97]--;
		}
			
		for(int count: instances) {
			if(count!=0)
				return false;
		}
		return true;
	}
	public static void main(String[] args) {
		String s1 = "MY hat stinks             ";
		String s2 = "Stank Smithy";
		
		if(anagrammCheck(s1,s2) == true) 
			System.out.print("The strings '"+s1+"' and '"+s2+"' are anagrams!");
		else 
			System.out.print("The strings '"+s1+"' and '"+s2+"' are NOT anagrams!");		
		
	}
}
