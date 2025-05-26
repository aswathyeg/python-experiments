class Book:
    def __init__(self, title, auther, pages):
        self.title = title
        self.auther = auther
        self.pages = pages

    def is_thicker_than(self, other_book):
        return self.pages > other_book.pages


books = Book("title", "dsdd", 435)
books.is_thicker_than()
