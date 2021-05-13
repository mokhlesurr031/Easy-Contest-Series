#include<stdio.h>
struct Reactangle{
    int length;
    int breadth;
};
int main(){
//    struct Reactangle r={4,5};
    struct Reactangle r;
//    r.length=3;
//    r.breadth = 4;
    scanf("%d%d", &r.length, &r.breadth);
    printf("Length: %d, Breadth: %d\n", r.length, r.breadth);

    printf("Area of rectangle is: %d", r.length*r.breadth);

}
