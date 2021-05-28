import scrapy
from scrapy.linkextractors import LinkExtractor

class NutritionSpider(scrapy.Spider):
    name = 'nutrition'
    allowed_domains = ['http://nutritionvalue.org','nutritionvalue.org']
    start_urls = ['https://www.nutritionvalue.org/foods_by_Vitamin+C_content.html']
#    
    def parse(self, response):
         all_items = response.xpath(".//table[@class = 'full_width results zero']//text()")
         item_name =  response.xpath(".//td[@class = 'left']/a[@class = 'table_item_name']//text()").extract()
         vitaminC_level = response.xpath(".//td[@class = 'right']//text()").extract()
         products =zip(item_name,vitaminC_level)
         
         food = []
         
         for items in products:
             scraped_info = {
                'item_name' : items[0],
                'vitaminC_level' : items[1]
                   }
             yield scraped_info         
         next_page = response.xpath("//a[@class='nav']/@href")
         if next_page:
             for page in next_page:
                 url = response.urljoin(page[0].extract())
                 yield scrapy.Request(url, self.parse)
             
         
             
         #self.next_page =  response.xpath("//a[@class='nav']/@href").extract()
#         self.next_page = 'https://www.nutritionvalue.org/foods_by_Vitamin+C_content.html/' + self.next_page
#         self.next_page = self.next_page[-1]
#         
#         if self.next_page is not None:
#             yield scrapy.Request(response.urljoin(self.next_page),callback=self.parse)    
#        
#    
