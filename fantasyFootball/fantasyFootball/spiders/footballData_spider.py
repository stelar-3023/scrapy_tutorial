import scrapy

class FootballDataSpider(scrapy.Spider):
    name = "fantasy"
    start_urls = [
        "https://www.pro-football-reference.com/years/2019/fantasy.htm"
        ]
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'fantasy-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)