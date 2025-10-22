#include <iostream>
#include <string>


class Book 
{
private:
    std::string _author;

public:
    void set_author(const std::string& author);

    std::string get_author();
};