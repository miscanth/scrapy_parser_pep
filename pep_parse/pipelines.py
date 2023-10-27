import time, os, csv
from pathlib import Path

#BASE_DIR = Path(__file__).parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR = Path(__file__).absolute().parent
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))

NAME_RESULT_DIR = 'results'
#RESULT_DIR = f'{BASE_DIR} / {NAME_RESULT_DIR}'
RESULT_DIR = BASE_DIR / NAME_RESULT_DIR
DATE_TIME = time.strftime('%Y-%m-%d_%H-%M-%S')
FILE_NAME = f'status_summary_{DATE_TIME}s.csv'

class PepParsePipeline:
    def __init__(self):
        self.pep_dict = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.pep_dict[item['status']] = self.pep_dict.get(item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        #RESULT_DIR.mkdir(exist_ok=True)
        #file_path = BASE_DIR / RESULTS_DIR / FILENAME.format(self.time)
        # filename = f'results/status_summary_{date_time}s.csv'
        filename = RESULT_DIR / FILE_NAME
        #filename = f'results/status_summary_{FILE_NAME}s.csv'
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, qty in self.pep_dict.items():
                f.write(f'{status},{qty}\n')
            f.write(f'Total,{sum(self.pep_dict.values())}\n')
