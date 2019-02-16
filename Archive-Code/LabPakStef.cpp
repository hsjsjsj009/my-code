#include <iostream>
#include <cstring>
#include <string>
#include <map>

using namespace std;

class Encrypt{
    public:
    void make_dictionary(char start){
        string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int started = alphabet.find(start);
        char *huruf = new char[26];
        for (int l =0;l<26;l++){
            if (started == 26){
                started = started-26;
            }
            *huruf[l]=alphabet[started];
            started += 1;
        }
        dictionary[start]=huruf;
        delete huruf;
        cout << dictionary.size() << "\n";
        for (map<char,char*>::iterator k=dictionary.begin();k!=dictionary.end(); ++k){
            cout << k->first << " " << k->second << "\n";
        }
        
    }
    private:
    map<char,char*> dictionary;
};

int main(){
    map<char,string> dict_key;
    string key,text;
    Encrypt enkripsi;
    cin >> key;
    for (string::iterator it=key.begin();it!=key.end();++it){
        cout << *it;
        enkripsi.make_dictionary(*it);
        cout << "\n";   
        }
}