#include<iostream>
using namespace std;


struct day
{
    char new_people[50];
    int total_new_people;


    void charm_your_miss()
    {
        while(true){
            do_math();
        }
        while(true){
            do_smile();
        }
    }

    void do_math()
    {
        int a, b;
        scanf("%d%d", &a, &b);
        printf("%d", a+b);
    }

    void do_smile()
    {
        printf(" :) ");
    }
};


int main()
{
//    struct day d;
//    d.charm_your_miss();
//    d.do_smile();

    day a_bright_day;
    a_bright_day.total_new_people = 0;

    printf("%d", a_bright_day.total_new_people);
    return 0;
}
