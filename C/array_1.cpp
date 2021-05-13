#include<iostream>
using namespace std;

int main()
{
    int arr[5], val;
//    arr[3] = 23;
//    cout<<arr[3]<<endl;
//    cout<<arr[34];

    for (int i=0; i<7; i++){
        cin>>val;
        arr[i] = val;
    }
//    cout<<arr[2]<<endl;

    for (int i=0; i<7; i++){
        cout<<&arr[i]<<endl;
    }
    return 0;
}
