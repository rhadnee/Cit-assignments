 Find top movies on IMDB since 1980 using web scraping and save the result in a csv file. 
# # The csv file should have the following columns: title, year, rating, metascore, votes, gross, 
# # director, actors, runtime, genre, description. The csv file should be sorted by rating in descending order. 
# # The csv file should have the following columns: title, year, rating, metascore, votes, gross, director, actors, 
# # runtime, genre, description. The csv file should be sorted by rating in descending order.
# # https://www.imdb.com/search/title/?title_type=top-rated&year=1980,2022&sort=moviemeter,asc

#importing the libraries needed 
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from openpyxl.workbook import Workbook

# Declaring the headers 
headers = {"Accept-Language": "en-US,en;q=0.5"}

#declaring the list of empty variables, So that we can append the data overall
Title = []
Year = []
Runtime = []
Rating = []
Metascore = []
Votes = []
Gross = []
Description = []
Director = []
Actors = []
Genre = []

page = requests.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(page.text, 'html.parser')

movie_data = soup.find('tbody', class_ = 'lister-list').find_all('tr')


for movie in movie_data:
    name = movie.find('td', class_ = 'titleColumn').find('a').text
    Title.append(name)
    
    year_of_release = movie.find('td', class_ = 'titleColumn').span.text.strip('()')
    # for year_of_release in range(1980,2023):
    Year.append(year_of_release)

    rate = movie.find('td',class_ = "ratingColumn imdbRating").strong.text
    Rating.append(rate)

    url = 'https://www.imdb.com/' + movie.find('td', class_ = 'titleColumn').a.get('href')
    page2 = requests.get(url)
    soup2 = BeautifulSoup(page2.text, 'html.parser')

    movie_details = soup2.find('div', class_ = "sc-2a827f80-10 fVYbpg")
    
    # runtime = movie_details.find()
    # print(runtime)

    meta = movie_details.find('span', class_ = "score-meta").text
    Metascore.append(meta)

    all_genre = movie_details.find('div', class_ = "ipc-chip-list__scroller").find_all('a')
    
    for item in all_genre:
        genre = item.span.text
        Genre.append(genre)
    
    # Genre.append(genre)

    description = movie_details.find('span', class_ = "sc-16ede01-2 gXUyNh").text
    Description.append(description)

    director = movie_details.find('a', class_ = "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text
    Director.append(director)

    # director = movie_details.ul.li.div.text
    

    stars = movie_details.ul.li.find_next_sibling().find_next_sibling().div.ul.find_all('li')
    for x in stars:
        star = x.text
        Actors.append(star)
   
#     value = store.find_all('span', attrs = {'name': "nv"})
    
#     vote = value[0].text
#     votes.append(vote)
    
#     grosses = value[1].text if len(value)>1 else '%^%^%^'
#     gross.append(grosses)

         
# creating a dataframe
movie_list = pd.DataFrame({ "Movie Name": Title, "Year of Release" : Year,"Movie Rating": Rating, "Meatscore of movie": Metascore,
"Description": Description, "Director": Director, "Actor": Actors, 'Genre': Genre})
# # movie_list.head(5)

# # # #saving the data in excel format
# # movie_list.to_excel("Top 1000 IMDb movies.xlsx")

#If you want to save the data in csv format
movie_list.to_csv("Top Rated IMDb movies.csv")

print("Done")




# Scrap Hacker News project and save the result in a csv file. The csv file should have the 
# following columns: title, link, points, comments, author, rank. The csv file should be sorted 
# by rank in ascending order.

headers = {"Accept-Language": "en-US,en;q=0.5"}

Titles = []
Links = []
Points = []
Comments = []
Authors = []
Ranks = []

headers = {"Accept-Language": "en-US,en;q=0.5"}

for page in range(1, 27):
    try:
        source = requests.get(f"https://news.ycombinator.com/news?p={page}")
        source.raise_for_status()

        soup = BeautifulSoup(source.text, 'html.parser')
        
        movies = soup.find('table', class_ = 'itemlist').find_all('tr')
    

        for movie in movies:

            title = movie.find('span', class_ = "titleline").find('a').text

            Link = movie.find('span', class_ = 'titleline').find('a', href=True)

            Rank = movie.find('span', class_ = 'rank').text.strip('.')

            # Point = movie.find('td', class_ = 'subtext')
            # print(Point)
        
            # Comment = movie.find('a', href = True)
            # print(Comment['href'])
            # break

            Author = movie.find('td', class_ = 'subtext')
            print(Author)
            break
            # name = movie.find('td', class_ =  'titleColumn').a.text
            
            # rank = movie.find('td', class_ = 'titleColumn').get_text(strip = True).split('.')[0]
            
            # year = movie.find('td', class_ = 'titleColumn').span.text.strip('()')
            
            # rating = movie.find('td', class_ = 'ratingColumn imdbRating').strong.text
            # print(rating)
        

    except Exception as e:
        print(e)

data = pd.DataFrame({ "Title": Titles, "Link" : Links, "Rank": Ranks})

data2 = pd.DataFrame({"Point": Points, "Comment": Comments,"Author" : Authors })

data.to_csv("Hacker News.csv")
data2.to_csv("Hacker News.csv")