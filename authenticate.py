from telegram.ext import *
from telegram import *
from utils import *
from constants import *

class _Authentication:
    def name(self, update:Update, context:CallbackContext):
        if update.message.text != "/start":
            context.user_data['name'] = update.message.text
            context.user_data['greeting'].delete()
            context.user_data['request_register_number'] = update.message.reply_text("Iltimos endi raqamingizni yuboring!", reply_markup=send_number_keyboard())
            return NUMBER
        else:
            update.message.reply_text("Iltimos ismingizni to'g'ri yozing!") 
    
    def number(self, update:Update, context:CallbackContext):
        context.user_data['number'] = update.message.text or update.message.contact.phone_number
        name = context.user_data['name']
        number = context.user_data['number']
        username = update.message.from_user.username
        user_id = update.message.from_user.id
        res = db.request_authorization(user_id, name, number, username)
        if res != None and res['ok']:
            update.message.reply_text("Sizning so'rovingiz qabul qilindi!\nRuhsat berilganda o'zimiz malum qilamiz!\nAgarda uzoq vaqt habar kelmasa /start kommandasini yuboring!")
            admins = db.get_admins_list(update.message.from_user.id)
            req = msg_db.create_request(res['rq_id'])
            text = f"Tizimga kirish uchun so'rov noma!\n<b>Ismi</b>: {name}\n<b>Raqami</b>: {number}\n<b>Username</b>: {username}"
            keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(f"{done} Ruhsat berish", callback_data=f"accept_request:{res['rq_id']}"), InlineKeyboardButton(f"{cross} rad etish" , callback_data=f"deny_request:{res['rq_id']}")
            ]])
            for admin in admins:
                try:
                    msg_id = context.bot.send_message(text=text, chat_id=admin['chat_id'], reply_markup=keyboard, parse_mode="HTML")
                    msg_db.create_message(req[0][1], msg_id.message_id, admin['chat_id'])
                except Exception as e: print(e)
        return WAIT

    def description(self, update:Update, context:CallbackContext):
        name = context.user_data['name']
        number = context.user_data['number']
        username = update.message.from_user.username
        user_id = update.message.from_user.id
        res = db.request_authorization(user_id, name, update.message.text, number, username)
        if res != None and res['ok']:
            update.message.reply_text("Sizning so'rovingiz qabul qilindi!\nRuhsat berilganda o'zimiz malum qilamiz!\nAgarda uzoq vaqt habar kelmasa /start kommandasini yuboring!")
            admins = db.get_admins_list(update.message.from_user.id)
            req = msg_db.create_request(res['rq_id'])
            text = f"Tizimga kirish uchun so'rov noma!\n<b>Ismi</b>: {name}\n<b>Raqami</b>: {number}\n<b>Username</b>: {username}"
            keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(f"{done} Ruhsat berish", callback_data=f"accept_request:{res['rq_id']}"), InlineKeyboardButton(f"{cross} rad etish" , callback_data=f"deny_request:{res['rq_id']}")
            ]])

            for admin in admins:
                try:
                    msg_id = context.bot.send_message(text=text, chat_id=admin['chat_id'], reply_markup=keyboard, parse_mode="HTML")
                    msg_db.create_message(req[0][1], msg_id.message_id, admin['chat_id'])
                except Exception as e: print(e)
        return WAIT
    

    def wait_start(self, update:Update, context:CallbackContext):
        user = update.message.from_user if update.message != None else update.callback_query.from_user
        message = update.message if update.message != None else update.callback_query.message
        res = db.check_request_status(user.id)
        print('kirdi')
        if res['status'] == 0:
            print(0)
            message.reply_text(f"Sizning so'rovingiz kutilmoqda!", reply_markup=ReplyKeyboardRemove())
        elif res['status'] == 2:
            print(2)
            message.reply_text(f"Sizning so'rovingiz bekor qilingan!", reply_markup=ReplyKeyboardRemove())
        elif res['status'] == 1:
            keys = keyboards.make_menu_keyboards()
            update.message.reply_text("Bosh menu!", reply_markup=keys)
            return MENU
        elif res['status'] == 3:
            print(3)
            print(user.id)
            message.reply_text(f"Kechirasiz siz tizimdan haydaldingiz!", reply_markup=ReplyKeyboardRemove())
        else:
            print(4)
            context.user_data['greeting'] = message.reply_text(user.id, "Kechirasiz sizning so'rovingiz topilmadi!\nIltimos qayta ro'yxatdan o'ting!\nIsmingizni yuboring!", reply_markup=ReplyKeyboardRemove())
            return NAME

        

authentication = _Authentication()
