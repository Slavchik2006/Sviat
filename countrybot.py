import telebot
import sqlite3
import threading

lock = threading.Lock()
conn = sqlite3.connect("db.sqlite3", check_same_thread=False)
cursor = conn.cursor()
#!!!!!!!
cursor.execute("CREATE TABLE IF NOT EXISTS user_scores(chat_id integer PRIMARY KEY, name text, score int)")
cursor.execute("CREATE TABLE IF NOT EXISTS countries(id integer PRIMARY KEY, name text, path text)")
cursor.execute("CREATE TABLE IF NOT EXISTS chat_id(idcountry integer, chatid integer)")
countries = [(1, "Албания", "images_for_project/flags/flag_of_albania"),
             (2, "Алжир", "images_for_project/flags/flag_of_Algeria"),
             (3, "Андорра", "images_for_project/flags/flag_of_andorra"),
             (4, "Аргентина", "images_for_project/flags/flag_of_Argentina"),
             (5, "Австрия", "images_for_project/flags/flag_of_Austria"),
             (6, "Бельгия", "images_for_project/flags/flag_of_Belgium"),
             (7, "Беларусь", "images_for_project/flags/flag_of_belorussia"),
             (8, "Босния", "images_for_project/flags/flag_of_bosnia"),
             (9, "Бразилия", "images_for_project/flags/flag_of_Brazil"),
             (10, "Болгария", "images_for_project/flags/flag_of_Bulgaria"),
             (11, "Хорватия", "images_for_project/flags/flag_of_croatia"),
             (12, "Чехия", "images_for_project/flags/flag_of_czech"),
             (13, "Дания", "images_for_project/flags/flag_of_denmark"),
             (14, "Эстония", "images_for_project/flags/flag_of_estonia"),
             (15, "Финляндия", "images_for_project/flags/flag_of_Finland"),
             (16, "Франция", "images_for_project/flags/flag_of_France"),
             (17, "Германия", "images_for_project/flags/flag_of_Germany"),
             (18, "Великобритания", "images_for_project/flags/flag_of_Great_Britain"),
             (19, "Греция", "images_for_project/flags/flag_of_greece"),
             (20, "Венгрия", "images_for_project/flags/flag_of_Hungary"),
             (21, "Ирландия", "images_for_project/flags/flag_of_Ireland"),
             (22, "Исландия", "images_for_project/flags/flag_of_iseland"),
             (23, "Италия", "images_for_project/flags/flag_of_Italy"),
             (24, "Япония", "images_for_project/flags/flag_of_Japan"),
             (25, "Камерун", "images_for_project/flags/flag_of_Kameroon"),
             (26, "Канада", "images_for_project/flags/flag_of_Kanada"),
             (27, "Латвия", "images_for_project/flags/flag_of_latvia"),
             (28, "Лихтенштейн", "images_for_project/flags/flag_of_Liechtenstein"),
             (29, "Литва", "images_for_project/flags/flag_of_Litva"),
             (30, "Люксембург", "images_for_project/flags/flag_of_Luxemburg"),
             (31, "Северная Македония", "images_for_project/flags/flag_of_makedonia"),
             (32, "Мальта", "images_for_project/flags/flag_of_malta"),
             (33, "Молдова", "images_for_project/flags/flag_of_moldova"),
             (34, "Монако", "images_for_project/flags/flag_of_Monako"),
             (35, "Черногория", "images_for_project/flags/flag_of_montenegro"),
             (36, "Нидерланды", "images_for_project/flags/flag_of_Niderlands"),
             (37, "Норвегия", "images_for_project/flags/flag_of_norway"),
             (38, "Польша", "images_for_project/flags/flag_of_poland"),
             (39, "Португалия", "images_for_project/flags/flag_of_Portugal"),
             (40, "Румыния", "images_for_project/flags/flag_of_romania"),
             (41, "Россия", "images_for_project/flags/flag_of_Russia"),
             (42, "Сан-Марино", "images_for_project/flags/flag_of_sanmarino"),
             (43, "Сербия", "images_for_project/flags/flag_of_serbia"),
             (44, "Словакия", "images_for_project/flags/flag_of_slovakia"),
             (45, "Словения", "images_for_project/flags/flag_of_slovenia"),
             (46, "Испания", "images_for_project/flags/flag_of_spain"),
             (47, "Швеция", "images_for_project/flags/flag_of_sweden"),
             (48, "Швейцария", "images_for_project/flags/flag_of_Switzerland"),
             (49, "Украина", "images_for_project/flags/flag_of_Ukraine"),
             (50, "США", "images_for_project/flags/flag_of_USA"),
             (51, "Ватикан", "images_for_project/flags/flag_of_vatikan"),
             (52, "Афганистан", "images_for_project/flags/flag_of_afganistan"),
             (53, "Армения", "images_for_project/flags/flag_of_armenia"),
             (54, "Азербайджан", "images_for_project/flags/flag_of_azerbaijan"),
             (55, "Бахрейн", "images_for_project/flags/flag_of_bahrein"),
             (56, "Бангладеш", "images_for_project/flags/flag_of_bangladesh"),
             (57, "Бруней", "images_for_project/flags/flag_of_bruney"),
             (58, "Бутан", "images_for_project/flags/flag_of_butan"),
             (59, "Китай", "images_for_project/flags/flag_of_china"),
             (60, "Восточный Тимор", "images_for_project/flags/flag_of_east_timor"),
             (61, "Филиппины", "images_for_project/flags/flag_of_filippins"),
             (62, "Грузия", "images_for_project/flags/flag_of_georgia"),
             (63, "Индия", "images_for_project/flags/flag_of_india"),
             (64, "Индонезия", "images_for_project/flags/flag_of_indonesia"),
             (65, "Иордания", "images_for_project/flags/flag_of_iordania"),
             (66, "Иран", "images_for_project/flags/flag_of_iran"),
             (67, "Ирак", "images_for_project/flags/flag_of_iraq"),
             (68, "Израиль", "images_for_project/flags/flag_of_israel"),
             (69, "Камбоджа", "images_for_project/flags/flag_of_kambodja"),
             (70, "Казахстан", "images_for_project/flags/flag_of_kazakhstan"),
             (71, "Кипр", "images_for_project/flags/flag_of_kipr"),
             (72, "Киргизия", "images_for_project/flags/flag_of_kirgizia"),
             (73, "Кувейт", "images_for_project/flags/flag_of_kuveyt"),
             (74, "Лаос", "images_for_project/flags/flag_of_laos"),
             (75, "Ливан", "images_for_project/flags/flag_of_livan"),
             (76, "Малайзия", "images_for_project/flags/flag_of_malasia"),
             (77, "Мальдивы", "images_for_project/flags/flag_of_maldives"),
             (78, "Мьянма", "images_for_project/flags/flag_of_mianma"),
             (79, "Мексика", "images_for_project/flags/flag_of_Mexico"),
             (80, "Монголия", "images_for_project/flags/flag_of_mongolia"),
             (81, "Непал", "images_for_project/flags/flag_of_nepal"),
             (82, "Северная Корея", "images_for_project/flags/flag_of_north_korea"),
             (83, "ОАЭ", "images_for_project/flags/flag_of_oae"),
             (84, "Оман", "images_for_project/flags/flag_of_oman"),
             (85, "Пакистан", "images_for_project/flags/flag_of_pakistan"),
             (86, "Катар", "images_for_project/flags/flag_of_qatar"),
             (87, "Саудовская Аравия", "images_for_project/flags/flag_of_saudiaravia"),
             (88, "Шри-Ланка", "images_for_project/flags/flag_of_shri_lanka"),
             (89, "Сингапур", "images_for_project/flags/flag_of_singapour"),
             (90, "Сирия", "images_for_project/flags/flag_of_siria"),
             (91, "Южная Корея", "images_for_project/flags/flag_of_south_korea"),
             (92, "Таджикистан", "images_for_project/flags/flag_of_tadjikistan"),
             (93, "Таиланд", "images_for_project/flags/flag_of_tailand"),
             (94, "Турция", "images_for_project/flags/flag_of_turkey"),
             (95, "Туркменистан", "images_for_project/flags/flag_of_turkmenistan"),
             (96, "Узбекистан", "images_for_project/flags/flag_of_uzbekistan"),
             (97, "Вьетнам", "images_for_project/flags/flag_of_vietnam"),
             (98, "Йемен", "images_for_project/flags/flag_of_yemen"),
             (99, "Антигуа и Барбуда", "images_for_project/flags/flag_of_antigua"),
             (100, "Багамские острова", "images_for_project/flags/flag_of_bagames"),
             (101, "Барбадос", "images_for_project/flags/flag_of_barbados"),
             (102, "Белиз", "images_for_project/flags/flag_of_beliz"),
             (103, "Коста-Рика", "images_for_project/flags/flag_of_costarica"),
             (104, "Куба", "images_for_project/flags/flag_of_cuba"),
             (105, "Доминика", "images_for_project/flags/flag_of_dominika"),
             (106, "Доминиканская республика", "images_for_project/flags/flag_of_dominikana"),
             (107, "Гренада", "images_for_project/flags/flag_of_grenada"),
             (108, "Гаити", "images_for_project/flags/flag_of_haiti"),
             (109, "Гондурас", "images_for_project/flags/flag_of_honduras"),
             (110, "Гватемала", "images_for_project/flags/flag_of_hvatemala"),
             (111, "Ямайка", "images_for_project/flags/flag_of_jamaica"),
             (112, "Никарагуа", "images_for_project/flags/flag_of_nikaragua"),
             (113, "Панама", "images_for_project/flags/flag_of_panama"),
             (114, "Сент-Китс и Невис", "images_for_project/flags/flag_of_sentkits"),
             (115, "Сент-Люсия", "images_for_project/flags/flag_of_sentlucia"),
             (116, "Сент-Винсент и Гренадины", "images_for_project/flags/flag_of_sentvincent"),
             (117, "Тринидад и Тобаго", "images_for_project/flags/flag_of_trinidad"),
             (118, "Сальвадор", "images_for_project/flags/flag_of_salvador"),]
bot = telebot.TeleBot('1214576878:AAGObjbzLmXg5dqLUfgRrFOABtb74ZaJvYo')

country = cursor.execute("SELECT * FROM countries").fetchall()
if len(country) == 0:
    cursor.executemany("INSERT INTO countries VALUES (?,?,?)", countries)
    conn.commit()

class UserModel:
    def __init__(self, database_row):
        self.chat_id = database_row[0]
        self.first_name = database_row[1]
        self.score = database_row[2]

    def get_string_representation(self):
        return self.first_name + " " + str(self.score)


class DatabaseHelper:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def get_all_users(self):
        try:
            lock.acquire(True)
            users_in_database = cursor.execute("SELECT * FROM user_scores").fetchall()
        finally:
            lock.release()            
        return [UserModel(user) for user in users_in_database]

    def get_user_with_chat_id(self, chat_id):
        try:
            lock.acquire(True)
            user = cursor.execute("SELECT chat_id FROM user_scores WHERE chat_id = ?", [chat_id]).fetchall()
        finally:
            lock.release()            
        

    def increment_user_score(self, chat_id):
        try:
            lock.acquire(True)
            cursor.execute("UPDATE user_scores SET score = score + 1 WHERE chat_id = ?", [chat_id])
            conn.commit()
        finally:
            lock.release()   
        

    def get_country_name_by_id(self, id):
        try:
            lock.acquire(True)
            country_name = cursor.execute("SELECT name FROM countries WHERE id = ?", [id]).fetchall()
        finally:
            lock.release() 
        return country_name

dbHelper = DatabaseHelper(cursor, conn)


def insert_question(chat_id, country_id):
    try:
        lock.acquire(True)
        cursor.execute("INSERT INTO chat_id VALUES(?,?)", [country_id, chat_id])
    finally:
        lock.release() 
    conn.commit()

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, 'Привет! Для того чтобы начать играть напиши /game, чтобы посмотреть количество очков напиши /stats')

@bot.message_handler(commands=['stats'])
def score(message):
    users_in_leaderboard = dbHelper.get_all_users()
    message_text = ""
    for user in users_in_leaderboard:
        message_text += user.get_string_representation() + "\n"
    bot.send_message(message.chat.id, message_text)

def get_country(message):
    try:
        lock.acquire(True)
        countryid = cursor.execute("SELECT idcountry FROM chat_id WHERE chatid = ?", [message.chat.id]).fetchall()
    finally:
        lock.release()
    print(countryid)
    if len(countryid) == 0:
        print("error")
    else:     
        name_country = dbHelper.get_country_name_by_id(countryid[0][0])
        if message.text.lower()  == name_country[0][0].lower():
            bot.send_message(message.chat.id, "Правильно")
            dbHelper.increment_user_score(message.chat.id) 
        elif message.text.lower() != name_country[0][0].lower():
            bot.send_message(message.chat.id, "Неправильно Это страна : "  + name_country[0][0])
        print(name_country)
        try:
            lock.acquire(True)
            cursor.execute("DELETE FROM chat_id WHERE chatid = ?", [message.chat.id])
            conn.commit()
        finally:
            lock.release()    
        game(message)



   
@bot.message_handler(commands=['game'])
def game(message):
    # print(type(message.chat.id))
    try:
        lock.acquire(True)
        user_in_leaderboard = cursor.execute("SELECT chat_id FROM user_scores WHERE chat_id = ?", [message.chat.id]).fetchall()
    finally:
        lock.release()
    if len(user_in_leaderboard) == 0:
        try:
            lock.acquire(True)
            cursor.execute("INSERT INTO user_scores VALUES(?,?,?)", [message.chat.id, message.chat.username, 0])
            conn.commit()
        finally:
            lock.release()
    try:
        lock.acquire(True)
        cursor.execute("SELECT * FROM countries ORDER BY RANDOM() LIMIT 1")
        country = cursor.fetchall()[0]
    finally:
            lock.release()    
    bot.send_photo(message.chat.id, photo=open(country[2] + '.jpg', 'rb'))
    bot.send_message(chat_id=message.chat.id, text="Чьей страны этот флаг?")
    insert_question(message.chat.id, country[0])

@bot.message_handler(content_types=['text'])
def resolve(message):
    
    get_country(message)

    idcountry = ""
    #country_id = dbHelper.get_country_id_by_name(country_name)
    if idcountry == -1:
        bot.send_message(message.chat.id, "Нет такой страны")
        return



    # сходить в базу и найти для этого чата какая загадана страна
    # сравнить, та ли это страна
    # если да, добавить очко.
    # если нет, сказать пробовать дальше.



bot.polling()
