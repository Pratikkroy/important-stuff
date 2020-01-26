from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os

class Movie:
    
    def __init__(self, rank=0, title="", year=1970, link=""):
        self.rank = rank
        self.title = title
        self.year = year
        self.link = link

    def __str__(self):
        return self.rank + self.title + self.year + self.link

class ImdbScraping:

    def __init__(self):
        self.phantomJS_executable_path = r'/Users/roypra/Documents/phantomjs-2.1.1-macosx/bin/phantomjs'
        self.poster_dir_path = r'/Users/roypra/python/web_scraping/movie_posters'
        self.source_page_url = 'https://www.imdb.com/'
        self.top_250_movie_url = 'chart/top/?ref_=nv_mv_250'

    def get_soup(self):
        return BeautifulSoup(self.driver.page_source,'lxml')

    def initialise_driver(self):
        self.driver = webdriver.PhantomJS(executable_path = self.phantomJS_executable_path)

    def get_movies_list(self):
        self.initialise_driver()
        self.driver.get(self.source_page_url+self.top_250_movie_url)
        soup = self.get_soup()

        movies_list = []
        table = soup.find('table', class_ = 'chart')
        for td in table.find_all('td', class_ = 'titleColumn'):

            full_title = td.text.strip().replace('\n','')
            # print(full_title)

            rank, title = full_title.split('.',1)
            title, year = title.split('(',1)
            year = year.split(')',1)[0]
            a_tag = td.find('a')
            # print(rank, title, year, a_tag['href'])
            movies_list.append(Movie(rank, title, year, a_tag['href']))
        
        self.quit_driver()
        return movies_list


    def save_all_movies_poster(self, movies_list):
        
        for movie in movies_list:
            movie_page_url = self.source_page_url + movie.link
            self.initialise_driver()
            
            try:
                self.driver.get(movie_page_url)
            except Exception as ex:
                print("<----- Excxeption occurred at movie_page_url ----------------->")
                print(ex)

            soup = self.get_soup()

            div = soup.find('div', class_ = 'poster')
            a_tag = div.find('a')

            movie_poster_url = self.source_page_url + a_tag['href']
            self.initialise_driver()

            try:
                self.driver.get(movie_poster_url)
            except Exception as ex:
                print("<----- Excxeption occurred at movie_poster_url ---------------->")
                print(ex)

            soup = self.get_soup()

            all_div = soup.find_all('div', class_ = 'pswp__zoom-wrap')
            all_img = all_div[1].find_all('img')

            try:
                os.chdir(self.poster_dir_path)

                print(movie.rank, movie.title, all_img[1]['src'])
                self.save_poster(movie.title, all_img[1])
            except Exception as ex:
                print("<------- Directory does not exist --------->")
                print(ex)
            
            self.quit_driver()
            
            

    def save_poster(self, title, img):
        # f = open('{0}.jpg'.format(title.encode('utf8').replace(':','')), 'wb')
        f = open('{0}.jpg'.format(title), 'wb')
        f.write(requests.get(img['src']).content)
        f.close()

    def quit_driver(self):
        self.driver.quit()


if __name__ == '__main__':
    imdb_scraping = ImdbScraping()
    movies_list = imdb_scraping.get_movies_list()
    imdb_scraping.save_all_movies_poster(movies_list)


