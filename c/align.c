#include<stdio.h>
#define OFFSET(s,m) (size_t)&(((s *)0)->m)

#pragma pack(1)
typedef struct
{
    int a;
    float b;
    char c;
    double d;
    int *pa;
    char *pc;
}Sta;
#pragma pack()

int main()
{
    printf("a_=%d\n",OFFSET(Sta,a));
    printf("b_=%d\n",OFFSET(Sta,b));
    printf("c_=%d\n",OFFSET(Sta,c));
    printf("d_=%d\n",OFFSET(Sta,d));
    printf("pa_=%d\n",OFFSET(Sta,pa));
    printf("Pc_=%d\n",OFFSET(Sta,pc));
    return 0;
}
