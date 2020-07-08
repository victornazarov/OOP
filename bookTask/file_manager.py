import pickle
import os

def save_file(books):
    with open('books.bin', 'wb') as file:
        pickle.dump(books, file)

def load_file():
    if os.path.exists('books.bin'):
        with open('books.bin', 'rb') as file:
            return pickle.load(file)
    return []
