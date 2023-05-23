#2
import logging

def write_file(fill_path, data):
    try:
        with open(fill_path, 'w') as file:
            file.write(data)
        #тут вам написати логгер про успішність запису в файл
    except Exception as e:
        logging.error(f'')#тут вам написати в якому файлі трапилася помилка і що саме {e}

#тут вам basic.Config
write_file("output.txt", input("Введіть що треба вписати в файл: "))