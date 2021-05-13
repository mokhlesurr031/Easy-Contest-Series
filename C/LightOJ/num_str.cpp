#include <iostream>
#include<iomanip>

using namespace std;

int main() {

    int test, number;
    string name;
    char ar[4];

    cin>>test;

    while(test>0){
        cin>> number;
        while(number>0){
            getline(cin, name);

//            for (int i=0; i<4; i++){
//                    cout<<name[i]<<endl;
//            }
            cout<<name<<endl;


            number--;
        }


        test--;
    }


    return 0;
}
