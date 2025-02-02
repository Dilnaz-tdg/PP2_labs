#1
def ifhigher(movie):
    return movie["imdb"] > 5.5

"""print(ifhigher({
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
}))"""

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#2 
def sublist(movies):
    morethan5 = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            morethan5.append(movie)
    return morethan5

"""ms = sublist(movies)
for movie in ms:
    print(movie["name"], movie["imdb"])"""


#3
def category(movies):
    moviescateg = []
    userc = input("Your category: ").strip().lower()
    for movie in movies:
        if movie["category"].lower() == userc:
            moviescateg.append(movie)
    return moviescateg

"""ms= category(movies)
for movie in ms:
    print(movie)"""

#4
def averagelist(movies):
    totalsc = sum(movie["imdb"] for movie in movies)
    return totalsc/len(movies)

"""print(f"avrage of all: {averagelist(movies):.2f}")"""

#5
def averageofcateg(movies):
    moviesctg = []
    userc = input("Your category: ").strip().lower()
    for movie in movies:
        if movie["category"].lower() == userc:
            moviesctg.append(movie)
    totalsum = sum(movie["imdb"] for movie in moviesctg)
    return totalsum/len(moviesctg)

"""print(f"average of your category: {averageofcateg(movies):.2f}")"""


