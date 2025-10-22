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


const Book& Ebook::get_book(const int& book_number) const {
    return this->_books[book_number];
}


int main() {
    std::string name = "Book";
    std::string author = "Author";
    Book book{name, author};

    int storage = 10;
    Ebook ebook{storage};
    
    ebook.add_book(book);

    std::string book_name = book.get_name();

    Book get_ebook = ebook.get_book(0);
    std::cout << get_ebook.get_name() << "\n";

    return 0;
}