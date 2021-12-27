"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json


KEYS_ARR = ['item', 'quantity', 'price', 'buyer', 'date']

# Либо красивый вывод с отступами
# def write_order_to_json(user_input):
#     temp_arr = {}
#     for index, val in enumerate(KEYS_ARR):
#         temp_arr[val] = user_input[index]
#         # print(temp_arr)
#     with open('orders.json', 'w', encoding='utf-8') as file:
#         json.dump(temp_arr, file, sort_keys=True, indent=4, ensure_ascii=False)

# Либо функционал позволяющий добавлять сколько угодно словарей по ключу orders
def write_order_to_json(user_input):
    temp_arr = {}
    for index, val in enumerate(KEYS_ARR):
        temp_arr[val] = user_input[index]
    with open('orders.json', encoding='utf-8') as file:
        json_str = json.loads(file.read())
        json_str['orders'].append(temp_arr)
    with open('orders.json', 'w', encoding='utf-8') as file:
        dict_as_string = json.dumps(json_str)
        # print('type(dict_as_string)', type(dict_as_string))
        file.write(dict_as_string)


if __name__ == '__main__':
    user_input = ['яблоко', 2, 1000, 'Жунин З.Й.', '02-03-2014']
    write_order_to_json(user_input)
