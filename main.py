import telebot
import os
import file_ops
import operations

a = file_ops

credentials = {"Member_Type": "", "En_Ro": "", "Date_of_Birth": "", "PassWord": ""}
bot = telebot.TeleBot("Telegram_Bot_Key")


def execute(fun, fname, message):  # function to execute a function
    if os.path.exists(fname):
        if a.getfile_age(fname) > 1:
            os.remove(fname)
            fun
            bot.send_photo(message.chat.id, photo=open(fname, "rb"))
        else:
            bot.send_photo(message.chat.id, photo=open(fname, "rb"))
    else:
        fun
        bot.send_photo(message.chat.id, photo=open(fname, "rb"))


@bot.message_handler(commands=["start", "help"])
def start_or_help(message):
    if message.text == "/start":
        bot.reply_to(message, "Welcome to StarBeam.")
        bot.send_message(message.chat.id, "Select /help in Menu to see all the commands")
    elif message.text == "/help":
        bot.reply_to(message, "The bot can perform the following operations-\n")
        bot.send_message(message.chat.id, "/credentials - enter your credentials (only once)\n"
                                          "/login - login to JUET website\n"
                                          "/attendance - fetch screenshot of attendance\n"
                                          "/faculty - who teaches what?\n"
                                          "/exam_marks - fetch your exam marks\n"
                                          "/view_cgpa - view your CGPA/SGPA\n"
                                          "/logout - logout from website")


@bot.message_handler(commands=["login", "logout"])
def init_login_or_logout(message):
    if message.text == "/login":
        bot.reply_to(message, "<<<Logging in>>>")
        operations.login()
        bot.send_message(message.chat.id, "You are now logged in :)")

    elif message.text == "/logout":
        bot.reply_to(message, "<<<Logging out>>>")
        operations.logout()
        bot.send_message(message.chat.id, "You are logged out :)")


@bot.message_handler(commands=["attendance"])
def fetch_attendance(message):
    fname = "attendance.png"
    bot.send_message(message.chat.id, "please wait...")
    execute(operations.attendance(), fname, message)


@bot.message_handler(commands=["exam_marks"])
def exam_marks(message):
    fname = "exam_marks.png"
    bot.send_message(message.chat.id, "please wait...")
    execute(operations.exam_marks(), fname, message)


@bot.message_handler(commands=["faculty"])
def subject_faculty(message):
    fname = "faculty_info.png"
    bot.send_message(message.chat.id, "please wait...")
    execute(operations.subject_faculty(), fname, message)


@bot.message_handler(commands=["view_cgpa"])
def view_cgpa(message):
    fname = "cgpa_table.png"
    bot.send_message(message.chat.id, "please wait...")
    execute(operations.view_cgpa(), fname, message)


bot.infinity_polling()
