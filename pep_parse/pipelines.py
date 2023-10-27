from .settings import BASE_DIR, FILE_NAME, NAME_RESULT_DIR


class PepParsePipeline:
    def __init__(self):
        self.pep_dict = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.pep_dict[item['status']] = (
            self.pep_dict.get(item['status'], 0) + 1
        )
        return item

    def close_spider(self, spider):
        filename = BASE_DIR / NAME_RESULT_DIR / FILE_NAME
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, qty in self.pep_dict.items():
                f.write(f'{status},{qty}\n')
            f.write(f'Total,{sum(self.pep_dict.values())}\n')
