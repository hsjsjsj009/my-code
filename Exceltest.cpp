#include "E:\INSTALLER\CPP\libxl-win-3.8.3\libxl-3.8.3.0\include_cpp\libxl.h"
using namespace libxl;

int main() 
{
    Book* book = xlCreateBook(); // xlCreateXMLBook() for xlsx
    if(book)
    {
        Sheet* sheet = book->addSheet("Sheet1");
        if(sheet)
        {
            sheet->writeStr(2, 1, "Hello, World !");
            sheet->writeNum(3, 1, 1000);
        }
        book->save("example.xls");
        book->release();
    } 
    return 0;
}