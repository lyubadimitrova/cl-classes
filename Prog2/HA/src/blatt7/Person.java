package blatt7;

public class Person implements Comparable<Object>{
	
	private Name name;
	private MyDate birthday;
	
	public Person(Name name, MyDate birthday) {
		this.name = name;
		this.birthday = birthday;
	}
	
	@Override
	public String toString() {
		return String.format("Name: %-30s Birthday: %10s", name, birthday);
	}
	
	public Name getName() {
		return this.name;
	}
	
	public MyDate getBirthday() {
		return this.birthday;
	}
	
	
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((birthday == null) ? 0 : birthday.hashCode());
		result = prime * result + ((name == null) ? 0 : name.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		
		if (this == obj)
			return true;
		
		if (obj == null)
			return false;
		
		Person other = (Person)obj;
		
		if(!this.name.equals(other.name)) 
			return false;
		
		if(!this.birthday.equals(other.birthday)) 
			return false;
		
		return true;
	}

	@Override
	public int compareTo(Object other) {
		
		Person otherPerson = (Person)other;

		int nameComp = this.name.compareTo(otherPerson.name);
		if(nameComp != 0)
			return nameComp;
		
		return this.birthday.compareTo(otherPerson.birthday);
			
	}
	
	public static void main(String[] args) {
		
		Name n1 = new Name("Arthur", "Conan", "Doyle");
		MyDate d1 = new MyDate(22,5,1859);
		Person p1 = new Person(n1, d1);
		
		Name n2 = new Name("Jane", "Austen");
		MyDate d2 = new MyDate(16,12,1775);
		Person p2 = new Person(n2, d2);
		
		System.out.println(p1);
		System.out.println(p2);
		
		System.out.println(p1.compareTo(p2));
	}
	
}
