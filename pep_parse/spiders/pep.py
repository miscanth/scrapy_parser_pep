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
            pep_name = tr_tag.css('a::text')[1].get()
            yield response.follow(
                pep_link, callback=self.parse_pep, meta={'name': pep_name})

    def parse_pep(self, response):
        number = response.css(
            'ul.breadcrumbs li')[2].css('li::text').get().replace('PEP ', '')
        name = response.meta.get('name')
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
