#include  <stdio.h>
#include  <string.h>
#include  <sys/types.h>
#include <stdio.h>
#include <unistd.h>

#define   MAX_COUNT  200
#define   BUF_SIZE   100

int main(int argc, char* argv[]) {

	pid_t pid;
	char buf[BUF_SIZE];
	int i=0;
	sprintf(buf, "Beginning: pid %d i %d \n", getpid(), i);
	write(1, buf, strlen(buf));
	
	pid = fork();
	if (pid!=0) {	
		i++;
		sprintf(buf, "First if: parent_pid %d fork_value %d i %d \n", getpid(), pid, i);
		write(1, buf, strlen(buf));
	}
	sprintf(buf, "Between if1 and if2: pid %d i %d \n", getpid(), i);
	write(1, buf, strlen(buf));
	if (i!=0) {
		sprintf(buf, "Second if before fork: pid %d i %d \n", getpid(), i);
		write(1, buf, strlen(buf));
		pid = fork();
		sprintf(buf, "Second if after fork: parent_pid %d fork_value %d i %d \n", getpid(), pid, i);
		write(1, buf, strlen(buf));
	}
	sprintf(buf, "Between if2 and if3: pid %d i %d \n", getpid(), i);
	write(1, buf, strlen(buf));
	pid = fork();
	if (pid!=0||i!=0) {
		i++;
		sprintf(buf, "Third if: parent_pid %d fork_value %d i %d \n", getpid(), pid, i);
		write(1, buf, strlen(buf));
	}
	sprintf(buf, "Between if3 and if4: pid %d i %d \n", getpid(), i);
	write(1, buf, strlen(buf));
	pid = fork();
	if (pid==0&&i==0) {
		sprintf(buf, "Fourth if before fork: parent_pid %d fork_value %d i %d \n", getpid(), pid, i);
		write(1, buf, strlen(buf));
		pid = fork();
		sprintf(buf, "Fourth if after fork: parent_pid %d fork_value %d i %d \n", getpid(), pid, i);
		write(1, buf, strlen(buf));
	}

	sprintf(buf, "Exiting: pid %d i %d \n", getpid(), i);
	write(1, buf, strlen(buf));

	//printf("%d\n", i);
	return 0;
}