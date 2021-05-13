#include<iostream>

using namespace std;

int main()
{
    int *A = new int[5];
//    int A[5];
//    int A = {1,2,3,4,5};
    A[0] = 1;
    A[1] = 2;
    A[2] = 3;
    A[3] = 4;
    A[4] = 5;

//    printf("%d", A[0]+A[4]);

//    for (int i=0; i<5; i++){
//        printf("Okay: %d\n", A[i]+A[i+1]);
//    }

    printf("%d", A[4])

    delete[] A;
}
