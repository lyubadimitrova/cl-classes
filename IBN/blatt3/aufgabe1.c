#include<stdio.h> 
#include<stdlib.h> 
#include<unistd.h> 
#include<sys/types.h> 
#include<string.h> 
#include<sys/wait.h> 

#define   MAX_COUNT  200
#define   BUF_SIZE   100

int main()
{
	// 2 pipes
	// first pipe to send input string from parent to child process
	// second pipe to send reversed string from child to parent process
	int fd1[2];
	int fd2[2];
	
	
	char input[] = "Hello World";
	// create the child process B of parent process A
	int pid;
	
	if (pipe(fd1) ==-1){
		fprintf(stderr, "first Pipe Failed");
		return 1;
	}
	
	if (pipe(fd2)==-1){
		fprintf(stderr, "second Pipe Failed");
		return 1;
	}
	pid = fork();
	
	if (pid < 0){
		fprintf(stderr, "fork failed");
		return 1;
	}
	//parent
	else if (pid > 0){
		char output[strlen(input)+1];
		
		close(fd1[0]); // Close reading ends of pipe 1
		
		//Write input string and close writing end of pipe 1
		write(fd1[1], input, strlen(input)+1);
		close(fd1[1]);
		
		// Wait for child to send a string
		wait(NULL);
		
		close(fd2[1]); //Close writing end of pipe 2
		
		// Read string form child, print and close reading end of pipe 2
		read(fd2[0], output, strlen(input)+1);
		printf("output: %s\n", output);
		close(fd2[0]); 
	}
	
	// child
	else if (pid == 0){
		close(fd1[1]); // Close writing ends of pipe 1
		
		// Read a string using pipe 1
		char output[strlen(input)+1];
		read(fd1[0], input, strlen(input)+1);
		
		// reversed
		int i;
		int k = 0;
		
		for (i=strlen(input)-1; i>=0; i--){        
			output[k++] = input[i];
        
        }
		
		// Close both reading ends
		close(fd1[0]);
		close(fd2[0]);
		
		// Write output in pipe 2 and close writing end of pipe 2
		write(fd2[1], output, strlen(output)+1);
		close(fd2[1]);
		exit(0);
	}
}
	
