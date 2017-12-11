import lxml.html
import requests
import database


class Scraping:

    def __init__(self):
        self.url = 'http://www.ishrs.org/physician/country/us'
        self.request = requests.get(self.url)
        self.data = {}

    def get_data(self):
        self.request = requests.get(self.url)
        self.tree = lxml.html.fromstring(self.request.content)
        self.etree = self.tree.xpath('//tbody/tr')
        for item in self.etree:
            self.name = item.xpath('.//td[contains(@class, "full-name")]/text()')
            self.adress = item.xpath('.//td[@class="views-field views-field-name"]/text()')
            self.city = item.xpath('.//td[contains(@class, "city")]/text()')
            self.province = item.xpath('.//td[contains(@class, "province")]/text()')
            self.country = item.xpath('.//td[contains(@class, "country")]/text()')
            self.work_data = [self.name, self.city, self.adress, self.province, self.country]
            self.data[self.etree.index(item)] = []
            for element in self.work_data:
                element = element[0].replace('', '').strip()
                self.data[self.etree.index(item)].append(element)

    def insert_data(self):
        Database = database.Database("data")
        Database.create_database()
        for i in self.data:
            Database.insert_data(self.data[i])
        Database.commit_changes()


Scraping = Scraping()
Scraping.get_data()
Scraping.insert_data()