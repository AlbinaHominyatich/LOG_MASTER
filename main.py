import random
import logging

def rand_file(file_path, num):
    try:
        with open(file_path, 'w') as file:
            for i in range(num):
                data = random.randint(1, 100)
                file.write(str(data) + '\n')
                #далі допишіть логування
    #не забудьте except
#тут вам basic.Config
rand_file("input_random.txt", int(input("Кількість згенерованих чисел: ")))