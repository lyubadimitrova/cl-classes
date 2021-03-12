#include "fcpp.hh"

bool istteilbar(int a, int b) {
	return cond( a % b == 0, true, false );
}

int quadrat(int x) {
	return x*x;
}

int potenz(int x, int exp) {
	return cond(exp > 1, cond( istteilbar(exp, 2), quadrat(potenz(x, exp/2)), x*potenz(x, exp-1) ), x);
}

int main() {

	print(potenz(2, 3));
	print(potenz(3, 2));
	print(potenz(5, 1));
	print(potenz(1, 5));
	return 0;
}
