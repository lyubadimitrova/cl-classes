#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#define NUM_THREADS 500000

void *TaskCode(void *argument) {
    int tid;
    tid = *((int*) argument);
    printf("It's me, dude! I am number %d!\n", tid);
    return NULL;
}

int main(int argc, char *argv[]) {
    pthread_t threads[NUM_THREADS];
    int thread_args[NUM_THREADS];
    int rc;
    int i;
    
    for(i = 0; i < NUM_THREADS; ++i) { 
        thread_args[i] = i;
        printf("In main: creating thread %d\n", i);
        //create all threads:
        rc = pthread_create(&threads[i], NULL, TaskCode, (void *) &thread_args[i]);
        assert(0 == rc);
        rc = pthread_join(threads[i], NULL); //wait for the thread to complete
        assert(0 == rc);
    }
    exit(EXIT_SUCCESS);
}