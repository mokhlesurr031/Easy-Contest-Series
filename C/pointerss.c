#include<stdio.h>
int main()
{
    int a=50, *add;
    add = &a;
    printf("Value is: %d and address is %d\n", a, add);
    printf("Get value by address: %d", *add);

}
