from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class AirbnbItem(Item):
     tipo = Field()
     capacidad = Field()



class AirbnbCrawler(CrawlSpider):
     name = "MiPrimerCrawler"
     start_urls = ["https://www.airbnb.com.br/s/Londres--Reino-Unido/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Londres%2C%20Reino%20Unido&place_id=ChIJdd4hrwug2EcRmSrV3Vo6llI&source=structured_search_input_header&search_type=autocomplete_click"] 
     allowed_domains = ['airbnb.com']

     rules = (
          
     )