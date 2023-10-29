import csv
from .settings import BASE_DIR, FILE_NAME, NAME_RESULT_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.pep_dict = {}

    def process_item(self, item, spider):
        self.pep_dict[item['status']] = (
            self.pep_dict.get(item['status'], 0) + 1
        )
        return item

    def close_spider(self, spider):
        filename = BASE_DIR / NAME_RESULT_DIR / FILE_NAME

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for status, qty in self.pep_dict.items():
                writer.writerow({'Статус': status, 'Количество': qty})
            writer.writerow(
                {'Статус': 'Total', 'Количество': sum(self.pep_dict.values())}
            )
