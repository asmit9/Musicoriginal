from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

class Config(object):
    # required config variables
    API_HASH = getenv("API_HASH", "c23506fc9beb78eaa5d234d70052c314")                # get from my.telegram.org
    API_ID = int(getenv("API_ID", "20001464"))                  # get from my.telegram.org
    BOT_TOKEN = getenv("BOT_TOKEN", "7314750666:AAEPmosb05poZF3pbgARgQCF4_Q5mgP8yBM")              # get from @BotFather
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://asmit9831:plmokn123@cluster0.1xdv6mh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")        # from https://cloud.mongodb.com/
    HELLBOT_SESSION = getenv("HELLBOT_SESSION", "BQAjab0vdZH8FZv7iN0KHgfBCa1xhmLNgTNt31oeXVHV8uV5EeweN30URn6kd1l6zfHTLN_2jPITZWOYdBwRnE_U6mqg62KmL2twMU52p9XnYAoRjm31cQCDHtK1Zf_SPAPzYg89cUvGZCo05kiQ-YBFr7rPWLqI_wvgZbu6Aa25Lbijx08VeLz9ogPXeJ4kKSqgLbf8H0_vSZtrHOyKGlSESnnUz55Wd_oKf06E5KlA2ARwR0lm3gs0fSs_GTm035r4NEzPpnR_j9wzuf57otF5LoyPwHl7YrcNpvad0pTlgPunlXAHwHbvJihm9RxQnjDN-aH3LALkK3nymkRXSOCGAAAAAbDhS9kA")  # enter your session string here
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002346148205"))            # make a channel and get its ID
    OWNER_ID = getenv("OWNER_ID", "7262522329")                  # enter your id here

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
