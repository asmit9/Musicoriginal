from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

class Config(object):
    # required config variables
    API_HASH = getenv("API_HASH", "0e017f716c49a52a0ba4a8bfa95ccaf7")                # get from my.telegram.org
    API_ID = int(getenv("API_ID", "27896987"))                  # get from my.telegram.org
    BOT_TOKEN = getenv("BOT_TOKEN", "7223926558:AAH-0Z2AIcyI6W3g8F-SuV06gBMzc07G_xM")              # get from @BotFather
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://asmit9831:plmokn123@cluster0.1xdv6mh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")        # from https://cloud.mongodb.com/
    HELLBOT_SESSION = getenv("HELLBOT_SESSION", "BQBa9TG4pi1R_fPMS7gqzjSsny6EYv70dsx_NiXsdfg8Ou1rpGw7mbt_srQtpw3z7PvWX2YcPnH0QXRMVZesgzy53sKP3Mf-3aeYRi1VazYnUzaO0J0v5fN6kBzi1u_skICRaue2Vj0uwllV5-_NwiRx13GbaKqk8ZbA0NjPwtou-GnMJDj324ZIwqnQrNckbGHvG_H9SdPsJ6D8FdKcoL3Ih2qNffYF8snCAnLdlAcd8iUF0fwc-8oHmAADuCg3TFDSAGwnFGQuQP90q8L0d8kIhEOtdeoNkqVdCgOv62zivKGYs5XL7L0sOSiDUNwiBSRkPnAeo-E6n7ZH8eGL8KOaAAAAAaVCZwUA")  # enter your session string here
    LOGGER_ID = int(getenv("LOGGER_ID", 0))            # make a channel and get its ID
    OWNER_ID = getenv("OWNER_ID", "7067559685")                  # enter your id here

    # optional config variables
    BLACK_IMG = getenv("BLACK_IMG", "https://telegra.ph/file/2c546060b20dfd7c1ff2d.jpg")        # black image for progress
    BOT_NAME = getenv("BOT_NAME", "\x40\x4d\x75\x73\x69\x63\x5f\x48\x65\x6c\x6c\x42\x6f\x74")   # dont put fancy texts here.
    BOT_PIC = getenv("BOT_PIC", "https://te.legra.ph/file/5d5642103804ae180e40b.jpg")           # put direct link to image here
    LEADERBOARD_TIME = getenv("LEADERBOARD_TIME", "3:00")   # time in 24hr format for leaderboard broadcast
    LYRICS_API = getenv("LYRICS_API", None)             # from https://docs.genius.com/
    MAX_FAVORITES = int(getenv("MAX_FAVORITES", 30))    # max number of favorite tracks
    PLAY_LIMIT = int(getenv("PLAY_LIMIT", 0))           # time in minutes. 0 for no limit
    PRIVATE_MODE = getenv("PRIVATE_MODE", "off")        # "on" or "off" to enable/disable private mode
    SONG_LIMIT = int(getenv("SONG_LIMIT", 0))           # time in minutes. 0 for no limit
    TELEGRAM_IMG = getenv("TELEGRAM_IMG", None)         # put direct link to image here
    TG_AUDIO_SIZE_LIMIT = int(getenv("TG_AUDIO_SIZE_LIMIT", 104857600))     # size in bytes. 0 for no limit
    TG_VIDEO_SIZE_LIMIT = int(getenv("TG_VIDEO_SIZE_LIMIT", 1073741824))    # size in bytes. 0 for no limit
    TZ = getenv("TZ", "Asia/Kolkata")   # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

    # do not edit these variables
    BANNED_USERS = filters.user()
    CACHE = {}
    CACHE_DIR = "./cache/"
    DELETE_DICT = {}
    DWL_DIR = "./downloads/"
    GOD_USERS = filters.user()
    PLAYER_CACHE = {}
    QUEUE_CACHE =  {}
    SONG_CACHE = {}
    SUDO_USERS = filters.user()


# get all config variables in a list
all_vars = [i for i in Config.__dict__.keys() if not i.startswith("__")]
