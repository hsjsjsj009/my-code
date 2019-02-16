#include <iostream>
using namespace std;

int T,N,K;

int main(){
    cin >> T;
    string hasil;
    for (int k = 0 ;k<T;k++){
        cin >> N >> K;
        int A;
        for (int l = 0; l<N; l++){
            cin >> A;
            if ((K-A) >= 0 ) {
                K -= A;
                hasil += "1"; 
            }else {
                hasil += "0";
            }
        }
        cout << hasil;
        hasil = "";

        
    }
}