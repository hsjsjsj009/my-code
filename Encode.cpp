#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <experimental/random>
using namespace std;

string biner(int l){
    string temp_2;
    while (l >0) {
        temp_2 = to_string(l%2)+ temp_2;
        l=l/2;
    }
    return temp_2;
    }

string hexa(int k){
    string huruf[6] = { "A","B","C","D","E","F" };
    string temp_3;
    int temp;
    while (k>0){
        temp = k%16;
        if (temp>9){
            temp -= 10;
            temp_3 = huruf[temp] + temp_3;
        }
        else {
            temp_3 = to_string(temp) + temp_3;
        }
        k = k/16;
    }
    return temp_3;       
}

int main(){
    string name,k;
    int baris;
    cout << "Masukkan alamat file : "; cin >> name;
    ifstream my_file,my_2nd_file;
    my_file.open(name);
    my_2nd_file.open(name);
    for(string k; getline(my_file,k);){
        baris++;
    }
    my_file.close();
    string l[baris];
    int count = 0;
    int alphabet = 0;
    for (string j; getline(my_2nd_file,j);){
        l[count] = j;
        count++;
        alphabet += j.length();
    }
    int key[alphabet],o;
    int key2 = experimental::randint(1,alphabet); //last edited
    for (int gh = 0;gh<) // last edited
    for (int a = 0;a<baris;a++){
        for (string::iterator it=l[a].begin();it!=l[a].end(); ++it){
                key[o] = experimental::randint(10,99);
                cout << hexa(((int)*it)+key[o])<<" "<<a+2<<"\ ";
                o++;
        }
        cout << "\n";
    }
    cout << "\n";
    for (int k = 0;k<alphabet;k++){
        cout<<biner(key[k])<<"";
    }
} 

