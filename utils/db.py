import json
import requests
from sqlite3 import *
# from constants import *
host = "http://167.172.128.11"
# host = "http://192.168.0.188:8000"


def request_authorization(user_id: str, name_surname: str, number, user_name: str):
    res = requests.get(f'{host}/create_request_user/', json={
        "name": str(name_surname),
        "phone": str(number),
        "chat_id": str(user_id),
        "username": str(user_name)
    })
    return res.json()


def check_request_status(user_id: int):
    print(host)
    res = requests.get(f'{host}/check_user/', json={
        "chat_id": user_id
    })
    print(res)
    return res.json()


# check_user(2343434)

# def get_request_types() -> list:
#     res = requests.get(f'{host}/get_request_types/').json()
#     return res['data']



def get_admins_list(user_id: int):
    res = requests.get(f'{host}/admin_list/', json={
        "chat_id": user_id
    })
    if res.status_code == 200:
        return res.json()['data']
    else:
        return None

def get_users_list(user_id: int):
    res = requests.get(f'{host}/users_list/', json={
        "chat_id": user_id
    })
    if res.status_code == 200:
        return res.json()['data']
    else:
        return None


def accept_request_admin(user_id: int, req: int) -> bool:
    res = requests.get(f'{host}/update_status/', json={
        "admin": user_id,
        "rq": req,
        "status": 1
    })
    if res.status_code == 200:
        return res.json()
    else:
        return None


def deny_request_admin(user_id: int, req: int) -> bool:
    res = requests.get(f'{host}/update_status/', json={
        "admin": user_id,
        "rq": req,
        "status": 2
    })
    if res.status_code == 200:
        return res.json()
    else:
        return None

def get_request_types(user_id:id):

    res = requests.get(f'{host}/request_types/', json={
        "chat_id": user_id,
    })
    print(res.text)
    if res.status_code == 200:
        return res.json()
    else:
        return None

def get_req_type(user_id:int, name:str):
    reqs = get_request_types(user_id)
    for req in reqs['data']:
        if req['name'] == name:
            return req
    return None






def get_request(req_id:int):
    print(req_id)
    res = requests.get(f'{host}/get_request/', json={
        "req": req_id,
    })
    # print(res.text)
    if res.status_code == 200:
        return res.json()
    else:
        return None

def create_request(user_id:int, req_type:int, req_template:str):
    res = requests.get(f'{host}/create_request/', json={
        "req_type": req_type,
        "request_template": req_template,
        "user": user_id
    })
    if res.status_code == 200:
        return res.json()
    else:
        return None


def get_admins_by_list(admins:list[int], user_id:int):
    res = requests.get(f'{host}/get_admins_by_list/', json={
        "confirmers": admins
    })

    if res.status_code == 200:
        return res.json()
    else:
        return None



def get_request_from_user(user_id:int, req_id:int):
    res = requests.get(f'{host}/get_request_from_user/', json={
        "req_id": req_id,
    })
    print(res)
    if res.status_code == 200:
        return res.json()
    else:
        return None



def update_request_status(user_id:int, req_id:int, status:int, description:str=None):
    res = requests.get(f'{host}/request_status_update/', json={
        "req_id": req_id,
        "status": status,
        "chat_id": user_id,
        "desc": description
    })
    print(res.text)
    if res.status_code == 200:
        return res.json()
    else:
        return None



def get_waiting_sent_requests(user_id:int):
    res = requests.get(f'{host}/get_waiting_sent_requests/', json={
        "chat_id": user_id 
    })
    print(res,"AAA")

    if res.status_code == 200:
        return res.json()
    else:
        return None



def get_waiting_come_requests(user_id:int):
    res = requests.get(f'{host}/get_waiting_come_requests/', json={
        "chat_id": user_id 
    })
    try:
        return res.json()
    except:
        return None



def is_authed(user_id:int):
    db_user = check_request_status(user_id)
    return db_user['status'] == 1



def register_group(chat_id:int, name:int):
    res = requests.get(f'{host}/register_group/', json={
        "chat_id": chat_id,
        "name": name
    })
    print(res.text)
    try:
        return res.json()
    except:
        return None

def get_group(chat_id:int):
    res = requests.get(f'{host}/get_group/', json={
        "chat_id": chat_id,
    })
    try:
        return res.json()
    except:
        return None