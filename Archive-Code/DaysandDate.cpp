#include <iostream>
#include<string.h>
using namespace std;

int T,date;
string input_days;
string name_days[7] = {"mon","tues","wed","thurs","fri","sat","sun"};


int main(){
    cin >> T;
    int days[T][7];
    for (int s = 0;s<T;s++){
        cin >> date >> input_days;
        if (date == 28){
            for (int a = 0;a<7;a++){
                days[s][a] = 4;
            }
        }
        else if (date == 29) {
            for (int l=0;l<7;l++){
                if (input_days == name_days[l]){
                    for (int k=0;k<7;k++){
                        if (k==l){
                            days[s][k] = 5;
                        }
                        else {
                            days[s][k] = 4;
                        }
                    }
                }
            }
        }
        else if (date == 30) {
            for (int l=0;l<7;l++){
                if (input_days == name_days[l]){
                    for (int k=0;k<7;k++){
                        if ((k==l) || (k==l+1)){
                            days[s][k] = 5;
                        }
                        else {
                            days[s][k] = 4;
                        }
                    }
                }
            }
        }
        else if (date == 31) {
            for (int l=0;l<7;l++){
                if (input_days == name_days[l]){
                    for (int k=0;k<7;k++){
                        if ((k==l) || (k==l+1) || (k==l+2)) {
                            days[s][k] = 5;
                        }
                        else {
                            days[s][k] = 4;
                        }
                    }
                }
            }
        }
        
    }
    for (int z = 0; z<T; z++){
        for (int k=0;k<7;k++){
            cout << days[z][k] << "\ ";
        }
        cout << "\n";
    }
    return 0;
    }
    
