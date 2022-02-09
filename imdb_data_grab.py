from imdb import IMDb
import csv

fields = ['Name', 'Year', 'Runtime', 'Genres', 'Rating']

ia = IMDb()
search = ia.get_top250_movies()
count = 0
with open('test.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields)
    for i in search:
        id = ia.search_movie(str(i))
        movie = ia.get_movie(id[0].movieID)
        csvwriter.writerow([movie, movie.data['year'], movie.data['runtimes'][0], (', '.join(x for x in movie.data['genres'])), movie.data['rating']])
        count += 1
        print(count)
        if count == 100:
        	break
print('Done')