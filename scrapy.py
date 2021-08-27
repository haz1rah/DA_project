#Import Module
import scrapy

# Create New Spider
class NewSpider(scrapy.Spider):
    #Spider Name
    name = "new_spider"
    #Target Website
    start_urls = ['http:']

    #Define parser
    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

        #To recurse next page
        Page_selector = '.next a ::atr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )
