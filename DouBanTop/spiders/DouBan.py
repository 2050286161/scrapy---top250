from urllib.parse import urljoin

import scrapy
from scrapy import Selector, Request

from DouBanTop.items import DoubantopItem


class DoubanSpider(scrapy.Spider):
    name = "DouBan"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        item=DoubantopItem()
        selector=Selector(response)
        Movies=selector.xpath('//div[@class="info"]')
        for Movie in Movies:
            MovieData=Movie.xpath('div[@class="hd"]/a/span/text()').getall()
            MovieName="".join(MovieData)
            MovieInfo=Movie.xpath('div[@class="bd"]/div[@class="star"]/span/text()').get()
            Star = Movie.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[0]
            Quote = Movie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            # quote可能为空，因此需要先进行判断
            if Quote:
                Quote = Quote[0]
            else:
                Quote = ''
            item['MovieName'] = MovieName
            item['MovieInfo'] = ';'.join(MovieInfo)
            item['Star'] = Star
            item['Quote'] = Quote
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        # 第10页是最后一页，没有下一页的链接
        if nextLink:
            nextLink = nextLink[0]
            yield Request(urljoin(response.url, nextLink), callback=self.parse)
