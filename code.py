import time
import board
from adafruit_pyportal import PyPortal

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, make sure you have added them there!")
    raise


# Set up where we'll be fetching data from
DATA_SOURCE = "https://api.github.com/repos/adafruit/circuitpython"
STARS_COUNT = ["stargazers_count"]
REPO_NAME = ["full_name"]

# the current working directory (where this file is)
cwd = ("/" + __file__).rsplit("/", 1)[0]

pyportal = PyPortal(
    url=DATA_SOURCE,
    json_path=(REPO_NAME, STARS_COUNT),
    status_neopixel=board.NEOPIXEL,
    default_bg=cwd + "/bgs/terminal.bmp",
    text_font=cwd + "/fonts/Helvetica-Bold-24.bdf",
    text_position=((20, 160), (20, 280)),  # quote location  # author location
    text_color=(0xFFFFFF, 0xF291C7),  # quote text color  # author text color
    text_wrap=(30, 0),  # characters to wrap for quote  # no wrap for author
    text_maxlen=(180, 30),  # max text size for quote & author
    debug=True,
)

# speed up projects with lots of text by preloading the font!
pyportal.preload_font()

while True:
    try:
        value = pyportal.fetch()
        print("Response is", value)
    except (ValueError, RuntimeError) as e:
        print("Some error occured, retrying! -", e)
    time.sleep(60)
