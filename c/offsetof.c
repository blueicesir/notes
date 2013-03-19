#include<stdio.h>
#include<stdlib.h>
// #include<stddef.h>

#define offsetof(s,m) (size_t)&(((s*)0)->m)
#define sizeofmem(s,m) (size_t)sizeof((((s*)0)->m))

struct __node__ {
    unsigned char Type;
    unsigned char nLen;
    char* pString;
};

int main()
{
    printf("Hello World!\n");
    printf("sizeof(__node__)=%d\n",sizeof(struct __node__));
    printf("offsetof(struct __node__,Type)=%d,size=%d\n",offsetof(struct __node__,Type),sizeofmem(struct __node__,Type));
    printf("offsetof(struct __node__,nLen)=%d,size=%d\n",offsetof(struct __node__,nLen),sizeofmem(struct __node__,nLen));
    printf("offsetof(struct __node__,pString)=%d,size=%d\n",offsetof(struct __node__,pString),sizeofmem(struct __node__,pString));
}
