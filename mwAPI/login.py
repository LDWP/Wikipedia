from mwAPI.user_config import SESSION, URL, HEADERS, LOGIN
from mwAPI.main import fetch_CSRF_token
def fetch_login_token():
    PARAMS = {
        "action": "query",
        "meta": "tokens",
        "type": "login",
        "format": "json"
    }

    RESPONSE = SESSION.get(url=URL, params=PARAMS)
    DATA = RESPONSE.json()
    LOGIN_TOKEN = DATA['query']['tokens']['logintoken']
    return LOGIN_TOKEN

def post_request_login(lgname):
    LOGIN_TOKEN = fetch_login_token()
    if not lgname:
        raise ValueError("Please define lgname before calling post_request_login.")

    PARAMS = {
        "action": "login",
        "lgname": lgname,
        "format": "json"
    }
    DATA = {
        "lgpassword": LOGIN[lgname],
        "lgtoken": LOGIN_TOKEN
    }

    RESPONSE = SESSION.post(url=URL, params=PARAMS, data=DATA, headers=HEADERS)
    DATA = RESPONSE.json()
    if 'login' in DATA:
        assert DATA['login']['result'] == 'Success'
    else:
        print(f"Login failed with error: {DATA.get('error', {}).get('info', 'Unknown error')}")

def logout():
    CSRF_TOKEN = fetch_CSRF_token()
    PARAMS = {
        'action': 'logout',
        'token': CSRF_TOKEN,
        'format': 'json'
    }
    RESPONSE = SESSION.post(url=URL, data=PARAMS, headers=HEADERS)
    DATA = RESPONSE.json()
    return DATA

if __name__ == "__main__":
    print("login.py ON")
    post_request_login("Pseudonyme1")