#include<iostream>
using namespace std;

int main()
{
    int groups, members, total=0, div;

    cin>>groups;

    for (int i=0; i<groups; i++){
        cin>>members;
        total += members;
    }
    div = total%4;
    int result = total/4;

    if (div>0)result++;

    cout<<result<<endl;
}
