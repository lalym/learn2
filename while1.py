names =["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
a=''
x=0
while a != 'Валера':
    a = list.pop(names)
    x = x + 1
    print('Не он.. ищу дальше..')
    if a == 'Валера':
        print('{} нашелся с {} раза!'.format(a,x))