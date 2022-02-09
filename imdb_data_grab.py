from imdb import IMDb
from omdb import OMDBClient
import os
from dotenv import load_dotenv
import csv

#fields = ['Title', 'Year', 'IMDB ID', 'Country', 'Director', 'Genre', 'Metascore', 'Plot', 'Ratings', 'Runtime', 'imdbRating', 'tomato rating', 'tomato user rating']

load_dotenv()
OMDB_KEY = os.getenv("OMDB_KEY")

ia = IMDb()
omdb = OMDBClient(apikey=OMDB_KEY)

search = []
l = [line.rstrip() for line in open('100 most pop title list.txt')]
for x in l:
    y = (x.rstrip("\n").rpartition("\t")[-1])
    movie_parsed = y.rpartition(" ")
    search.append([movie_parsed[0], movie_parsed[-1][1:5]])

count = 0
with open('test.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow((omdb.get(title=search[0][0], year=search[0][1], tomatoes=True)).keys())
    for i in search:
        #id = ia.search_movie(str(i))
        #movie = ia.get_movie(id[0].movieID)
        movie = omdb.get(title=i[0], year=i[1], tomatoes=True)
        csvwriter.writerow(movie.values())
        count += 1
        print(count)
        if count == 100:
        	break
print('Done')