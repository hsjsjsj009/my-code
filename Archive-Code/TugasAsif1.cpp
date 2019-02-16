#include <iostream>
using namespace std;

int a[2],b[2][10],pangkat2,pangkat1;

int main(){
for (int i=0;i<2;i++){
    cin >> a[i];
    for (int j=a[i];j>-1;j--){
        cout <<"x^"<<j;cin>>b[i][j];
    }
}
pangkat1 = a[0];
pangkat2 = a[1];
int indikator[a[1]],save[a[1]],z;
bool test = false;

for (int k=a[0];k>-1;k--){
    for (int l=a[1];l>-1;l--){
        if ((b[0][k]*b[1][l]) >= 0){
            if (pangkat1 == a[0]){
                cout<<b[0][k]*b[1][l]<<"x^"<<pangkat1+pangkat2<<"\ ";
            pangkat2 -=1;
            }
            else{
              for (int b = 0;b<a[1];b++){
                    if ((pangkat1+pangkat2) == indikator[b]){
                        test = true;
                        z = b;
                    }
                }
                if (test){
                    cout<<"+ "<<b[0][k]*b[1][l]+save[z]<<"x^"<<pangkat1+pangkat2<<"\ ";
                    pangkat2 -=1;
                }
                else {
                    cout<<"+ "<<b[0][k]*b[1][l]<<"x^"<<pangkat1+pangkat2<<"\ ";
                    pangkat2 -=1;
                    indikator[l] = pangkat1+pangkat2;
                    save[l] = b[0][k]*b[1][l];
                }
            }
            }
        else if ((b[0][k]*b[1][l]) < 0) {
            if (pangkat1 == a[0]){
                cout<<b[0][k]*b[1][l]<<"x^"<<pangkat1+pangkat2<<"\ ";
            pangkat2 -=1;
            }
            else{
                for (int b = 0;b<a[1];b++){
                    if ((pangkat1+pangkat2) == indikator[b]){
                        test = true;
                        z = b;
                    }
                }
                if (test){
                    cout<<"- "<<(b[0][k]*b[1][l]+save[z])*-1<<"x^"<<pangkat1+pangkat2<<"\ ";
                    pangkat2 -=1;
                }
                else {
                    cout<<"- "<<b[0][k]*b[1][l]*-1<<"x^"<<pangkat1+pangkat2<<"\ ";
                    pangkat2 -=1;
                    indikator[l] = pangkat1+pangkat2;
                    save[l] = b[0][k]*b[1][l];
                }
            }
        }
    }
    pangkat1-=1;
    pangkat2 = a[1];
}

}


