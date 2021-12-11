from . import db
from .keyboards import *
from .msg_id import msg_db



import random

def send_code_to_sms(number):
    code = random.randint(111111, 999999)
    #code to send verification code by api
    print(code)
    return code


def is_odd(a):
    return bool(a - ((a >> 1) << 1))






def distribute(items, number) -> list[list]:
    res = []
    start = 0
    end = number
    for item in items:
        if items[start:end] == []:
            return res
        res.append(items[start:end])
        start += number
        end += number
    return res


def format_number(string:str):
        string  = str(string)
        j = len(string) % 3
        substrings = [string[3 * i + j:3 * (i + 1) + j] for i in range(len(string)//3)]
        if j != 0:
            substrings.insert(0, string[:j])
        return " ".join(substrings)


def is_confirmer(req, user):
    print(req)
    
    for conf in req['confirmers']:
        print(conf)
        if conf['chat_id'] == user.id:
            return True
    return False
