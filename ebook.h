#include "book.h"
#include <vector>


class Ebook : Book
{
private:
    int _storage;
    std::vector<Book> _books;

public:
    void set_storage(const int&);

    const int& get_storage() const;

    void add_book(const Book&);

    const std::vector<Book>& get_books() const;

    const Book& get_book(std::string& book_name) const;

    Ebook operator+(const Book&);

    Ebook(int& storage, std::vector<Book>& books) : _storage(storage), _books(_storage) {}
    ~Ebook();
};