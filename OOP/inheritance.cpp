#include <iostream>
#include <string>

class Robot
{
protected:
    std::string serial;
    std::string brand;

public:
    Robot(std::string serial, std::string brand) : serial(serial), brand(brand) {}

    void info()
    {
        std::cout << "This robot is part of the brand " << brand << " and has the following serial number: " << serial << std::endl;
    }
};

class BipedRobot : public Robot
{
public:
    std::string model = "1772.38418";

    BipedRobot(std::string serial, std::string brand, std::string model) : serial(serial), brand(brand), model(model) {}
};

int main()
{
    BipedRobot robot = BipedRobot(
        "BP1004",
        "ANYBotics",
    )

    return 0;
}