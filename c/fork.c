#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main()
{
    pid_t pid1;
    pid_t pid2;

    pid1=fork();
    pid2=fork();
    printf("pid1:%d,pid2:%d\n",pid1,pid2);
}
