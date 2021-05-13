#include<iostream>
using namespace std;

int main()
{
    int A[10] = {3,5,7,9,10,16,19, 25, 34, 50};

    int l = 0, h= 10, mid, num;

    cin>>num;


    while(l<=h)
    {
        mid = (l+h)/2;
        if (num==A[mid])
        {
            cout<<"Index number is: " <<mid<<endl;
            break;
        }
        else if (num < A[mid])
        {
            h = mid-1;
        }
        else if(num>A[mid])
        {
            l = mid+1;
        }

    }
    return 0;
}
