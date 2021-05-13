
#include<iostream>
using namespace std;

int main()
{
    int num,expected_num, ind, flag=0;

    cout<<"Expected num: ";
    cin>>expected_num;

    cout<<"Array elements: ";
    cin>>num;

    int A[num];

//    cout<<sizeof(A);

    cout<<"Indexes: ";
    for (int i=0; i<num; i++){
        cin>>ind;
        A[i] = ind;
    }


    int low=0, high=num, mid;

    while(low<=high)
    {
        mid = (low+high)/2;
        if (expected_num == A[mid])
        {
            cout<<"Found"<<endl;
            cout<<"Index: "<< A[mid];
            flag+=1;
            break;
        }
        if (expected_num>A[mid])
        {
            low = mid+1;
        }
        if (expected_num < A[mid])
        {
            high = mid-1;
        }
    }

    if(flag==0)
    {
        cout<<"Not found"<<endl;
    }

    return 0;





}
