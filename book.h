#include "main.h"
#include <vector>


class Ebook : Book
{
private:
    int _storage;
    std::vector<Book> _books;

public:
    void set_storage(const int&);

    const int& get_storage() const;

    void add_books(const Book&);

    const std::vector<Book>& get_books() const;

    Ebook operator+(const Ebook&);

    Ebook(int& storage, std::vector<Book>& books) : _storage(storage), _books(books) {}
    ~Ebook();
};