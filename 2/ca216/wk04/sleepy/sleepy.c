#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/types.h>

pid_t getpid(void);
unsigned int sleep(unsigned int seconds);
void sighandler(int signum);

int main(int argc, char* argv[]) {
    signal(SIGINT, sighandler);

    int n = atoi(argv[1]);
    for (int i = 0; i < n; i++) {
        printf("%d\n", getpid());
        int rem = sleep(5);
        printf("%d\n", rem);
    }

    return 0;    
}

void sighandler(int signum) {
    printf("Recieved a signal %d\n", signum);
}