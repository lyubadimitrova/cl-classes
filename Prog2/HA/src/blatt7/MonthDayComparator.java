package blatt7;

import java.util.*;

public class MonthDayComparator implements Comparator<MyDate>{
	
	@Override
	public int compare(MyDate date1, MyDate date2) {
		
		Integer m1 = new Integer(date1.getMonth());
		Integer m2 = new Integer(date2.getMonth());
		int monthComp = m1.compareTo(m2);
		if(monthComp != 0) 
			return monthComp;
		
		Integer d1 = new Integer(date1.getDay());
		Integer d2 = new Integer(date2.getDay());
		int dayComp = d1.compareTo(d2);
		if(dayComp != 0) 
			return dayComp;
		
		Integer y1 = new Integer(date1.getYear());
		Integer y2 = new Integer(date2.getYear());
		return y1.compareTo(y2);
	}

}
