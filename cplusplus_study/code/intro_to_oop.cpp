/* getter / setter 쓰는 이유
 : 멤버 변수의 값에 제약이 있고, 임의로 값을 주기 싫을 대
 getter / setter 쓰지 않는 이유
  : 특별한 제약조건이 없으면 쓰지 않는게 가독성이 좋다 
*/

#include <iostream>

struct Date {
    public :
        int getDay() { return this->day;}
        void setDay(int day) { this->day = day;}
    private : 
        int day = 3;
        int month = 4;
        int year = 5;
};


/* struct 쓰는 이유
 : 멤버 변수에 제약조건이 없는 경우
class 쓰는 이유
 : 멤버 변수에 제약조건이 있는 경우
*/
class DateClass {
    public :
        DateClass( ) { //constructor
            
        }
        int getDay() { return this -> day;}
        void setDay(int day) { 
            if (day >=1 && day <= 31)
                this -> day = day;
            }
    private :
        int day = 5;
        int month = 4;
        int year = 3;
};

/*
class 와 namespace 차이
 : instance의 필요 유무
*/

namespace A {
    int Allo() { return 0; }
    const int x = 3;
};

namespace B {
    int Allo() { return 0; }
    const int x; // error

    void B() { B::x = 3; } // error
};

/*
Initializer Lists
개념 : 생성자가 돌기 전에, 즉 인스턴스가 생기기도 전에 변수값을 초기화해주는 것
사용법 : 생성자() : 변수명1(변수값1),변수명2(변수값2),... {생성자 body}
사용 이유 :
1. 생성자보다 빠르 ㄴ속도
2. 멤버 중 const는 오직 initializer lists로만 초기화 가능
3. 
*/

/*
Abstraction(추상화)
: 
*/

/*
Private Method
 : 
*/
int main(){
    Date date;
    
    std::cout << date.getDay();
    date.setDay(5);
    std::cout << date.getDay();

    DateClass date2;
    std::cout << date2.getDay();
    return 0;

    std::cout << A::x;
}