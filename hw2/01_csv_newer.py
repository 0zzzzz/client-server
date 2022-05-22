"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных 
из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание 
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров 
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в 
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, 
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить 
в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». 
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных 
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
import csv
import chardet
import re

files_array = ['info_1.txt', 'info_2.txt', 'info_3.txt']
headers_array = [
    'Изготовитель системы',
    'Название ОС',
    'Код продукта',
    'Тип системы',
]
os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
main_list = [
    os_prod_list,
    os_name_list,
    os_code_list,
    os_type_list,
]
main_data = []


def get_data(files, headers, variables):
    final_list = []
    for txt_file in files:
        with open(txt_file, 'rb') as file:
            content = file.read()
        encoding = chardet.detect(content)['encoding']
        with open(txt_file, encoding=encoding) as file:
            for line in file:
                for num, val in enumerate(headers):
                    # По требованию заказчика от сих
                    if val not in main_data:
                        main_data.append(val)
                    # до сих
                    result = re.match(fr'{val}', line)
                    if result:
                        split_line = re.split(r':', line, maxsplit=1)
                        result = re.sub(r"^\s+", "", split_line[1]).replace('\n', '')
                        variables[num].append(result)
                    # по хорошему конечно до сих :)
    final_list.append(main_data)
    while len(os_prod_list) > 0:
        temp_list = []
        for val in variables:
            temp_list.append(val[0])
            val.remove(val[0])
        final_list.append(temp_list)
    # и вот это всё тоже
    return final_list


def write_to_csv(files, headers_arr, variables):
    data_list = get_data(files, headers_arr, variables)
    with open('my_csv.csv', 'w', encoding='utf-8') as file:
        file_write = csv.writer(file)
        for row in data_list:
            file_write.writerow(row)


if __name__ == '__main__':
    write_to_csv(files_array, headers_array, main_list)
