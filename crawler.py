import scrapy
from scrapy.http import HtmlResponse

class SciKitLearnSpider(scrapy.Spider):
    name = "Sci-Kit Learn Spider"

    start_urls = ["https://scikit-learn.org/stable/modules/classes.html"]

    def parse(self, response):
        #modules = response.css("section").xpath("@id").getall()

        #modules = list(filter(lambda x: x.startswith(("module", "sklearn")), modules))

        #for module in modules:
        #    yield {
        #        "id": module 
        #    }

        for sel in response.xpath(".//*[@id='api-reference']"):
            for section in sel.css("section").xpath("@id"):
                print(section)