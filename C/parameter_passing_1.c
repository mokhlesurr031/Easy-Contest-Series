//
//3 types:
//    1. pass by value
//    2. pass by address
//    3. pass by method/ call by reference



//pass by value/call by value

#include<stdio.h>

int main(){
    int swap(x, y)
    {
        int temp;
        temp = x;
        x = y;
        y=temp;
        printf("%d %d", x, y);
    }

    int a=20, b=10;

    swap(a, b);

//    printf("%d %d", a, b);


    return 0;
}
