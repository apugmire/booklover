import unittest
import pandas as pd
import numpy as np

from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        
        test_object = BookLover('Bob', 'fakeemail@gmail.com', 'biographies')
        test_object.add_book('Tom Segura Biography', 5)
        
        actual = len(test_object.book_list)
        expected = 1
        
        self.assertEqual(actual,expected)
        
    def test_2_add_book(self):
        
        test_object2 = BookLover('Alysa', 'amp3xs@virginia.edu', 'fantasy')
        test_object2.add_book('Throne of Glass', 3)
        test_object2.add_book('Throne of Glass', 4)
        
        actual = len(test_object2.book_list)
        expected = 1
        
        self.assertEqual(actual,expected)
    
    def test_3_has_read(self):
        
        gomibooks = pd.DataFrame({'book_name':['Of Mice and Men', 'Uses of Catnip'], 'book_rating':[1, 5]})
        test_object3 = BookLover('Gomi', 'mycat@gmail.com', 'romance', 2, gomibooks)
        
        test_object3.add_book('100 Cutest Cats', 3)
        
        self.assertIs(test_object3.has_read('100 Cutest Cats'), True)

    def test_4_has_read(self):
        
        test_object4 = BookLover('Wasabi', 'mycat2@virginia.edu', 'historical fiction')
        
        test_object4.add_book('Six of Crows', 4)
        test_object4.add_book('When the Moon Hatched', 2)
        test_object4.add_book('WW2 Technology', 5)
        
        self.assertFalse(test_object4.has_read('Grapes of Wrath'), 'test_4_has_read() failed')
    
    
    def test_5_num_books_read(self):
        
        edamamebooks = pd.DataFrame({'book_name':['Book One', 'Book Two'], 'book_rating':[3, 4]})
        
        test_object5 = BookLover('Edamame', 'mycat3@hotmail.com', 'Manga', 2, edamamebooks)
        
        test_object5.add_book('Book Three', 1)
        test_object5.add_book('Book Four', 5)
        
        actual = test_object5.num_books_read()
        expected = 4
        
        self.assertEqual(actual, expected)
    
    def test_6_fav_books(self):
        
        test_object6 = BookLover('Same', 'sjk4tr@virginia.edu', 'inspirational')
        test_object6.add_book('Grapes of Wrath', 1)
        test_object6.add_book('Good Girls Guide to Murder', 5)
        test_object6.add_book('Icebreaker', 4)
        test_object6.add_book('WildFire', 3)
        
        faves = test_object6.fav_books()
        
        self.assertTrue((faves.book_rating > 3).sum() ==  2, "test_6_fav_books failed")

if __name__ == '__main__':
    
    unittest.main(verbosity=3)