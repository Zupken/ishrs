import lxml.html
import requests


class Scraping:

    def __init__(self):
        self.url = 'http://www.ishrs.org/physician/country/us'
        self.request = requests.get(self.url)

    def get_data(self):
        self.request = requests.get(self.url)
        self.tree = lxml.html.fromstring(self.request.content)
        self.etree = self.tree.xpath('//tbody/tr')
        print(self.etree)
        for item in self.etree:
            self.name = item.xpath('.//td[contains(@class, "full-name")]/text()')
            print(self.name)


Scraping = Scraping()
Scraping.get_data()