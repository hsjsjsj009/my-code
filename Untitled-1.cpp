#include <iostream>
#include <string>
using namespace std;

string SimpleSymbols(string str) { 
    int l = str.length();
    
    string hasil;
    for (int f = 0;f<l;f++){
        char b = str[l-1];
        char c = str[l+1];
        char a = '+';
        if ((f==0) && (isalpha(str[l]))){
            hasil = "false";
        }
        else if ((b==a) && (c==a) && (isalpha(str[l]))){
            hasil = "true";
        }
        else if ((f==l-1) && (isalpha(str[l]))){
            hasil = "false";
        }
        else {
            hasil = "false";
        }
    }
  // code goes here   
  return hasil; 
            
}

int main() { 
  
  // keep this function call here
  cout << SimpleSymbols("+d+=3=+s+");
  return 0;
    
} 