# 1. Не используя библиотеки для парсинга,
# распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
#
# 2. * (вместо 1) Найти IP адрес спамера
# и количество отправленных им запросов по данным файла логов из предыдущего задания.

import requests

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
text = requests.get(url).text

with open('nginx_logs.txt.txt', 'w') as f:
    f.write(text)

spammer_dict = dict()

with open('nginx_logs.txt', encoding='utf-8') as f:
    line = f.readline()
    while line:
        ip_address = line.split()[0]
        if ip_address in spammer_dict:
            spammer_dict[ip_address] += 1
        else:
            spammer_dict[ip_address] = 1
        line = f.readline()

spammer_count_max = max(spammer_dict.values())
ip_spammer = [key for key, value in spammer_dict.items() if spammer_dict[key] == spammer_count_max][0]

print(f'IP-адрес спамера: {ip_spammer}\nКоличество запросов: {spammer_count_max}')
