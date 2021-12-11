class Config(object):
    LOGGER = True
    # REQUIRED
    API_KEY = "2136261295:AAGRm85AIjpG6hspmOwNtNUgPX_F6EJ7pUA"
    OWNER_ID = "1025888307" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "hoji"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = None# ' postgres://user_bot:user_id@198.211.105.120:5432/db_bot'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  
    DONATION_LINK = None  
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  
    STRICT_GBAN = False
    STRICT_GMUTE = False
    WORKERS = 8 
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'
    ALLOW_EXCL = False  
