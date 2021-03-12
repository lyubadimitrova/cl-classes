#include "fcpp.hh"

int main() {
	int x = enter_int("Please enter a number x=");
	int y = enter_int("Please enter a number y=");
	print(cond(x > y, "x > y", cond(x < y, "x < y", "x = y")));
	return 0;
}