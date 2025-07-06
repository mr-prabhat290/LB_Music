from BrandrdXMusic.core.bot import Hotty
from BrandrdXMusic.core.dir import dirr
from BrandrdXMusic.core.git import git
from BrandrdXMusic.core.userbot import Userbot
from BrandrdXMusic.misc import dbb, heroku
from SafoneAPI import SafoneAPI
from .logging import LOGGER

# Initialize system
dirr()
git()
dbb()
heroku()

# Start main apps
app = Hotty()
userbot = Userbot()
api = SafoneAPI()

# Load all platforms
from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

# Name your app
APP = "BRANDED_KUDI_BOT"  # Don't change this

# ✅ Import chatbot module to enable ChatGPT AI
from BrandrdXMusic.modules import chatbot
