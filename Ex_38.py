# Задача 38: Создать телефонный справочник возможностью добавления записей и чтения. 
# Пользователь также может ввести фамилию, тогда программа должны вывести на экран 
# все записи с этой фамилий. Также пользователь может добавлять новых людей в справочник 
# в режиме экспорт.

def inp():
    with open('tel_nums.txt', 'a', encoding='utf-8') as t_d:
        t_d.write('\n')
        s_name = str(input('Введите фамилию: ')+'\n')
        for info in s_name:
            t_d.write(info)
        name = str(input('Введите имя: ')+'\n')
        for info2 in name:
            t_d.write(info2)
        tel = str(input('Введите телефон: ')+'\n')
        for info3 in tel:
            t_d.write(info3)
        print('Данные сохранены, спасибо!')

def s_name():
    surname = input('Введите фамилию: ')
    with open('tel_nums.txt', 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        for i in range(len(text)):
            if text[i] == surname:
                for line in text[i:i+3]:
                    print(line)

def second_chance():
    mode_2 = int(input('Выберите режим ввода данных (1) или поиска контакта (2): '))
    if mode_2 == 1:
        inp()
    elif mode_2 == 2:
        s_name()
    else:
        print('Выберите 1 или 2')


mode = int(input('Выберите режим ввода данных (1) или поиска контакта (2): '))
if mode == 1:
    inp()
elif mode == 2:
    s_name()
else:
    second_chance()
    # print('Выберите 1 или 2')
