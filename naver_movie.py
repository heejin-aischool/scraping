import requests
from bs4 import BeautifulSoup
import csv

soup_objects = []

URL = f'https://movie.naver.com/movie/running/current.nhn'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

movie_section = soup.select('ul[class=lst_detail_t1] > li')

movie_dict = []
for movie in movie_section:
    a_tag = movie.select_one('dl > dt > a')
    movie_title = a_tag.get_text()
    movie_code = a_tag['href'].split('=')[1]
    movie_data = {
        'title' : movie_title,
        'code' : movie_code
    }

    with open(f'naver_movie.csv', 'a', encoding='utf-8-sig', newline='') as file:
        fieldnames=['title','code']
        csvwriter = csv.DictWriter(file,fieldnames=fieldnames)
        csvwriter.writerow(movie_data)
