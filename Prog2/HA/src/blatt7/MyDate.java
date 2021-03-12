package blatt7;

import java.util.*;
import blatt7.MonthDayComparator;

public class MyDate implements Comparable<Object> {
	
	//instance variables
	private int day;
	private int month;
	private int year;
	
	//constructor
	public MyDate(int day, int month, int year) {
		
		this.year = year;
		if(month > 12 || month < 1) {
			System.err.print("Invalid month!");
		}
		else if(day > getMonthLen(month, year) || day < 1) {
			System.err.print("Invalid day for this month!");
		}
		this.month = month;
		this.day = day;
	}
	
	private int getMonthLen (int month, int year) {
		int monthLen = 0;
		switch(month) {
			case 1: case 3: case 5: case 7: case 8: case 10: case 12: monthLen = 31;
			case 4: case 6: case 9: case 11: monthLen = 30;
			case 2: if(isLeap(year)) {
						monthLen = 29;
					} else { monthLen = 28; }
		}
		return monthLen;
	}
	
	private boolean isLeap(int year) {
		if ( (year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0) ) {
			return true;
		} else {return false;}
	}
	
	public int getDay() {
		return this.day;
	}
	
	public int getMonth() {
		return this.month;
	}
	
	public int getYear() {
		return this.year;
	}
	
	@Override
	public String toString() {
		return String.format("%04d-%02d-%02d", year, month, day);
	}
	
	@Override
	public boolean equals(Object other) {
		
		if(other == null) 
			return false;
		
		MyDate otherDate = (MyDate)other;
		
		if(this.year != otherDate.year) 
			return false;
		
		if(this.month != otherDate.month) 
			return false;
		
		if(this.day != otherDate.day) 
			return false;
		
		return true;	
	}
	
	@Override
	public int hashCode() {
		
        int result = 0;
        result = this.day * 3 + this.month * 5 + this.year * 7;
        return result;
    }
	
	@Override
	public int compareTo(Object other) {
		
		MyDate otherDate = (MyDate)other;
		
		Integer y1 = new Integer(this.year);
		Integer y2 = new Integer(otherDate.year);
		int yearComp = y1.compareTo(y2);
		if(yearComp != 0)
			return yearComp;
		
		Integer m1 = new Integer(this.month);
		Integer m2 = new Integer(otherDate.month);
		int monthComp = m1.compareTo(m2);
		if(monthComp != 0) 
			return monthComp;
		
		Integer d1 = new Integer(this.day);
		Integer d2 = new Integer(otherDate.day);
		return d1.compareTo(d2);
	}
	
	public static void main(String[] args) {
		
		MyDate a = new MyDate(29,2,1996);
		MyDate b = new MyDate(14,3,1996);
		MyDate c = new MyDate(18,2,2003);
		MyDate d = new MyDate(9,1,1998);
		
		List<MyDate> dates = new ArrayList<MyDate>();
		dates.add(a);
		dates.add(b);
		dates.add(c);
		dates.add(d);
		Collections.sort(dates);
		System.out.println("Dates sorted ascending: " + dates);
		Collections.sort(dates, new MonthDayComparator());
		System.out.println("Dates sorted by month + day: " + dates);
			
	}
}
