dialogs = {"привет": "И тебе привет!", "как дела": "Лучше всех"}
bye="Пока"

def get_answers (ask, dialogs):
    if ask in dialogs:
        return (dialogs.get(ask.lower()))




def ask_user():
    try:
        while True:
            ask = input('Как дела? \n')
            #не работает при вводе "Пока"
            if ask != bye.lower():
                print(get_answers(ask, dialogs))
            else:
                print('До встречи!')
                break
    except KeyboardInterrupt:
        x = print("\nБыло приятно пообщаться!")
        return x
ask_user()