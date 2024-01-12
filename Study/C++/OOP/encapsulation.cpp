/*
    As you may see, encapsulation in C++ is different from Python: it adds and actual layer of protection by using the access mofier "private". Every attribute or method written within "private" will not be able to be directly accessed. If you uncomment the last line before the return, you will see that it will return an error!
 */

#include <iostream>
#include <string>

class Robot
{
private:
    std::string serial;
    std::string brand;

public:
    Robot(std::string serial, std::string brand) : serial(serial), brand(brand) {}

    void info()
    {
        std::cout << "This robot is made by " << brand << " and has a serial number " << serial << std::endl;
    }
};

int main()
{
    Robot robot = Robot("176357.87618723", "ANYBotics");
    robot.info();

    // std::cout << "\n\nBrand: " << robot.brand << std::endl;˜

    return 0;
}