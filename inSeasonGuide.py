
from sets import Set

janurary = Set([ 'celery', 'lettuce', 'mushrooms', 'potatoes', 'turnips'])
february = Set([ 'celery', 'lettuce', 'mushrooms', 'potatoes', 'turnips'])
march = Set([ 'lettuce', 'mushrooms', 'potatoes'])
april = Set([ 'lettuce', 'mushrooms', 'potatoes', 'asparagus', 'spinach', 'tomatoes'])
may = Set(['asparagus', 'lettuce', 'mushrooms', 'onions', 'peas', 'radishes', 'spinach', 'tomatoes', 'cabbage'])
june = Set([ 'tomatoes', 'strawberries', 'summer squash', 'radishes', 'peas', 'onions', 'mushrooms', 'lettuce', 'cauliflower', 'celery', 'cauliflower', 'cabbage', 'broccoli', 'beets', 'asparagus'])
july = Set(['lima beans', 'snap beans', 'beets', 'broccoli', 'cabbage', 'cantaloupe', 'carrots','cauliflower', 'celery', 'cucumbers', 'sweet corn', 'eggplant', 'lettuce', 'mushrooms','onions', 'peaches', 'peppers', 'radishes', 'raspberries', 'summer squash', 'tomatoes', 'watermelon'])



        
winter = janurary | february
spring = march | april | may
summer = june | july
months = [janurary, february, march, april, may, june, july]
    
def year():
    if month == 'janurary':
        return months[0]
    elif month == 'february':
        return months[1]
    elif month == 'march':
        return months[2]
    elif month == 'april':
        return months[3]
    elif month == 'may':
        return months[4]
    elif month == 'june':
        return months[5]
    elif month == 'july':
        return months[6]
    
def optionTwo(vegChoice):
    if vegChoice in janurary:
        return 'janurary'
    if vegChoice in february:
        return 'february'
    if vegChoice in march:
        return 'march'
    if vegChoice in april:
        return 'april'
    if vegChoice in may:
        return 'may'
    if vegChoice in june:
        return 'june'
    if vegChoice in july:
        return 'july'
    else:
        return 'Never. Does not grow here!'

def seasons(seasonChoice):
    if seasonChoice == 'winter':
        return winter
    elif seasonChoice == 'spring':
        return spring 
    elif seasonChoice == 'summer':
        return summer 
    
def optionFour(firstVeg, secondVeg):
    if firstVeg and secondVeg in janurary:
        return 'janurary'
    if firstVeg and secondVeg in february:
        return 'february'
    if firstVeg and secondVeg in march:
        return 'march'
    if firstVeg and secondVeg in april:
        return'april'
    if firstVeg and secondVeg in may:
        return 'may'
    if firstVeg and secondVeg in june:
        return 'june'
    if firstVeg and secondVeg in july:
        return 'july'
    else:
        return "They are not available in season at the same time!"   
if __name__ == "__main__":
    
    print """ Do you want to find out:
    1. what is in-season for a particular season
    2. when a fruit or vegetable is in-season
    3. what fruits and vegetables are in-season in a particular month
    4. Compare or contrast 2 vegetables or fruits"""
    howToUse = raw_input()

    if howToUse == "2":
        print "Find out when fruit/vegetables are in season in PA!"
        print "What fruit/ vegetable are you interested in learning about?"
        vegChoice = raw_input()
        print "-" * 30
        print "%s are in-season from:" %vegChoice
        print optionTwo()
    elif howToUse == "1":
        print "What season do you want to know about?"
        seasonChoice = raw_input()
        print "-" * 30
        print "In %s the following fruits and vegetables are in season:" %seasonChoice
        print seasons()
    elif howToUse == "3":
        print "What month would you like to know the in-season fruits and vegetables of?"
        month = raw_input()
        print "-"*30
        print "In %s you can locally find:" %month
        print year()
    elif howToUse == "4":
        print "So you want to know if you can find 2 fruits or vegetables in-season at the same time. What is the first one?"
        firstVeg = raw_input()
        print "What is the second?"
        print "-" *30
        secondVeg = raw_input()
        print "%s and %s can be both be found in-season during :" %(firstVeg, secondVeg)
        optionFour()
    
