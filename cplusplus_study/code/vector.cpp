#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;
//using std::vector와의 차이점

int main() {
    vector<vector<int>> v {{1,2},{3,4}};  //이거 왜 돼지
    cout << "hello";
    
    // 스트림 연습
    string a("1 2 3");
    istringstream my_stream(a);

    int n;
    my_stream >> n;
    cout << n << '\n';

}