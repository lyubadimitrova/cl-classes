package blatt7;

public class Name implements Comparable<Object>{
	
	//instance variables
	
	private String firstName;
	private String lastName;
	private String middleName;
	
	//Getters and setters
	
	public String getFirstName() {
		return this.firstName;
	}
	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}
	public String getLastName() {
		return this.lastName;
	}
	public void setLastName(String lastName) {
		this.lastName = lastName;
	}
	public String getMiddleName() {
		return this.middleName;
	}
	public void setMiddleName(String middleName) {
		this.middleName = middleName;
	}
	
	//Constructors
	
	public Name(String firstName, String lastName) {
		setFirstName(firstName);
		setLastName(lastName);
	}
	
	public Name(String firstName, String middleName, String lastName) {
		this(firstName, lastName);
		setMiddleName(middleName);	
	}
	
	
	@Override
	public String toString() {
		if(middleName != null)
			return String.format("%s %s %s", firstName, middleName, lastName);
		else 
			return String.format("%s %s", firstName, lastName);
	}


	@Override
	public boolean equals(Object other) {
		
		if(other == null) 
			return false;
		
		if(this == other)
			return true;
		
		Name otherPerson = (Name)other;
		
		if(!this.firstName.equals(otherPerson.firstName)) 
			return false;
		
		if(!this.middleName.equals(otherPerson.middleName)) 
			return false;
		
		if(!this.lastName.equals(otherPerson.lastName)) 
			return false;
		
		return true;	
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((firstName == null) ? 0 : firstName.hashCode());
		result = prime * result + ((lastName == null) ? 0 : lastName.hashCode());
		result = prime * result + ((middleName == null) ? 0 : middleName.hashCode());
		return result;
	}
	
	@Override
	public int compareTo(Object other) {
		
		Name otherPerson = (Name)other;
		
		int lastNameComp = this.lastName.compareTo(otherPerson.lastName);
		if(lastNameComp != 0)
			return lastNameComp;

		int firstNameComp = this.firstName.compareTo(otherPerson.firstName);
		if(firstNameComp != 0)
			return firstNameComp;
		
		if(this.middleName != null && otherPerson.middleName != null)
			return this.middleName.compareTo(otherPerson.middleName);
		
		return 0;
			
	}
	
	public static void main(String[] args) {
		
		/*
		Name a = new Name("Arthur", "Conan", "Doyle");
		Name b = new Name("Arthur", "Conan", "Doyle");
		Name c = new Name("Jane", "Austen");
		Name d = new Name("Arthur","Conan");
		
		System.out.println(a.hashCode());
		System.out.println(b.hashCode());
		System.out.println(c.hashCode());

		System.out.println(a.equals(b));
		System.out.println(a.equals(c));
		System.out.println(a.equals(d));
		
		System.out.println(a.compareTo(c));
		System.out.println(a.compareTo(d));
		System.out.println(c.compareTo(d));
		*/
		
	}
}
