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
             (51, "Ватикан", "images_for_project/flags/flag_of_vatikan")]
bot = telebot.TeleBot('1214576878:AAGObjbzLmXg5dqLUfgRrFOABtb74ZaJvYo')

country = cursor.execute("SELECT * FROM countries").fetchall()
if len(country) == 0:
    cursor.executemany("INSERT INTO countries VALUES (?,?,?)", countries)
    conn.commit()

class UserModel:
    def __init__(self, database_row):
        self.chat_id = database_row[0]
        self.username = database_row[1]
        self.score = database_row[2]

    def get_string_representation(self):
        return self.username + " " + str(self.score)


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
    name_country = dbHelper.get_country_name_by_id(countryid[0][0])
    if message.text.lower()  == name_country[0][0].lower():
        bot.send_message(message.chat.id, "Правильно")
        dbHelper.increment_user_score(message.chat.id) 
    elif message.text.lower() != name_country[0][0].lower():
        bot.send_message(message.chat.id, "Неправильно Это страна :"  + name_country[0][0])
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
