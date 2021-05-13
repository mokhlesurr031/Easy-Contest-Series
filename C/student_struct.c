#include<stdio.h>

struct Students{
    int roll;
    char name[25];
    char dept[20];
    char address[50];
};

int main()
{
    struct Students stu;
//    struct Students stu = {1, 'Mahin', 'CSE', 'Dhaka'};


//    stu.roll = 24;
//    stu.name= 2;
//    stu.dept = "CSE";
//    stu.address = "Dhaka";
    scanf("%s", stu.name);

    printf("Name: %s",stu.name);

}
