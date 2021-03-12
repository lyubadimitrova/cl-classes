#include "fcpp.hh"

bool istteilbar(int a, int b) {
	return cond( a % b == 0, true, false );
}

int summe(int b, int n) {
	return cond( b < 1, 0, cond(istteilbar(n, b), b, 0) + summe(b-1, n) );
}

bool vollkommen(int zahl) {
	return cond(zahl == summe(zahl/2, zahl), true, false);
}


int main() {

	print(cond(vollkommen(6), "6 is a perfect number", "6 is not a perfect number"));
	print(cond(vollkommen(8), "8 is a perfect number", "8 is not a perfect number"));
	print(cond(vollkommen(28), "28 is a perfect number", "28 is not a perfect number"));
	print(cond(vollkommen(32), "32 is a perfect number", "32 is not a perfect number"));
	return 0;
}





