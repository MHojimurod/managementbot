from sqlite3 import *
class Messages_db:
    def __init__(self):
        self.db:Connection = connect('req_messages.db', check_same_thread=False)
        self.cur:Cursor = self.db.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS "messages" (
	        "id"	INTEGER NOT NULL UNIQUE,
	        "req"	INTEGER NOT NULL,
	        "msg_id"	INTEGER NOT NULL,
	        "chat_id"	INTEGER NOT NULL,
	        PRIMARY KEY("id" AUTOINCREMENT)
            );

            """)
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "requests" (
	        "id"	INTEGER NOT NULL UNIQUE,
	        "req_id"	INTEGER NOT NULL,
	        PRIMARY KEY("id" AUTOINCREMENT));""")
        

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS "messages_2" (
	        "id"	INTEGER NOT NULL UNIQUE,
	        "req"	INTEGER NOT NULL,
	        "msg_id"	INTEGER NOT NULL,
	        "chat_id"	INTEGER NOT NULL,
	        PRIMARY KEY("id" AUTOINCREMENT)
            );

            """)
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "requests_2" (
	        "id"	INTEGER NOT NULL UNIQUE,
	        "req_id"	INTEGER NOT NULL,
	        PRIMARY KEY("id" AUTOINCREMENT));""")
        self.db.commit()

    

    def exec(self, sql:str, *args):
        res = self.cur.execute(sql, *args)
        res = res.fetchall()
        self.db.commit()
        return res
    

    def create_request(self, req_id:int):
        self.exec(f"INSERT INTO requests(req_id) VALUES ({req_id})")
        res = self.exec(f"select * from  requests where req_id = {req_id}")
        return res
    
    def get_request(self, req_id:int):
        res = self.exec(f"select * from  requests where req_id = {req_id}")
        return res
    
    def create_message(self, req_id:int, message_id:int, chat_id:int):
        req = self.get_request(req_id)
        if len(req) == 0:
            raise Exception("Request not found")
        self.exec(f"INSERT INTO messages(req, msg_id, chat_id) VALUES ({req_id}, {message_id}, {chat_id})")
        res = self.exec(f"select * from  requests where req_id = {message_id}")
        return res
    
    def get_messages(self, req_id:int):
        res = self.cur.execute(f"SELECT * FROM messages WHERE req={req_id}")
        return self.cur.fetchall()
    




    def create_request_2(self, req_id:int):
        self.exec(f"INSERT INTO requests_2(req_id) VALUES ({req_id})")
        res = self.exec(f"select * from  requests_2 where req_id = {req_id}")
        return res
    
    def get_request_2(self, req_id:int):
        res = self.exec(f"select * from  requests_2 where req_id = {req_id}")
        return res
    
    def create_message_2(self, req_id:int, message_id:int, chat_id:int):
        req = self.get_request_2(req_id)
        if len(req) == 0:
            raise Exception("Request not found")
        self.exec(f"INSERT INTO messages_2(req, msg_id, chat_id) VALUES ({req_id}, {message_id}, {chat_id})")
        res = self.exec(f"select * from  messages_2 where req = {message_id}")
        return res
    
    def get_messages_2(self, req_id:int):
        print(req_id)
        res = self.cur.execute(f"SELECT * FROM messages_2 WHERE req={req_id}")
        return self.cur.fetchall()

msg_db = Messages_db()