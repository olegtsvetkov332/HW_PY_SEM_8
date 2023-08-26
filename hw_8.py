def add_contact(a, b):
    data = open('phone_book.txt', 'a', encoding='utf-8')
    data.write(name + ', ')
    data.write(number + '\n')
    data.close()

def open_book():
    data = open('phone_book.txt', 'r', encoding='utf-8')
    print(*data)
    data.close()

def continue_or_not():
    while True:
        temp = int(input('''Продолжить?
                        1 - да
                        0 - нет\n'''))
        if temp == 1:
            break
        else:
            quit()

def delete_contact(number):
    with open('phone_book.txt', 'r') as pb:
        lines = pb.readlines()
    with open('phone_book.txt', 'w') as pb:
        for line in lines:
            if line.strip('\n') != number:
                pb.write(line)

while True:
    temp = int(input('''Введите для продолжения \n
                 1 - посмотреть телефонный справочник \n
                 2 - внести новый контакт \n
                 3 - удалить существующий контакт \n
                 4 - найти существующий контакт по ФИО\n''')) #не работает, не стал доделывать, извините(
    if temp == 1:
        open_book()
        continue_or_not()
    if temp == 2:
        name = str(input('Введите ФИО: '))
        number = str(input('Введите номер: '))
        add_contact(name, number)
    if temp == 3:
        name_2 = str(input('Скопируйте и вставьте сюда строку из справочника, котрую хотите удалить0: '))
        delete_contact(name_2)
    if temp == 4:
        data = open('phone_book.txt', 'r', encoding='utf-8')
        print(data)
        data.close()