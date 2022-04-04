import pandas as pd
import csv

data = pd.read_excel(r'dataset.xlsx')

head = (data.columns)
"""[title, year, rated, released, runtime, genre, director, writer, actors, plot, language, country, awards, poster, ratings, metascore,
imdb_rating, imdb_votes, imdb_id, type, tomato_meter, tomato_image, tomato_rating, tomato_reviews, tomato_fresh, tomato_rotten, tomato_consensus,
tomato_user_meter, tomato_user_rating, tomato_user_reviews, tomato_url, dvd, box_office, production, website, response]"""


genre_comb_data = {('Drama', 'NULL'): 0}


for entry in data.genre:
    l = entry.split(", ")
    n = len(l)
    if n == 1:
        if (l[0], 'NULL') not in genre_comb_data.keys():
            genre_comb_data[(l[0], 'NULL')] = 1
        else:
            genre_comb_data[(l[0], 'NULL')] = genre_comb_data[(l[0], 'NULL')] + 1
    else:
        for i in range(n-1):
            for j in range(i+1,n):
                if ((l[i], l[j]) in genre_comb_data.keys()):
                    genre_comb_data[(l[i], l[j])] = genre_comb_data[(l[i], l[j])] + 1
                elif ((l[j], l[i]) in genre_comb_data.keys()):
                    genre_comb_data[(l[j], l[i])] = genre_comb_data[(l[j], l[i])] + 1
                else:
                    genre_comb_data[l[i], l[j]] = 1
                
with open('genrecombdata.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, csv.QUOTE_MINIMAL) 
    csvwriter.writerow(['genre_1', 'genre_2', 'frequency'])
    for x in genre_comb_data.items():
        y = list(x[0])
        y.append(x[1])
        csvwriter.writerow(y)   
        
        
genredict = {}
for entry in data.genre:
    l = entry.split(", ")
    for genre in l:
        if genre not in genredict.keys():
            genredict[genre] = 1
        else:
            genredict[genre] = genredict[genre] + 1

with open('genredata.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, csv.QUOTE_MINIMAL) 
    csvwriter.writerow(['genre', 'frequency'])
    for x in genredict.items():
        csvwriter.writerow(x)   