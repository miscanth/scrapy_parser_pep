from pathlib import Path
import time


BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
FEED_EXPORT_ENCODING = 'utf-8'

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

FEED_EXPORT_FIELDS = {
    'number': 'Номер',
    'name': 'Название',
    'status': 'Статус',
}

ORDER_NUMBER = 300
ITEM_PIPELINES = {'pep_parse.pipelines.PepParsePipeline': ORDER_NUMBER}

BASE_DIR = Path(__file__).resolve().parent.parent
NAME_RESULT_DIR = 'results'
DATE_TIME = time.strftime('%Y-%m-%d_%H-%M-%S')
FILE_NAME = f'status_summary_{DATE_TIME}.csv'

SPIDER_NAME = 'pep'
ALLOWED_DOMAINS = ['peps.python.org']
START_URLS = ['https://peps.python.org/']
