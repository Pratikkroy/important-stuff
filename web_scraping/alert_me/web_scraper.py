from bs4 import BeautifulSoup
from selenium import webdriver
import requests

class AmazonScraper:

    def __init__(self):
        self.source_page_url = 'https://www.amazon.in/Foxster-Peacoat-Black-Sneakers-9-4060979672765/dp/B07N7M4FT6/ref=sr_1_9?crid=60ARSX6P49D6&dchild=1&keywords=puma%2Bsneakers%2Bfor%2Bmen&qid=1580238034&sprefix=puma%2Caps%2C381&sr=8-9&th=1&psc=1'
        self.price_block_id = 'priceblock_ourprice'

    def get_response(self, url):
        # list of valid headers http://www.networkinghowtos.com/howto/common-user-agent-list/
        # headers is used to to validate ourselves
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        return requests.get(url, headers=headers)

    def get_shoes_price(self):
        response = self.get_response(url=self.source_page_url)
        soup = BeautifulSoup(response.content, features="lxml")
        # price_span = soup.find('span', {'id':"priceblock_ourprice"})
        price_text = soup.find(id=self.price_block_id).text
        price = price_text.replace("₹", "").replace(",","").strip()
        return float(price)
    

if __name__ == '__main__':
    scraper = AmazonScraper()
    shoes_price = scraper.get_shoes_price()
    print(shoes_price)