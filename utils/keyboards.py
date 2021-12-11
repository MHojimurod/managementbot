from telegram import *
from telegram.ext.callbackcontext import CallbackContext
from utils import db
from constants import *
done = "✅"
prev = "⏮"
next = "⏭"
comment = "💬"
cross = "❌"
trash = "🗑"
reload = "🔄"

def send_number_keyboard() -> ReplyMarkup:
    return ReplyKeyboardMarkup([[KeyboardButton(text="📞 raqamni yuborish", request_contact=True)]], resize_keyboard=True)




def make_menu_keyboards():
    return ReplyKeyboardMarkup([[
        "So'rov yuborish", "Kutilayotgan so'rovlar"
    ],
    [
        "Tasdiqlanmagan so'rovlar"
    ]
    ], resize_keyboard=True)



def make_users_keyboard(update:Update, context:CallbackContext):
    keys = []
    try:
        users = db.get_users_list(update.message.from_user.id)
        tg_user = update.message.from_user
    except AttributeError:
        users = db.get_users_list(update.callback_query.from_user.id)
        tg_user = update.callback_query.from_user
    for user in users:
        if user['chat_id'] != tg_user.id:
            keys.append([
                InlineKeyboardButton(f"{user['name']}", url=f"http://t.me/{user['username']}"),
                InlineKeyboardButton(f"{done}" if user['id'] in context.user_data.get('request_confirmers', []) else f"{cross}", callback_data=f"remove_confirmer:{user['id']}" if user['id'] in context.user_data.get('request_confirmers', []) else f"add_confirmer:{user['id']}")
            ])
    keys.append([
        InlineKeyboardButton(f"{done} tayyor", callback_data="done_request"),
        InlineKeyboardButton(f"{cross} bekor qilish", callback_data="cancel_request")
    ])
    return InlineKeyboardMarkup(keys)