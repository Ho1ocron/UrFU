#pragma once

#include "book.h"
#include <vector>


class Ebook
{
private:
    int _storage;
    std::vector<Book> _books;

public:
    void set_storage(const int&);

    const int& get_storage() const;

    void add_book(const Book&);

    const std::vector<Book>& get_books() const;

    const Book& get_book(const int& book_number) const;

    Ebook operator+(const Book&);

    Ebook(int& storage) : _storage(storage) {}
};