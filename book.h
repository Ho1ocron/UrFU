#pragma once

#include <iostream>
#include <string>


class Book 
{
private:
    std::string _name;
    std::string _author;

public:
    // setters
    void set_author(const std::string& author);
    void set_name(const std::string& name);

    // getters
    const std::string& get_author() const;
    const std::string& get_name() const;

    Book(std::string& name, std::string& author) : _name(name), _author(author) {}
    ~Book() {std::cout << "Destructor called!" << std::endl;}

};