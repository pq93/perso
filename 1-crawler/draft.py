from scrapy.selector import Selector
body = open('./5-scrapy/movie/imdbtop250.txt','r').read()
#print(body)
a = Selector(text=body).xpath('//tbody[@class="lister-list"]/tr/td[@class="posterColumn"]/span[@name="ir"]/@data-value').extract()
#b = Selector(text=a).xpath('./td[@class="titleColumn"]/a').extract()
print(a)
