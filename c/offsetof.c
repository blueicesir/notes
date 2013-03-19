// 延时如何获取结构体成员相对于结构体的字节偏移量以及结构体成员的大小
// 使用一个特殊的写法，也许看到0这样的指针你就会紧张，0指针就是NULL
// 但编译器可以这样使用，因为它仅仅在编译期进行计算，运行时是没有真实的地址访问的
// 因此是安全的
// 如果你无需自定义就把stddef.h包含进来吧。
// 2013年3月19日

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
