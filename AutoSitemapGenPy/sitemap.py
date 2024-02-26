# Импортируем необходиные модули и классы
from __init__ import *
# Определение класса Sitemap
class Sitemap:
    # Инициализация класса
    def __init__(self, pages):
        self.pages = pages
        # Запрашиваем у пользователя URL-адрес сайта
        self.url = input('Enter your url [EXAMPLE: https://yourwebsite.com]\n==> ')
        # Устанавливаем значение changefreq_all и priority_all по умолчанию
        self.changefreq_all = 'daily'
        self.priority_all = 0.9
        # Создаем пустой список для приоритетов JSON
        self.priorityjson = []

    # Метод для добавления страниц из пути и URL-адресов
    def add_fromPath(self, path, urls, priority_all=0.5):
        # Добавляем данные в список приоритетов JSON
        self.priorityjson.append({
            "path": f"/{path}",
            "priority": priority_all
        })
        # Добавляем URL-адреса в список страниц
        for url in urls:
            self.pages.append(f'/{path}/{url}')

    # Метод для получения текущей даты в разных форматах
    def get_current_date(self, format_='__def__'):
        # Если указан формат 'UNIX', возвращаем текущее время в формате UNIX
        if format_ == 'UNIX':
            return str(int(round(time.time() / 60)))
        # В противном случае возвращаем текущую дату и время в формате "YYYY-MM-DDTHH:MM:SSZZ"
        else:
            return datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')

    # Метод для преобразования списка страниц в XML-строку с сitemap
    def to_string(self):
        # Создаем пустой набор URL-адресов, удаляя дубликаты
        urls_set = set(self.pages)

        # Создаем пустую строку XML схемы sitemap
        sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">"""

        # Для каждого URL-адреса в наборе страниц
        for url in urls_set:
            # Определяем директорию URL-адреса
            path = os.path.dirname(url)

            # Ищем соответствующий приоритет JSON для текущей директории
            for json_priority in self.priorityjson:
                if json_priority["path"] == path:
                    priority = json_priority["priority"]
                    break
            # Если такой директории не найдено, присваиваем приоритет по умолчанию
            else:
                priority = self.priority_all

            # Если в URL-адресе есть "index.", присваиваем приоритет 1.0
            if 'index.' in url:
                priority = 1.0

            # Добавляем текущий URL-адрес, дату последнего изменения, частоту изменения и приоритет в XML-строку
            sitemap_xml += f'    <url>\n        <loc>{self.url}{url}</loc>\n        <lastmod>{self.get_current_date()}</lastmod>\n        <changefreq>{self.changefreq_all}</changefreq>\n        <priority>{priority}</priority>\n    </url>\n'

        # Завершаем XML-строку схемой sitemap
        sitemap_xml += f"""    </urlset>\n"""

        # Возвращаем готовую XML-строку с сitemap
        return sitemap_xml

    # Метод для записи сгенерированного XML в файл
    def write(self, filename):
        # Открываем файл в режиме записи и кодировке UTF-8
        with open(filename, 'w', encoding='UTF-8') as xml_file:
            # Записываем в файл сгенерированную XML-строку с сitemap
            xml_file.write(self.to_string())
