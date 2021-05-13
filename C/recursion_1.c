#include<stdio.h>
void fun1(int n)
{
    if (n>0){
        printf("%d\n", n);
        fun1(n-1);
    }
}

int main()
{
    int x = 3;
    fun1(x);
}



//prints 3, 2, 1

//Steps:
//    1. main func calls fun1
//    2. if int n >0 , print 3
//    3. call fun1 with value -1
//    4. again n>3 so it prints 2
//    and so on



