import pandas as pd
import numpy as np

class BookLover():
    
    '''
    Tracks books read by name and rating
    
    This class provides methods for adding a book and its rating to a dataframe, confirming if a book has been read,
    calulating the amount of books read, and returning a dataframe of favorite books.
    
    Attributes:
    
    name : the name of the person (type:string)
    email : the person's email which serves as a unique identifier (type:string)
    fave_genre : the person's favorite genre (type:string)
    num_books : the number of books the person has read (type:int)
    book_list: a the name of the book and the rating (type: data frame)
    '''
    
    # initializes the instance. The num_books and book_list attributes are optional
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
    
    # adds a book and its rating to book_list if the book is not already in book_list
    def add_book(self, book_name, book_rating):
        if self.has_read(book_name):
            print(book_name + ' is already in your list')
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
    
    # returns true if the person has read the book (i.e the book_name is in book_list)
    def has_read(self, book_name):
        if (self.book_list['book_name'] == book_name).sum() > 0:
            return True
        else:
            return False
        
    # returns the number of books the person has read 
    def num_books_read(self):
        return (len(self.book_list))
    
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]