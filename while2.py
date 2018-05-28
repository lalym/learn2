def find_person(name, mylist):
    while True:
        if (name in mylist):
            print((name), "есть в списке.")
        else:
            print("Этого имени нет в списке.")
        break


mylist = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
name = input("Введите имя: ").capitalize()
find_person (name, mylist)