#include<stdio.h>
struct Reactangle{
    int length;
    int breadth;
};

int main()

{

    struct Reactangle r={10,5};
    struct Reactangle *p=&r;

    printf("%d %d\n", r.length, r.breadth);

    printf("Address: %d\n", p);

    printf("Access by address: %d\n", (*p).length);
    printf("Access by address simple way: %d\n", p->length);
}
