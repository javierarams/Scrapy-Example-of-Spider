from scrapy.spider import Spider
from scrapy.selector import Selector

from espectador.items import EspectadorItem #We have to import the items that we created on items.py


class EspectadorSpider(Spider): #create the spider class...
    name = "espectador"
    allowed_domains = ["espectador.com"]
    start_urls = [
        "http://www.espectador.com/"
    ]

    def parse(self, response):  #and here its where the magic happens.

    #The parse() method is in charge of processing the response and 
    #returning scraped data (as Item objects) and more URLs to follow 
    #(as Request objects).
        
        for sel in response.xpath('//div[@id="columna_uno"]/article'):
        #ok. for every existing .../article on //div[@id="columna..."] 
        #the spider will recollect the following data
            item = EspectadorItem() #define item ()
            item['title'] = sel.xpath('h1/a/@title').extract()
            item['link'] = sel.xpath('h1/a/@href').extract()
            item['desc'] = sel.xpath('p/text()').extract()
            yield item
            #thats it




