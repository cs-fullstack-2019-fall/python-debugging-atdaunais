# ### Problem 7:
# Create the class Books with name, rating, genre, and author properties/attributes. Create a class method that will change the rating of the book. Outside of the class, create three objects of the class Book and put them in an array. Lastly, USING THE ARRAY print only the names of the books using any method we’ve learned in class.


class Books:
    def __init__(self, name, rating, genre, author):  # initializer only had one underscore on each side
        self.name = name
        self.rating = rating
        self.genre = genre
        self.author = author

    def changeRating(self, newRating):
        self.rating = newRating

# the word Programming was misspelled
book1 = Books("Programming Python", 10, "Non-Fiction", "Kenn")
book2 = Books("Programming JavaScript", 10, "Non-Fiction", "Kevin")
book3 = Books("Programming HTML", 10, "Non-Fiction", "Erin")

bookArray = [book1, book2, book3]

for eachBook in bookArray:
    print(eachBook.name)