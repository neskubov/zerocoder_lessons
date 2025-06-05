import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]
    def __init__(self):
        self.cnt = 0

    def parse(self, response):
        pages = response.css('a.PaginationLink::attr(href)').getall()
        for page in pages:
            absolute_url = response.urljoin(page)
            yield scrapy.Request(url=absolute_url, callback=self.parse_detail)

    def parse_detail(self, response):
        line_svetilniki = response.css('div.lcSMD')
        for line in line_svetilniki:
            svetilniki = line.css('div.LlPhw')
            for svetilnik in svetilniki:
                if svetilnik.css('div.lsooF a.ui-GPFV8 span::text').get():
                    self.cnt += 1
                    yield {
                        'name': svetilnik.css('div.lsooF a.ui-GPFV8 span::text').get(),
                        'price': svetilnik.css('div.pY3d2 span::text').get(),
                        'url': svetilnik.css('div.lsooF a.ui-GPFV8').attrib.get('href', None),
                        'cnt': self.cnt
                    }

