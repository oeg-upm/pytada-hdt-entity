
#include <string>
#include <iostream>
#include <list>

int abc(){
    return 10;
}

std::list<string> deref_list_string(std::list<string>* l){
    std::list<string> ll;
    cout << "cpp: size: "<<l->size()<<endl;
    ll = *l;
    delete l;
    return ll;
}







