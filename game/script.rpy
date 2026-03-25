# Characters

define me = Character('Мирон', color="#c8ffc8")
define thought = Character(None, kind=me, what_italic=True, what_prefix="(", what_suffix=")")
define sophie = Character('София', color="#ffc8c8")
define hobo = Character('Бездомный', color="#008e00")
define phone = Character('Телефон', color="#0000ff")
define anonym = Character('Голос', color="#0000ff")

# Variables

default inventory = []
default me_gave_money = False

# Configurations

transform sprite_scaler:
    zoom 0.6  # Adjust this number until the head fits
    yalign 1.0 # Ensures the feet stay on the ground

image hobo = At("hobo.png", sprite_scaler)



# Script

label start:

    scene living_room

    "Дзын! Дзынь! Дзынь!"
    thought "Ек. Проспал."
    "Дзын! Дзынь! Дзынь!"
    thought "Это Соня"
    me "Алло?"
    sophie "Привет, Мирон! Где Ты?"
    me "..."
    me "Дома. Я только что проснулся."
    me ""

    jump where_to_go_menu

    label where_to_go_menu:
        me "Что делать?"
        menu:
            "Првоерить ванную":
                me "Проверю-ка я ванную."
                scene bathroom
                me "Ничего интересного"
                jump where_to_go_menu

            "Проверить кухню":
                me "Может что-то на кухне?"
                scene kitchen
                jump where_to_go_menu
            
            "Проверить компьютер":
                scene pc_full
                me "Место где я провожу много времени."
                scene pc_left
                me "Глаза до сих пор красные... Или то не из-за компьютера, хех"
                scene pc_right
                jump where_to_go_menu

            "Проверить балкон":
                me "Выйду на балкон..."
                scene balcony
                me "Пусто. Ну и ладно."
                jump where_to_go_menu

            "Выйти на улицу":
                scene park1
                me "На улицу! Пора выносить мусор."

    me "Что мне нравится в моем новом месте жительства, так это то, что выход смотрит прямо на парк."
    me "Пройду через парк, а то уже целый день дома сидел."

    scene arc_to_trash

    me "Какой-то подозрительный мужчина идет навстречу..."

    hobo "Мелочи не найдется?"

    show hobo

    menu:
        "Держи":
            $ me_gave_money = True
            me "Держи!"
            hobo "Что? Всего лишь 10 долларов? Ты издиваешься? Вали отсюда!"
            me "Откуда такие люди берутся..."
            
        "Пошел вон!":
            me "Пошел вон отсюда!"
            hobo "Фырк!"
        
    scene trash

    me "Ну, мусор вынесен, можно идти домой!"

    if me_gave_money:
        jump phone_call
    else:
        jump room_ending
    

    label farewell:
        "Спасибо за игру! Конец!"
        return

    label room_ending:
        scene living_room
        me "Эх! Прогуляться было приятно, но дома все-таки лучше!"
        jump farewell

    label phone_call:
        phone "Звонок..."
        me "Хм. Незнакомый номер."
        me "Алло?"
        anonym "Если Ты живешь в нашем \"мегаполисе\", то приходи на адрес Эсмеральды 79. У двери увидишь кодовый замок. Жди меня внутри. Пароль семь - один - ..."
        phone "Звонок прерван."
        me "Там где не ждали... Что за странный звонок? И кто это был?"
        me "Что делать? Пойти по этому адресу или нет?"

        menu:
            "Пойти по этому адресу":
                me "Ну, а что? Может там что-то интересное будет."
                jump horse_ending
                
            "Пойти обратно домой":
                me "Да ну его. Пойду домой, там по-спокойнее."
                jump room_ending

    label horse_ending:
        scene pin1
        me "Это место выглядит странно. Что это за здание?"
        scene pin2
        me "Вот и кодовоый замок. Введу пароль..."
        jump horse_ending_password_enter



    label horse_ending_password_enter:
        $ user_input = renpy.input("Введите пароль:", length=6)
        $ user_input = user_input.strip()

        # Проверка
        if user_input == "718":
            me "Открылась... Кто же внутри...."
            play music "audio/loshadka_skryptonite.mp3" fadein 2.0
            scene pin_inside
            me "Не может... Не может быть... Это же..."
            me "ЛОШАДКА!!!!"
            me "Мне так жарко, не хватает слов"
            "Good ending: Моё сердце не стучит, а как Феррари кричит: «Врум»"
            scene black with dissolve
            jump farewell
        else:
            "Ошибка! Неверный пароль."
            jump horse_ending_password_enter

# show screen inventory_button # Показываем кнопку в углу
    
# "Вы нашли старый рюкзак."
    
# $ add_item("Яблоко")
# $ add_item("Jeep")

# "Теперь в вашем инвентаре есть пара вещей. Проверьте кнопку слева!"

# $ add_item("Мопед")

# "Боо"

# return

    