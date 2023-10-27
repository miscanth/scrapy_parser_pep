import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        section_tag = response.xpath('//section[@id="numerical-index"]')
        tbody_tag = section_tag.css('tbody tr')
        for tr_tag in tbody_tag:
            pep_link = tr_tag.css('a')[0]
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number = response.css('ul.breadcrumbs li')[2].css('li::text').get().replace('PEP ', '')
        data = {
            'number': number,
            'name': ' '.join(name.strip() for name in response.xpath('//h1[@class="page-title"]//text()').getall()).strip().replace(f'PEP {number} – ', ''),
            'status': response.css('dt:contains("Status") + dd abbr::text').get(),
            }
        yield PepParseItem(data)



"""data = {
'number': number,
'name': ' '.join(name.strip() for name in response.xpath('//h1[@class="page-title"]//text()').getall()).strip().replace(f'PEP {number} – ', ''),
'status': response.css('dt:contains("Status") + dd abbr::text').get(),
}
yield PepParseItem(data)"""

"""item = PepParseItem()
        item['Номер'] = number
        item['Название'] = ' '.join(name.strip() for name in response.xpath('//h1[@class="page-title"]//text()').getall()).strip().replace(f'PEP {number} – ', '')
        item['Статус'] = response.css('dt:contains("Status") + dd abbr::text').get()
        yield item"""