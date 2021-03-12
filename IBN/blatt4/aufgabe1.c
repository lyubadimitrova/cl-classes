#include<stdio.h>
#include<string.h>
#include<pthread.h>
#include<stdlib.h>
#include<unistd.h>
#include<stdbool.h>

pthread_mutex_t lock;
int* counters;

void* thread_code(void *arg)
{   
    while(true) {
        pthread_mutex_lock(&lock);

        int id = *((int*) arg);
        counters[id] += 1;

        pthread_mutex_unlock(&lock);
    }
    return NULL;
}

int main(int argc, char *argv[])
{   
    long num_threads = strtol(argv[1], NULL, 10);
    counters = malloc(num_threads*sizeof(int*));

    pthread_t tid[num_threads];
    int err;

    if (pthread_mutex_init(&lock, NULL) != 0)
    {
        printf("\n mutex init failed\n");
        return 1;
    }

    //pthread_mutex_lock(&lock);     // locking the mutex for the creation causes all-0 counters?
    for (int i=0; i < num_threads; i++)
    {
        err = pthread_create(&(tid[i]), NULL, thread_code, (void *) &i);
        printf("Creating thread %d\n", i);
        if (err != 0)
            printf("\ncan't create thread :[%s]", strerror(err));
    }

    sleep(1);

    //pthread_mutex_unlock(&lock);

    sleep(3);
    
    for (int i=0; i < num_threads; i++)    {
        printf("Thread %d got mutex %d times\n", i, counters[i]);
        counters[i] = 0;
    }

    pthread_mutex_destroy(&lock);

    free(counters);

    return 0;
}