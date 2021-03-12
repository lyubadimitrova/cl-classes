package blatt7;

import java.util.*;

public class PersonTester{
	
	public static void main(String[] args) {
		
		//Aufgabe 1
		
		Name n1 = new Name("Abraham", "Lincoln");
		MyDate d1 = new MyDate(12,2,1809);
		Person p1 = new Person(n1, d1);
		
		Name n2 = new Name("Charles", "Darwin");
		MyDate d2 = new MyDate(12,2,1809);
		Person p2 = new Person(n2, d2);
		
		Name n3 = new Name("Alice", "Roosevelt", "Longworth");
		MyDate d3 = new MyDate(12,2,1884);
		Person p3 = new Person(n3, d3);
		
		Name n4 = new Name("Arthur", "Conan", "Doyle");
		MyDate d4 = new MyDate(22,5,1859);
		Person p4 = new Person(n4, d4);
		
		Name n5 = new Name("Jane", "Austen");
		MyDate d5 = new MyDate(16,12,1775);
		Person p5 = new Person(n5, d5);
		
		Name n6 = new Name("Simone", "de", "Beauvoir");
		MyDate d6 = new MyDate(9,1,1908);
		Person p6 = new Person(n6, d6);
		
		
		//Aufgabe 2
		
		List<Person> people = new ArrayList<Person>();
		
		people.add(p1);
		people.add(p2);
		people.add(p3);
		people.add(p4);
		people.add(p5);
		people.add(p6);
		
		
		Map<MyDate,HashSet<Person>> map = new TreeMap<MyDate,HashSet<Person>>();
		  
		for(int i = 0; i < people.size(); i++) {
			
			MyDate key = people.get(i).getBirthday();
			HashSet<Person> hs = new HashSet<Person>();
			hs.add(people.get(i));
			
			for(int j = i + 1; j < people.size(); j++) {
				if(key.equals((Object)people.get(j).getBirthday())) {
					hs.add(people.get(j));
					people.remove(j);
					j--;
				}
			}
			map.put(key, hs);
		}
		
		//Aufgabe 3
		
		Set<Map.Entry<MyDate,HashSet<Person>>> dates = map.entrySet();
		Iterator <Map.Entry<MyDate,HashSet<Person>>> it = dates.iterator();
		 
		
		while(it.hasNext()) {
			Map.Entry<MyDate,HashSet<Person>> me = (Map.Entry<MyDate,HashSet<Person>>)it.next();
			System.out.println("Born on date " + me.getKey() + ":");
			Iterator<Person> it2 = map.get(me.getKey()).iterator();
			while(it2.hasNext()) {
				System.out.println(it2.next().getName());
			}
			System.out.println();
		}
		
		System.out.println("------------------\n\n");
		//Aufgabe 4
		
		List<Person> people2 = new ArrayList<Person>();
		
		people2.add(p1);
		people2.add(p2);
		people2.add(p3);
		people2.add(p4);
		people2.add(p5);
		people2.add(p6);
		
		Map<MyDate,TreeSet<Person>> map2 = new TreeMap<MyDate,TreeSet<Person>>();
		
		for(int i = 0; i < people2.size() ; i++) {
			
			MyDate birthday = people2.get(i).getBirthday();
			int month = birthday.getMonth();
			int day = birthday.getDay();
			
			TreeSet<Person> ts = new TreeSet<Person>();
			ts.add(people2.get(i));
			
			for(int j = i + 1; j < people2.size(); j++) {
				MyDate otherBirthday = people2.get(j).getBirthday();
				if(otherBirthday.getMonth() == month && otherBirthday.getDay() == day) {
					ts.add(people2.get(j));
					people2.remove(j);
					j--;
				}
			}
			map2.put(birthday, ts);
		}
		
		
		Set<Map.Entry<MyDate,TreeSet<Person>>> dates2 = map2.entrySet();
		Iterator <Map.Entry<MyDate,TreeSet<Person>>> it2 = dates2.iterator();
		 
		
		while(it2.hasNext()) {
			Map.Entry<MyDate,TreeSet<Person>> me = (Map.Entry<MyDate,TreeSet<Person>>)it2.next();
			System.out.println("Birthday on same day:");
			Iterator<Person> it3 = map2.get(me.getKey()).iterator();
			while(it3.hasNext()) {
				System.out.println(it3.next().getName());
			}
			System.out.println();
		}
	}

}
