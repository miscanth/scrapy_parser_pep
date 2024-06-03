![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)


# Асинхронный парсер документов PEP на базе фреймворка Scrapy

### Описание проекта и используемые технологии

В проекте реализован парсинг документов PEP, а именно асинхронный парсер на базе специализированного фреймворка **Scrapy**. Результаты парсинга можно сохранять в формате CSV.

В парсере прописан единственный паук ***pep***. В его методах использованы как CSS-селекторы, так и ХPath-селекторы.
В качестве домена для парсинга установлен *peps.python.org*.

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


## Разработчик (исполнитель):
👩🏼‍💻 Юлия: https://github.com/miscanth