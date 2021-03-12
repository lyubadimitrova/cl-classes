#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char *argv[]) {   
	int* counters = malloc(3*sizeof(*counters));

	for (int i=0; i<3; i++) {
		printf("%d\n", counters[i]);
	}

	counters[1] = 5;
	counters[2] = -1;

	for (int i=0; i<3; i++) {
		printf("%d\n", counters[i]);
	}

	counters = malloc(3*sizeof(*counters));		

	counters[1] = 6	;
	for (int i=0; i<3; i++) {
		printf("%d\n", counters[i]);
	}

}