import unittest
from inSeasonGuide import *

class inSeasonGuideTest(unittest.TestCase):
    def year_test(self):
        ''' The imputed month should match the month set'''
        testMonth = 'janurary'
        self.assertEqual(year(testMonth), months[0])
    
    def test_option_two(self):
        ''' if the choice of the vegetable or fruit is in the set janurary than janurary should be printed'''
        testVegChoice = 'lettuce'
        self.assertEqual(optionTwo(testVegChoice), 'janurary')
    def test_option_four_jan(self):
        ''' if the two vegetables are both in the set janurary than it should return janurary'''
        testFirstVeg = 'celery'
        testSecondVeg = 'lettuce'
        self.assertEqual(optionFour(testFirstVeg, testSecondVeg), 'janurary')
    def test_option_four_not_in_jan(self):
        '''if the veg choices aren't in janurary than it shouldn't return janurary'''
        testFirstVeg = 'peach'
        testSecondVeg = 'turnip'
        self.assertEqual(optionFour(testFirstVeg, testSecondVeg), 'They are not available in season at the same time!' )
        
    
    def test_seasons(self):
        '''if season selected is winter it should return winter vegetables'''
        testSeasonChoice = 'winter'
        self.assertEqual(seasons(testSeasonChoice), winter) 