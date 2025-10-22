#include "main.h"
#include "book.h"


void Book::set_author(const std::string& author) {
    this->_author = author;
}


std::string Book::get_author() {
    return this->_author;
}


void Ebook::set_storage(const int& other) {
    this->_storage = other;
}


void Ebook::add_books(const Book& book) {
    this->_books.push_back(book);
}


void Ebook::set_storage(const int& storage) {
    this->_storage = storage;
}


int main() {
    Book book;
    std::string name = "Van";
    book.set_author(name);
    std::string author = book.get_author();

    std::cout << author << "\n";

    return 0;
}