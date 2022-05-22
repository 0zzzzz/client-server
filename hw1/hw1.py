import chardet
import subprocess
import platform
import locale


# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

def convert(word):
    return type(word), word


print(convert('разработка'))
print(convert('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'))


# 2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это небходимо в автоматическом, а
# не ручном режиме с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы
# encode и decode) и определить тип, содержимое и длину соответствующих переменных.


def byte_type(word):
    return type(eval(f'b"{word}"')), eval(f'b"{word}"'), len(eval(f'b"{word}"'))


print(byte_type('class'))


# 3. Определить, какие из слов, поданных на вход программы, невозможно записать в байтовом типе. Для проверки
# правильности работы кода используйте значения: «attribute», «класс», «функция», «type»

def byte_type_try(word):
    try:
        return type(eval(f'b"{word}"')), eval(f'b"{word}"'), len(eval(f'b"{word}"'))
    except SyntaxError:
        return f'в байтовом типе возможно записать только строку состоящую из символов ASCII'


print(byte_type_try('класс'))


# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).

def encode_decode(word):
    # encoded_word = word.encode('utf-8')
    # return encoded_word.decode('utf-8')
    return str(bytes(word, encoding='utf-8'), encoding='utf-8')


print(encode_decode('разработка'))


# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый
# (предварительно определив кодировку выводимых сообщений).


def my_ping(site):
    default_encoding = locale.getpreferredencoding()
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '2', site]
    result = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in result.stdout:
        # result = chardet.detect(line)
        # print(line.decode(result['encoding']))
        print(line.decode(f'{default_encoding}'))


my_ping('yandex.ru')

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку созданного файла (исходить из того, что вам априори неизвестна кодировка этого
# файла!). Затем открыть этот файл и вывести его содержимое на печать. ВАЖНО: файл должен быть открыт без
# ошибок вне зависимости от того, в какой кодировке он был создан!

f = open('test_file.txt', 'w', encoding='utf-8')
f.write('сетевое программирование \nсокет \nдекоратор')
f.close()


def file_decode(file):
    with open(file, 'rb') as f:
        content = f.read()
    encoding = chardet.detect(content)['encoding']
    with open(file, encoding=encoding) as f_n:
        for el_str in f_n:
            print(el_str, end='')


file_decode('test_file.txt')
