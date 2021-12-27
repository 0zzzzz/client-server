"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию
файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml

yaml_arr = {
    'products': ['apples', 'oranges', 'lemons'],
    'warehouse': 23,
    'wh_rooms': {'jamazone': {
        'room3': {
            'article': '1782278й',
            'price': '100€'
        }},
        'worstbay': {
            'room27': {
                'article': '45645345й',
                'price': '1000€'
            }}
    }
}

with open('data_yaml.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(yaml_arr, file, default_flow_style=False, allow_unicode=True)

with open('data_yaml.yaml', encoding='utf-8') as file:
    F_N_CONTENT = yaml.load(file, Loader=yaml.FullLoader)
    print(F_N_CONTENT)

if __name__ == '__main__':
    pass
