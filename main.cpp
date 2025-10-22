#include "book.h"
#include "ebook.h"


void Book::set_author(const std::string& author) {
    this->_author = author;
}


const std::string& Book::get_author() const {
    return this->_author;
}


void Book::set_name(const std::string& name) {
    this->_name = name;
}


const std::string& Book::get_name() const {
    return this->_name;
}


void Ebook::set_storage(const int& other) {
    this->_storage = other;
}


void Ebook::add_book(const Book& book) {
    this->_books.push_back(book);
}


Ebook Ebook::operator+(const Book& other) {
    this->_books.push_back(other);
}


const Book& Ebook::get_book(std::string& book_name) const {
    for (size_t i; i < _books.size(); ++i) {
        if (_books[i].get_name() == book_name) {
            return _books[i];
        }
    }
}


int main() {
    Book book;
    std::string name = "Van";
    book.set_author(name);
    std::string author = book.get_author();

    std::cout << author << "\n";

    return 0;
}