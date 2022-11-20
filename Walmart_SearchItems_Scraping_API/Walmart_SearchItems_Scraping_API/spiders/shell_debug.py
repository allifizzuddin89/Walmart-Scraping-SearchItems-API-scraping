import scrapy
from scrapy import Request
import json
from scrapy.shell import inspect_response


class ShellDebugSpider(scrapy.Spider):
    name = 'shell_debug'
    # allowed_domains = ['c']
    # start_urls = ['http://c/']

    url = 'https://www.walmart.com/search?q=automatic+espresso+machine&affinityOverride=default&page=1'

    headers ={
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52",
    }

    def start_requests(self):
        request = Request(
            url=self.url,
            headers=self.headers,
            callback=self.parse
        )
        yield request

    def parse(self, response):
        """
        Hidden API/Json in page source/element
        Easier to paginate using this method compare to API in network tool
        """
        inspect_response(response, self)
        # body_data = response.css('script[id="__NEXT_DATA__"]::text').get()
        # raw_data = json.loads(body_data)

        # """
        # Dumping the nested json object into text
        # Using the [Jsonpathfinder]('https://jsonpathfinder.com/') 
        # to find the path of the nested data
        # """
        # with open("walmart_raw.json", "w") as outfile:
        #     json.dump(raw_data, outfile, indent=4, sort_keys=True)
