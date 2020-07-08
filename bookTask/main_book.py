from bookTask.book import Book
from bookTask.file_manager import *

def create_book():
    name = input('Введите название: ')
    genre = input("Введите жанр:")
    author = input('Введите автора: ')
    count = int(input('Кол-во книг: '))
    cost = int(input('Стоимость книги: '))

    b = Book(name, genre, author, cost, count, 0)
    return b

def show_books(books:list):
    #format
    i = 1
    print('%10s%30s%15s%30s%15s%15s' % ('Номер', 'Название', 'Жанр', 'Автор', 'Кол-во', 'Стоимость'))
    for book in books:
        print('%10s%30s%15s%30s%15s%15s' % (i, book.name, book.genre, book.author, book.count, book.cost))
        i += 1

def sort_by_name(book):
    return book.name

def sort_books(books:list):
    books.sort(key=lambda book: book.name)
    #books.sort(key=sort_by_name)
    #for book in sorted(books, key=sort_by_name):

def edit_book(books):
    show_books(books)
    choose1 = int(input("Введите номер книги, которую хотите отредактировать:"))
    print(f"1.{books[choose1 - 1].name}")
    print(f"2.{books[choose1 - 1].genre}")
    print(f"3.{books[choose1 - 1].author}")
    print(f"4.{books[choose1 - 1].count}")
    print(f"5.{books[choose1 - 1].cost}")
    choose2 = int(input("Что именно Вы хотите отредактировать:"))
    if choose2 == 1:
        books[choose1 - 1].name = input()
    elif choose2 == 2:
        books[choose1 - 1].genre = input()
    elif choose2 == 3:
        books[choose1 - 1].author = input()
    elif choose2 == 4:
        books[choose1 - 1].count = int(input())
    elif choose2 == 5:
        books[choose1 - 1].cost = int(input())

# def find_book(books):
#     print("1.По автору")
#     print("2.По названию")
#     print("3.По жанру")
#     choose = int(input())
#     if choose == 1:
#         a = input("Введите автора:")
#         i = 1
#         print('%10s%30s%15s%30s%15s%15s' % ('Номер', 'Название', 'Жанр', 'Автор', 'Кол-во', 'Стоимость'))
#         for book in books:
#             if book.author == a:
#                 print('%10s%30s%15s%30s%15s%15s' % (i, book.name, book.genre, book.author, book.count, book.cost))
#                 i += 1
#     elif choose == 2:
#         a = input("Введите название:")
#         i = 1
#         print('%10s%30s%15s%30s%15s%15s' % ('Номер', 'Название', 'Жанр', 'Автор', 'Кол-во', 'Стоимость'))
#         for book in books:
#             if book.name == a:
#                 print('%10s%30s%15s%30s%15s%15s' % (i, book.name, book.genre, book.author, book.count, book.cost))
#                 i += 1
#     else:
#         a = input("Введите жанр:")
#         i = 1
#         print('%10s%30s%15s%30s%15s%15s' % ('Номер', 'Название', 'Жанр', 'Автор', 'Кол-во', 'Стоимость'))
#         for book in books:
#             if book.genre == a:
#                 print('%10s%30s%15s%30s%15s%15s' % (i, book.name, book.genre, book.author, book.count, book.cost))
#                 i += 1

def comp_name(book, a):
    return book.name == a

def comp_author(book, a):
    return book.author == a

def comp_genre(book, a):
    return book.genre == a

def find_book(books):
    print("1.По автору")
    print("2.По названию")
    print("3.По жанру")
    choose = int(input())
    if choose == 1:
        f = comp_author
        a = input("Введите автора:")
    elif choose == 2:
        f = comp_name
        a = input("Введите название:")
    else:
        f = comp_genre
        a = input("Введите жанр:")

    i = 1
    print('%10s%30s%15s%30s%15s%15s' % ('Номер', 'Название', 'Жанр', 'Автор', 'Кол-во', 'Стоимость'))
    for book in books:
        if f(book, a):
            print('%10s%30s%15s%30s%15s%15s' % (i, book.name, book.genre, book.author, book.count, book.cost))
            i += 1


def increase_value(books):
    cost = int(input("На сколько увеличить стоимость книг:"))
    for book in books:
        book.cost += cost

def main():
    books = load_file()
    while True:
        print('1.Создать книгу')
        print('2.Вывести книги')
        print('3.Редактировать книгу')
        print('4.Поиск книги') #по автору, по автору и названию, по названию, по жанру
        print('5.Сортировка')
        print('6.Увеличение стоимости книг')
        print('0.Выход')

        choose = int(input())
        if choose == 0:
            break
        elif choose == 1:
            b = create_book()
            books.append(b)
            save_file(books)
        elif choose == 2:
            show_books(books)
        elif choose == 3:
            edit_book(books)
            save_file(books)
        elif choose == 4:
            find_book(books)
        elif choose == 5:
            sort_books(books)
        elif choose == 6:
            increase_value(books)
            save_file(books)

main()
