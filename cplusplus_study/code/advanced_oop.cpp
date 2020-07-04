#include <iostream>
#include <string>

/*
Inheritance(상속) 
개념 : 다른 클래스의 멤버 변수/메소드들을 물려받는 것
문법 : class 자식클래스 : class 부모클래스 {}
*/

class Vehicle {
    public :
        int wheels = 0;
        std::string color = "blue";

        void print() const {
            std::cout << "This" << Vehicle::color << " vehicle has " << Vehicle::wheels<<"\n";
        }
};

class Car : class Vehicle {
    public :
        bool sunroof = false;
};

int main() {

    return 0;
}