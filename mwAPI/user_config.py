import requests
import sys

SESSION = requests.Session()
URL = "https://fr.wikipedia.org/w/api.php"
USERNAME = "Pseudonyme1"
TOOL_NAME = USERNAME + "-Py"
TOOL_VERSION = "1.0"
REQUESTS_VERSION = requests.__version__
PYTHON_VERSION = sys.version.split()[0]
USER_AGENT = f"{TOOL_NAME} (v:{TOOL_VERSION}, User:{USERNAME}) Python/{PYTHON_VERSION} requests/{REQUESTS_VERSION}"
# Exemple-Py (v:1.0, User:Exemple) Python/3.12.0 requests/2.31.0

HEADERS = {
    "User-Agent": USER_AGENT
}
LOGIN = {
    "Pseudonyme1":"BotPassword1", #Special:BotPasswords
    "Pseudonyme2":"BotPassword2"
    }