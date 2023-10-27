# scrapy_parser_pep

# Асинхронный парсер документов PEP на базе фреймворка Scrapy.

### Описание проекта и используемые технологии

При запуске паука ***pep*** парсер выводит два csv-файла:

1) В первый файл выводится список всех PEP: номер, название и статус.
2) Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество).
В конце также считается общее количество PEP.

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке: 
```
git clone git@github.com:miscanth/scrapy_parser_pep.git
```
Cоздать и активировать виртуальное окружение: 
```
python3.9 -m venv venv 
```
* Если у вас Linux/macOS 

    ```
    source env/bin/activate
    ```
* Если у вас windows 
 
    ```
    source env/scripts/activate 
    ```
```
python3.9 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить паука pep
```
scrapy crawl pep
```
