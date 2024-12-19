class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' por {self.author}"


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
                print(f"- {book}")
        
def main():
    
    library = Library()

    book1 = Book("O Mágico de Oz", "L. Frank Baum")
    book2 = Book("1984", "George Orwell")

    library.add_book(book1)
    library.add_book(book2)

    library.show_books()

if __name__ == '__main__':
    main()
